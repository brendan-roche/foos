from models.game import Game
from models.team import Team
from sqlalchemy import desc, text

num_teams = Team.query.count()
num_games = Game.query.count()
ranked_teams = Team.query.filter(text('wins + losses > 10')).order_by(desc(Team.rating)).all()

print('Total:')
print(('  Teams: %s' % num_teams))
print(('  Games: %s' % num_games))
print()

print('Rank         Team          Elo       Wins    Losses')
rank = 1
for t in ranked_teams:
    print(('%4s %20s %7.1f %5s %7s' % (rank, t.team_name(), t.rating, t.wins, t.losses)))
    rank += 1
