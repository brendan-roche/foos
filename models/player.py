from datetime import datetime

from init import db, ma

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    short_name = db.Column(db.String(20), unique=True)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name


class PlayerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'short_name')


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
