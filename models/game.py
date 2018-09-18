from datetime import datetime
from init import db, ma
from models.team import team_schema, Team

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    team1_attacker_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    # team1 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team1_attacker = db.relationship('Player', foreign_keys=[team1_attacker_id])

    team1_defender_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    # team1 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team1_defender = db.relationship('Player', foreign_keys=[team1_defender_id])

    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # team1 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team1 = db.relationship('Team', foreign_keys=[team1_id])

    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # team2 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team2 = db.relationship('Team', foreign_keys=[team2_id])

    team2_attacker_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    # team1 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team2_attacker = db.relationship('Player', foreign_keys=[team2_attacker_id])

    team2_defender_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    # team1 = db.relationship('Team', backref=db.backref('games', lazy=True))
    team2_defender = db.relationship('Player', foreign_keys=[team2_defender_id])

    team1_score = db.Column(db.Integer, nullable=False)
    team2_score = db.Column(db.Integer, nullable=False)

    rating_change = db.Column(db.Float, nullable=False)

    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, team1_attacker_id, team1_defender_id, team2_attacker_id, team2_defender_id, team1_score,
                 team2_score, rating_change):

        self.team1_attacker_id = team1_attacker_id
        self.team1_defender_id = team1_defender_id

        self.team2_attacker_id = team2_attacker_id
        self.team2_defender_id = team2_defender_id

        team1 = Team.find_or_create_team(team1_attacker_id, team1_defender_id)
        self.team1_id = team1.id

        team2 = Team.find_or_create_team(team2_attacker_id, team2_defender_id)
        self.team2_id = team2.id

        self.team1_score = team1_score
        self.team2_score = team2_score
        self.rating_change = rating_change


class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'team1', 'team2', 'team1_score', 'team2_score', 'rating_change', 'created', 'updated')

    team1 = ma.Nested(team_schema)
    team2 = ma.Nested(team_schema)


game_schema = GameSchema()
games_schema = GameSchema(many=True)
