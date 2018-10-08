from datetime import datetime

from elo import calculate_elo
from init import db, ma
from models.player import basic_player_schema, Player
from models.team import Team, team_schema
from marshmallow import fields
from trueskill import Rating, rate


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    team1_attacker_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    team1_attacker = db.relationship('Player', foreign_keys=[team1_attacker_id])

    team1_defender_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    team1_defender = db.relationship('Player', foreign_keys=[team1_defender_id])

    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team1 = db.relationship('Team', foreign_keys=[team1_id])

    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2 = db.relationship('Team', foreign_keys=[team2_id])

    team2_attacker_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    team2_attacker = db.relationship('Player', foreign_keys=[team2_attacker_id])

    team2_defender_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    team2_defender = db.relationship('Player', foreign_keys=[team2_defender_id])

    team1_score = db.Column(db.Integer, nullable=False)
    team2_score = db.Column(db.Integer, nullable=False)

    team1_rating = db.Column(db.Float, nullable=False, default=1000)
    team2_rating = db.Column(db.Float, nullable=False, default=1000)

    rating_change = db.Column(db.Float, nullable=False)

    team1_trueskill = db.Column(db.Float, nullable=False)
    team1_trueskill_sigma = db.Column(db.Float, nullable=False)
    team1_trueskill_change = db.Column(db.Float, nullable=False)
    team2_trueskill = db.Column(db.Float, nullable=False)
    team2_trueskill_sigma = db.Column(db.Float, nullable=False)
    team2_trueskill_change = db.Column(db.Float, nullable=False)

    team1_attacker_trueskill = db.Column(db.Float, nullable=False)
    team1_attacker_trueskill_sigma = db.Column(db.Float, nullable=False)
    team1_attacker_trueskill_change = db.Column(db.Float, nullable=False)
    team1_defender_trueskill = db.Column(db.Float, nullable=False)
    team1_defender_trueskill_sigma = db.Column(db.Float, nullable=False)
    team1_defender_trueskill_change = db.Column(db.Float, nullable=False)
    team2_attacker_trueskill = db.Column(db.Float, nullable=False)
    team2_attacker_trueskill_sigma = db.Column(db.Float, nullable=False)
    team2_attacker_trueskill_change = db.Column(db.Float, nullable=False)
    team2_defender_trueskill = db.Column(db.Float, nullable=False)
    team2_defender_trueskill_sigma = db.Column(db.Float, nullable=False)
    team2_defender_trueskill_change = db.Column(db.Float, nullable=False)

    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, team1_attacker_id, team1_defender_id, team2_attacker_id, team2_defender_id, team1_score,
                 team2_score):
        self.team1_attacker_id = team1_attacker_id
        self.team1_attacker = Player.query.get(team1_attacker_id)
        self.team1_defender_id = team1_defender_id
        self.team1_defender = Player.query.get(team1_defender_id)

        self.team2_attacker_id = team2_attacker_id
        self.team2_attacker = Player.query.get(team2_attacker_id)
        self.team2_defender_id = team2_defender_id
        self.team2_defender = Player.query.get(team2_defender_id)

        self.team1 = Team.find_or_create(team1_attacker_id, team1_defender_id)
        self.team1_id = self.team1.id

        self.team2 = Team.find_or_create(team2_attacker_id, team2_defender_id)
        self.team2_id = self.team2.id

        self.team1_score = team1_score
        self.team2_score = team2_score

        t1_trueskill = Rating(self.team1.trueskill, self.team1.trueskill_sigma)
        t2_trueskill = Rating(self.team2.trueskill, self.team2.trueskill_sigma)

        t1_attacker_trueskill = Rating(self.team1_attacker.trueskill, self.team1_attacker.trueskill_sigma)
        t1_defender_trueskill = Rating(self.team1_defender.trueskill, self.team1_defender.trueskill_sigma)
        t2_attacker_trueskill = Rating(self.team2_attacker.trueskill, self.team2_attacker.trueskill_sigma)
        t2_defender_trueskill = Rating(self.team2_defender.trueskill, self.team2_defender.trueskill_sigma)

        if team1_score > team2_score:
            self.team1.wins += 1
            self.team2.losses += 1
            self.team1_attacker.wins += 1
            self.team1_defender.wins += 1
            self.team2_attacker.losses += 1
            self.team2_defender.losses += 1
        else:
            self.team2.wins += 1
            self.team1.losses += 1
            self.team2_attacker.wins += 1
            self.team2_defender.wins += 1
            self.team1_attacker.losses += 1
            self.team1_defender.losses += 1

        total_score = team1_score + team2_score
        ranks = [team2_score / total_score, team1_score / total_score]
        (new_t1_trueskill), (new_t2_trueskill) = rate([[t1_trueskill], [t2_trueskill]], ranks=ranks)
        (new_t1_atk, new_t1_def), (new_t2_atk, new_t2_def) = rate(
            [[t1_attacker_trueskill, t1_defender_trueskill], [t2_attacker_trueskill, t2_defender_trueskill]],
            ranks=ranks)

        self.team1_trueskill = new_t1_trueskill[0].mu
        self.team1_trueskill_sigma = new_t1_trueskill[0].sigma
        self.team1_trueskill_change = new_t1_trueskill[0].mu - t1_trueskill.mu
        self.team2_trueskill = new_t2_trueskill[0].mu
        self.team2_trueskill_sigma = new_t2_trueskill[0].sigma
        self.team2_trueskill_change = new_t2_trueskill[0].mu - t2_trueskill.mu

        self.team1.trueskill = self.team1_trueskill
        self.team1.trueskill_sigma = self.team1_trueskill_sigma
        self.team2.trueskill = self.team2_trueskill
        self.team2.trueskill_sigma = self.team2_trueskill_sigma

        self.team1_attacker_trueskill = new_t1_atk.mu
        self.team1_attacker_trueskill_sigma = new_t1_atk.sigma
        self.team1_attacker_trueskill_change = new_t1_atk.mu - t1_attacker_trueskill.mu
        self.team1_defender_trueskill = new_t1_def.mu
        self.team1_defender_trueskill_sigma = new_t1_def.sigma
        self.team1_defender_trueskill_change = new_t1_def.mu - t1_defender_trueskill.mu
        self.team2_attacker_trueskill = new_t2_atk.mu
        self.team2_attacker_trueskill_sigma = new_t2_atk.sigma
        self.team2_attacker_trueskill_change = new_t2_atk.mu - t2_attacker_trueskill.mu
        self.team2_defender_trueskill = new_t2_def.mu
        self.team2_defender_trueskill_sigma = new_t2_def.sigma
        self.team2_defender_trueskill_change = new_t2_def.mu - t2_defender_trueskill.mu

        self.team1_attacker.trueskill = self.team1_attacker_trueskill
        self.team1_attacker.trueskill_sigma = self.team1_attacker_trueskill_sigma
        self.team1_defender.trueskill = self.team1_defender_trueskill
        self.team1_defender.trueskill_sigma = self.team1_defender_trueskill_sigma
        self.team2_attacker.trueskill = self.team2_attacker_trueskill
        self.team2_attacker.trueskill_sigma = self.team2_attacker_trueskill_sigma
        self.team2_defender.trueskill = self.team2_defender_trueskill
        self.team2_defender.trueskill_sigma = self.team2_defender_trueskill_sigma

        [p1_change, p2_change] = calculate_elo(team1_score, team2_score, self.team1.rating, self.team2.rating)

        self.rating_change = p1_change

        self.team1_rating = self.team1.rating + p1_change
        self.team2_rating = self.team2.rating + p2_change

        self.team1.rating = self.team1_rating
        self.team2.rating = self.team2_rating


