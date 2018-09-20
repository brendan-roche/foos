from datetime import datetime

from init import db, ma

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    short_name = db.Column(db.String(20), unique=True)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

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
    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name

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
        # Fields to expose
        fields = ('id', 'name')


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
