from datetime import datetime

from trueskill import Rating

from init import db, ma


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    short_name = db.Column(db.String(20), unique=True)

    wins = db.Column(db.Integer, nullable=False, default=0)
    losses = db.Column(db.Integer, nullable=False, default=0)

    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    trueskill = db.Column(db.Float, nullable=False, default=25)
    trueskill_sigma = db.Column(db.Float, nullable=False)

    games = db.relationship('Game',
                            primaryjoin='or_('
                                        'Player.id == Game.team1_attacker_id,'
                                        'Player.id == Game.team1_defender_id,'
                                        'Player.id == Game.team2_attacker_id,'
                                        'Player.id == Game.team2_defender_id)',
                            lazy=True)

    lost_games = db.relationship('Game',
                            primaryjoin='or_('
                                        'and_(or_('
                                        'Player.id == Game.team1_attacker_id,'
                                        'Player.id == Game.team1_defender_id), Game.team1_score < Game.team2_score),'
                                        'and_(or_('
                                        'Player.id == Game.team2_attacker_id,'
                                        'Player.id == Game.team2_defender_id), Game.team2_score < Game.team1_score)'
                                        ')',
                            lazy=True)

    won_games = db.relationship('Game',
                            primaryjoin='or_('
                                        'and_(or_('
                                        'Player.id == Game.team1_attacker_id,'
                                        'Player.id == Game.team1_defender_id), Game.team1_score > Game.team2_score),'
                                        'and_(or_('
                                        'Player.id == Game.team2_attacker_id,'
                                        'Player.id == Game.team2_defender_id), Game.team2_score > Game.team1_score)'
                                        ')',
                            lazy=True)

    teams = db.relationship('Team',
                            primaryjoin='or_('
                                        'Player.id == Team.player1_id,'
                                        'Player.id == Team.player2_id)',
                            lazy=True)

    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name
        self.wins = 0
        self.losses = 0
        trueskill = Rating()
        self.trueskill = trueskill.mu
        self.trueskill_sigma = trueskill.sigma

    @staticmethod
    def find_player(name):
        return Player.query.filter(Player.name == name).first()

    @staticmethod
    def find_or_create(name):
        player = Player.find_player(name)
        if player:
            return player

        new_player = Player(name, name)
        db.session.add(new_player)
        db.session.commit()

        return new_player


class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'wins', 'losses', 'trueskill', 'trueskill_sigma')

class PlayerStatsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'wins', 'losses', 'attacker', 'attacker_wins', 'defender', 'defender_wins', 'donuts', 'games')


player_schema = PlayerSchema()
basic_player_schema = PlayerSchema(only=('id', 'name'))
players_schema = PlayerSchema(many=True)
player_stats_schema = PlayerStatsSchema(many=True)
