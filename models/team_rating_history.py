from datetime import datetime

from init import db, ma

class TeamRatingHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team = db.relationship('Team', backref=db.backref('rating_history', lazy=True))

    rating = db.Column(db.Float, nullable=False)
    rating_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, team_id, rating, rating_date):
        self.team_id = team_id
        self.rating = rating
        self.rating_date = rating_date


class TeamRatingHistorySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('team', 'rating', 'rating_date')


team_rating_history_schema = TeamRatingHistorySchema(many=True)
