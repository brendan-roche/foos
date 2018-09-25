from datetime import datetime

from elo import calculate_elo
from init import db, ma
from models.player import player_schema
from models.team import Team


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

    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, team1_attacker_id, team1_defender_id, team2_attacker_id, team2_defender_id, team1_score,
                 team2_score):
        self.team1_attacker_id = team1_attacker_id
        self.team1_defender_id = team1_defender_id

        self.team2_attacker_id = team2_attacker_id
        self.team2_defender_id = team2_defender_id

        team1 = Team.find_or_create(team1_attacker_id, team1_defender_id)
        self.team1_id = team1.id

        team2 = Team.find_or_create(team2_attacker_id, team2_defender_id)
        self.team2_id = team2.id

        self.team1_score = team1_score
        self.team2_score = team2_score

        [p1_change, p2_change] = calculate_elo(team1_score, team2_score, team1.rating, team2.rating)

        self.rating_change = p1_change

        self.team1_rating = team1.rating + p1_change
        self.team2_rating = team2.rating + p2_change


class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'team1_id', 'team2_id', 'team1_defender', 'team1_attacker', 'team2_defender', 'team2_attacker',
                  'team1_score', 'team2_score', 'team1_rating', 'team2_rating', 'rating_change')

    team1_defender = ma.Nested(player_schema)
    team1_attacker = ma.Nested(player_schema)
    team2_defender = ma.Nested(player_schema)
    team2_attacker = ma.Nested(player_schema)

game_schema = GameSchema()
games_schema = GameSchema(many=True)
