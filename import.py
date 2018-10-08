import sys
import argparse

from games import doubles
from models.game import Game
from models.player import Player

from init import db

def team(p1, p2):
    if p1 < p2:
        return '%s / %s' % (p1, p2)

    return '%s / %s' % (p2, p1)


def resetDb():
    db.drop_all()
    db.create_all()

parser = argparse.ArgumentParser(description='Import games into db.')
parser.add_argument('--reset', dest='resetDb', action='store_true', help='reset db (default: false)')
parser.set_defaults(resetDb=False)

args = parser.parse_args()

# resets database!
if (args.resetDb):
    resetDb()


games = []
individual_players = set()
for parts in doubles:
    try:
        games.append({
            'p1_players': [parts[0], parts[1]],
            'p1': team(parts[0], parts[1]),
            'p1score': float(parts[2]),
            'p2': team(parts[3], parts[4]),
            'p2_players': [parts[3], parts[4]],
            'p2score': float(parts[5]),
        })

        individual_players.add(parts[0])
        individual_players.add(parts[1])
        individual_players.add(parts[3])
        individual_players.add(parts[4])
    except:
        print("Failed: %s", parts)
        sys.exit(1)

print("Individual games:\n")
game_number = 1
for g in games:

    game_number += 1

    t1_p1 = Player.find_or_create(g['p1_players'][0])
    t1_p2 = Player.find_or_create(g['p1_players'][1])
    t2_p1 = Player.find_or_create(g['p2_players'][0])
    t2_p2 = Player.find_or_create(g['p2_players'][1])

    game = Game(t1_p1.id, t1_p2.id, t2_p1.id, t2_p2.id, g['p1score'], g['p2score'])

    print(
        "%3d. %020s   %2.0f: %11.6f -> %11.6f (%+.6f) | %11.6f -> %11.6f (%+.6f, %11.6fσ)\n     %20s   %2.0f: %11.6f -> %11.6f (%+.6f) | %11.6f -> %11.6f (%+.6f, %11.6fσ)\n" % (
            game_number,
            g['p1'],
            game.team1_score,
            game.team1_rating - game.rating_change,
            game.team1_rating,
            game.rating_change,
            game.team1_trueskill - game.team1_trueskill_change,
            game.team1_trueskill,
            game.team1_trueskill_change,
            game.team1_trueskill_sigma,
            g['p2'],
            game.team2_score,
            game.team2_rating + game.rating_change,
            game.team2_rating,
            -game.rating_change,
            game.team2_trueskill - game.team2_trueskill_change,
            game.team2_trueskill,
            game.team2_trueskill_change,
            game.team2_trueskill_sigma,
        ))

    db.session.add(game)

db.session.commit()
