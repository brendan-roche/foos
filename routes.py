from flask import request, jsonify

from models.game import Game, games_schema, game_schema
from models.player import Player, player_schema, players_schema
from models.team import Team, teams_schema, team_schema

from init import db, app


# endpoint to create new player
@app.route("/player", methods=["POST"])
def add_player():
    name = request.json['name']
    short_name = request.json['short_name']

    new_player = Player(name, short_name)

    db.session.add(new_player)
    db.session.commit()

    return player_schema.jsonify(new_player)


# endpoint to show all players
@app.route("/player", methods=["GET"])
def get_players():
    all_players = Player.query.all()
    result = players_schema.dump(all_players)
    return jsonify(result.data)


# endpoint to get player detail by id
@app.route("/player/<id>", methods=["GET"])
def player_detail(id):
    player = Player.query.get(id)
    return player_schema.jsonify(player)


# endpoint to update player
@app.route("/player/<id>", methods=["PUT"])
def player_update(id):
    player = Player.query.get(id)
    name = request.json['name']
    short_name = request.json['short_name']

    player.short_name = short_name
    player.name = name

    db.session.commit()
    return player_schema.jsonify(player)


# endpoint to delete player
@app.route("/player/<id>", methods=["DELETE"])
def player_delete(id):
    player = Player.query.get(id)
    db.session.delete(player)
    db.session.commit()

    return player_schema.jsonify(player)


# endpoint to create new team
@app.route("/team", methods=["POST"])
def add_team():
    player1_id = request.json['player1_id']
    player2_id = request.json['player2_id']

    new_team = Team(player1_id, player2_id)

    db.session.add(new_team)
    db.session.commit()

    return team_schema.jsonify(new_team)


# endpoint to show all teams
@app.route("/team", methods=["GET"])
def get_teams():
    all_teams = Team.query.all()
    result = teams_schema.dump(all_teams)
    return jsonify(result.data)

# endpoint to show all teams
@app.route("/team/ranked", methods=["GET"])
def get_ranked_teams():
    all_teams = Team.query.filter('wins + losses > 10').order_by('rating DESC').all()
    result = teams_schema.dump(all_teams)
    return jsonify(result.data)


# endpoint to get team detail by id
@app.route("/team/<id>", methods=["GET"])
def team_detail(id):
    team = Team.query.get(id)
    return team_schema.jsonify(team)


# endpoint to find a team given the player ids
@app.route("/team/find/<player_id1>/<player_id2>", methods=["GET"])
def team_from_players(player_id1, player_id2):
    team = Team.find_team(player_id1, player_id2)
    return team_schema.jsonify(team)


# endpoint to delete team
@app.route("/team/<id>", methods=["DELETE"])
def team_delete(id):
    team = Team.query.get(id)
    db.session.delete(team)
    db.session.commit()

    return team_schema.jsonify(team)


@app.route("/game", methods=["POST"])
def add_game():
    team1_attacker_id = request.json['team1_attacker_id']
    team1_defender_id = request.json['team1_defender_id']
    team2_attacker_id = request.json['team2_attacker_id']
    team2_defender_id = request.json['team2_defender_id']

    team1_score = request.json['team1_score']
    team2_score = request.json['team2_score']
    rating_change = 0

    new_game = Game(team1_attacker_id, team1_defender_id, team2_attacker_id, team2_defender_id,
                    team1_score, team2_score, rating_change)

    db.session.add(new_game)
    db.session.commit()

    return game_schema.jsonify(new_game)


# endpoint to show all players
@app.route("/game", methods=["GET"])
def get_games():
    all_games = Game.query.all()
    result = games_schema.dump(all_games)
    return jsonify(result.data)


# endpoint to get player detail by id
@app.route("/game/<id>", methods=["GET"])
def game_detail(id):
    game = Game.query.get(id)
    return game_schema.jsonify(game)


# endpoint to update player
@app.route("/game/<id>", methods=["PUT"])
def game_update(id):
    game = Game.query.get(id)
    game.team1_id = request.json['team1_id']
    game.team2_id = request.json['team2_id']
    game.team1_score = request.json['team1_score']
    game.team2_score = request.json['team2_score']
    game.rating_change = request.json['rating_change']

    db.session.commit()
    return game_schema.jsonify(game)


# endpoint to delete player
@app.route("/game/<id>", methods=["DELETE"])
def game_delete(id):
    game = Game.query.get(id)
    db.session.delete(game)
    db.session.commit()

    return game_schema.jsonify(game)
