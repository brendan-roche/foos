from models.game import Game
from models.player import Player
from models.team import Team
from sqlalchemy import desc, text

def elo_team_ranking():
    elo_ranked = Team.query.filter(text('wins + losses > 10')).order_by(desc(Team.rating)).all()

    print('Elo Team Rankings')
    print('Rank   Team                      Elo    Wins    Losses')
    print('------ --------------------- --------- ------- -------')
    rank = 1
    for t in elo_ranked:
        print(('%4s   %-20s %8.1f %7s %9s' % (rank, t.team_name(), t.rating, t.wins, t.losses)))
        rank += 1

def trueskill_team_ranking():
    trueskill_ranked = Team.query.filter(text('wins + losses > 10')).order_by(desc(Team.trueskill)).all()

    print('Trueskill Team Rankings')
    print('Rank    Team                        Trueskill    Wins  Losses')
    print('------- ----------------------- -------------- ------- ------')
    rank = 1
    for t in trueskill_ranked:
        print(('%4s    %-20s %8.1fμ (%3.1fσ) %7s %7s' % (rank, t.team_name(), t.trueskill, t.trueskill_sigma, t.wins, t.losses)))
        rank += 1

def trueskill_player_ranking():
    trueskill_ranked = Player.query.filter(text('wins + losses > 10')).order_by(desc(Player.trueskill)).all()

    print('Trueskill Player Rankings')
    print('Rank   Player              Trueskill    Wins  Losses')
    print('------ ------------- ---------------- ------- ------')
    rank = 1
    for p in trueskill_ranked:
        print(('%4s   %-10s %10.1fμ (%3.1fσ) %7s %7s' % (rank, p.name, p.trueskill, p.trueskill_sigma, p.wins, p.losses)))
        rank += 1

num_teams = Team.query.count()
num_games = Game.query.count()

print('Total:')
print(('  Teams: %s' % num_teams))
print(('  Games: %s' % num_games))
print()

elo_team_ranking()
print()
trueskill_team_ranking()
print()
trueskill_player_ranking()