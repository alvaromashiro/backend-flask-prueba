from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
app = Flask(__name__)

CORS(app)

individual_goal = {
    'A': 5,
    'B': 10,
    'C': 15,
    'Cuauh': 20
}


def sumGoals(team, teams):
    goals = 0
    goals_by_level = 0
    for player in teams[team]:
        goals =+ player['goles']
        goals_by_level = goals_by_level + individual_goal[player['nivel']]
    return goals / goals_by_level


def results(players):
    for player in players:
        player['goles_minimos'] = individual_goal[player['nivel']]
        player.pop('nivel')
    return players


def calculate_salary(salary, bonus):
    return int(salary + bonus)


def calculate_bonus(player, percent_team):
    percent_player = player['goles'] / individual_goal[player['nivel']]
    percent_final = (percent_player + percent_team) / 2
    return player['bono'] * percent_final


@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    if data is None:
        return {'message': 'players is required'}, 406
    teams = {}
    try:
        for player in data['players']:
            teams.setdefault(player['equipo'], []).append(player)
            players = []
            for team in teams:
                total_percent_team = sumGoals(team, teams)
                for player in teams[team]:
                    bonus = calculate_bonus(player, total_percent_team)
                    player['sueldo_completo'] = \
                        calculate_salary(player['sueldo'], bonus)
                    players.append(player)
        return jsonify(results(players))
    except:
        return {"message": "Not acceptable data, please verify request data"},
    406


if __name__ == '__main__':
    app.run(debug=True, port=9000)
