from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

individual_goal = {
    'A' : 5,
    'B' : 10,
    'C' : 15,
    'Cuauh' : 20
}


def sumGoals(team,teams):
    goals = 0
    goals_by_level = 0
    for player in teams[team]:
        goals = goals + player['goles']
        goals_by_level = goals_by_level + individual_goal[player['nivel']]
    return  goals / goals_by_level

def results(players):
    for player in players:
        player['goles_minimos']=individual_goal[player['nivel']]
        player.pop('nivel')
    return players

@app.route('/', methods=['get','POST'])
def hello_world():
    data = request.get_json()
    teams = {}
    print(data)
    try:
            for player in data:
                    teams.setdefault(player['equipo'], []).append(player)
                    percent = player['goles']/individual_goal[player['nivel']]
                    # print(percent*player['sueldo'])
                print(teams)

                players = []
                for team in teams:
                    print(team)
                    total_percent_team = sumGoals(team,teams)
                    print(total_percent_team)
                    for player in teams[team]:
                        print(player)
                        percent_player = player['goles'] / individual_goal[player['nivel']]
                        percent_final = (percent_player + total_percent_team) / 2
                        print(f'porcentaje: { percent_final}')
                        salary = player['sueldo'] + (player['bono'] * percent_final)
                        print(f'Salario completo: {int(salary)}')
                        player['sueldo_completo'] = int(salary)
                        players.append(player)
                return jsonify(results(players))


if __name__ == '__main__':
    app.run(debug=True, port=9000)