class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'team1_id', 'team2_id', 'team1_defender', 'team1_attacker', 'team2_defender', 'team2_attacker',
                  'team1_score', 'team2_score', 'team1_rating', 'team2_rating', 'rating_change',
                  'team1_trueskill', 'team1_trueskill_sigma', 'team1_trueskill_change',
                  'team2_trueskill', 'team2_trueskill_sigma', 'team2_trueskill_change',
                  'team1_attacker_trueskill', 'team1_attacker_trueskill_sigma', 'team1_attacker_trueskill_change',
                  'team1_defender_trueskill', 'team1_defender_trueskill_sigma', 'team1_defender_trueskill_change',
                  'team2_attacker_trueskill', 'team2_attacker_trueskill_sigma', 'team2_attacker_trueskill_change',
                  'team2_defender_trueskill', 'team2_defender_trueskill_sigma', 'team2_defender_trueskill_change',
                  )

    team1_defender = ma.Nested(basic_player_schema)
    team1_attacker = ma.Nested(basic_player_schema)
    team2_defender = ma.Nested(basic_player_schema)
    team2_attacker = ma.Nested(basic_player_schema)


class GameResultSchema(ma.Schema):
    class Meta:
        fields = ('team1_score', 'team2_score', 'team1_rating_change', 'team2_rating_change')

    team1_score = fields.Integer()
    team2_score = fields.Integer()
    team1_rating_change = fields.Float()
    team2_rating_change = fields.Float()


game_results_schema = GameResultSchema(many=True)


class GamesWhatIfSchema(ma.Schema):
    class Meta:
        fields = ('team1', 'team2', 'scenarios')

    team1 = ma.Nested(team_schema)
    team2 = ma.Nested(team_schema)
    scenarios = ma.Nested(game_results_schema, many=True)


game_schema = GameSchema()
games_schema = GameSchema(many=True)
games_whatif_schema = GamesWhatIfSchema()
