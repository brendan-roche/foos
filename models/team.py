from datetime import datetime
from operator import and_, or_

from init import db, ma
from models.player import player_schema

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player1 = db.relationship('Player', foreign_keys=[player1_id])

    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player2 = db.relationship('Player', foreign_keys=[player2_id])

    games = db.relationship(
        'Game',
        primaryjoin='or_(Team.id == Game.team1_id, Team.id == Game.team2_id)',
        lazy='dynamic'
    )

    games_won = db.relationship(
        'Game',
        primaryjoin='or_(and_(Team.id == Game.team1_id, Game.team1_score > Game.team2_score), and_(Team.id == Game.team2_id, Game.team2_score > Game.team1_score))',
        lazy='dynamic'
    )

    games_lost = db.relationship(
        'Game',
        primaryjoin='or_(and_(Team.id == Game.team1_id, Game.team1_score < Game.team2_score), and_(Team.id == Game.team2_id, Game.team2_score < Game.team1_score))',
        lazy='dynamic'
    )

    rating = db.Column(db.Integer, nullable=False, default=1000)
    wins = db.Column(db.Integer, nullable=False, default=0)
    losses = db.Column(db.Integer, nullable=False, default=0)

    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, player1_id, player2_id):
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.rating = 1000
        self.wins = 0
        self.losses = 0

    @staticmethod
    def find_team(player1_id, player2_id):
        return Team.query.filter(or_(and_(Team.player1_id == player1_id, Team.player2_id == player2_id),
                                     and_(Team.player2_id == player1_id, Team.player1_id == player2_id))).first()

    @staticmethod
    def find_or_create(player1_id, player2_id):
        team = Team.find_team(player1_id, player2_id)
        if team:
            return team

        return Team(player1_id, player2_id)

class TeamSchema(ma.Schema):
    class Meta:
        fields = ('id', 'player1', 'player2', 'rating', 'wins', 'losses')

    player1 = ma.Nested(player_schema)
    player2 = ma.Nested(player_schema)


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
