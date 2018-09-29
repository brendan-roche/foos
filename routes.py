from flask import request, jsonify
from sqlalchemy import func, case, and_, or_
from sqlalchemy.sql import label

from models.game import Game, games_schema, game_schema, games_whatif_schema
from models.player import Player, player_schema, players_schema, player_stats_schema
from models.team import Team, teams_schema, team_schema
from elo import calculate_elo

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


# endpoint to find players matching a name
@app.route("/player/find/<name>", methods=["GET"])
def get_players_matching(name):
    all_players = Player.query.filter(or_(Player.name.like('%' + name + '%'), Player.short_name.like('%' + name + '%'))).all()
    result = players_schema.dump(all_players)
    return jsonify(result.data)


# endpoint to get player detail by id
@app.route("/player/<id>", methods=["GET"])
def player_detail(id):
    player = Player.query.get(id)
    return player_schema.jsonify(player)


@app.route("/player/<id>/games", methods=["GET"])
def player_games(id):
    games = Player.query.get(id).games
    result = games_schema.dump(games)
    return jsonify(result.data)


@app.route("/player/<id>/games/lost", methods=["GET"])
def player_lost_games(id):
    games = Player.query.get(id).lost_games
    result = games_schema.dump(games)
    return jsonify(result.data)


@app.route("/player/<id>/games/won", methods=["GET"])
def player_won_games(id):
    games = Player.query.get(id).won_games
    result = games_schema.dump(games)
    return jsonify(result.data)


@app.route("/player/<id>/teams", methods=["GET"])
def player_teams(id):
    teams = Player.query.get(id).teams
    result = teams_schema.dump(teams)
    return jsonify(result.data)


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


# endpoint to show team games
@app.route("/team/<id>/games", methods=["GET"])
def get_team_games(id):
    team = Team.query.get(id)
    team_games = team.games
    result = games_schema.dump(team_games)
    return jsonify(result.data)


# endpoint to show team games won
@app.route("/team/<id>/games/won", methods=["GET"])
def get_team_games_won(id):
    team = Team.query.get(id)
    team_games = team.games_won
    result = games_schema.dump(team_games)
    return jsonify(result.data)


# endpoint to show team games lost
@app.route("/team/<id>/games/lost", methods=["GET"])
def get_team_games_lost(id):
    team = Team.query.get(id)
    team_games = team.games_lost
    result = games_schema.dump(team_games)
    return jsonify(result.data)


@app.route("/team/<id1>/games/<id2>", methods=["GET"])
def get_teams_head_to_head(id1, id2):
    team = Team.query.get(id1)

    team_games = team.games.filter(or_(Game.team1_id == id2, Game.team2_id == id2)).all()
    result = games_schema.dump(team_games)
    return jsonify(result.data)


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

    new_game = Game(
        team1_attacker_id,
        team1_defender_id,
        team2_attacker_id,
        team2_defender_id,
        team1_score,
        team2_score
    )

    db.session.add(new_game)
    db.session.commit()

    return game_schema.jsonify(new_game)


@app.route("/game/whatif", methods=["POST"])
def what_if_game():
    team1_attacker_id = request.json['team1_attacker_id']
    team1_defender_id = request.json['team1_defender_id']
    team2_attacker_id = request.json['team2_attacker_id']
    team2_defender_id = request.json['team2_defender_id']
    t1 = Team.find_or_create(team1_attacker_id, team1_defender_id)
    t2 = Team.find_or_create(team2_attacker_id, team2_defender_id)
    scenarios = []

    for i in range(10):
        [p1_change, p2_change] = calculate_elo(10, i, t1.rating, t2.rating)
        rating_change = round(p1_change, 2)
        scenarios.append(dict(team1_score=10, team2_score=i, team1_rating_change=rating_change,
                              team2_rating_change=-rating_change))

    for i in range(9, -1, -1):
        [p1_change, p2_change] = calculate_elo(i, 10, t1.rating, t2.rating)
        rating_change = round(p1_change, 2)
        scenarios.append(dict(team1_score=i, team2_score=10, team1_rating_change=rating_change,
                              team2_rating_change=-rating_change))

    data = dict(team1=t1, team2=t2, scenarios=scenarios)

    return games_whatif_schema.jsonify(data)


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

    db.session.commit()
    return game_schema.jsonify(game)


# endpoint to delete player
@app.route("/game/<id>", methods=["DELETE"])
def game_delete(id):
    game = Game.query.get(id)
    db.session.delete(game)
    db.session.commit()

    return game_schema.jsonify(game)


@app.route("/player/stats", methods=["GET"])
def get_players_stats():
    stats = db.session.query(
        Player.id,
        Player.name,
        label('wins', func.sum(case([(and_(
            or_(Player.id == Game.team1_attacker_id, Player.id == Game.team1_defender_id),
            Game.team1_score > Game.team2_score), 1), (and_(
            or_(Player.id == Game.team2_attacker_id, Player.id == Game.team2_defender_id),
            Game.team2_score > Game.team1_score), 1)], else_=0))),
        label('losses', func.sum(case([(and_(
            or_(Player.id == Game.team1_attacker_id, Player.id == Game.team1_defender_id),
            Game.team1_score < Game.team2_score), 1), (and_(
            or_(Player.id == Game.team2_attacker_id, Player.id == Game.team2_defender_id),
            Game.team2_score < Game.team1_score), 1)], else_=0))),
        label('attacker', func.sum(
            case([(or_(Player.id == Game.team1_attacker_id, Player.id == Game.team2_attacker_id), 1), ], else_=0))),
        label('attacker_wins', func.sum(case([(or_(
            and_(Player.id == Game.team1_attacker_id, Game.team1_score > Game.team2_score),
            and_(Player.id == Game.team2_attacker_id, Game.team2_score > Game.team1_score)), 1), ],
            else_=0))),
        label('defender', func.sum(
            case([(or_(Player.id == Game.team1_defender_id, Player.id == Game.team2_defender_id), 1), ], else_=0))),
        label('defender_wins', func.sum(case([(or_(
            and_(Player.id == Game.team1_defender_id, Game.team1_score > Game.team2_score),
            and_(Player.id == Game.team2_defender_id, Game.team2_score > Game.team1_score)), 1), ],
            else_=0))),
        label('donuts', func.sum(case([(and_(
            or_(Player.id == Game.team1_attacker_id, Player.id == Game.team1_defender_id), Game.team1_score == 0), 1), (
            and_(or_(
                Player.id == Game.team2_attacker_id,
                Player.id == Game.team2_defender_id),
                Game.team2_score == 0),
            1)],
            else_=0))),
        label('games', func.count(Player.id))
    ) \
        .join(Player.games) \
        .group_by(Player.id) \
        .order_by(Player.name) \
        .all()

    result = player_stats_schema.dump(stats)
    return jsonify(result.data)
