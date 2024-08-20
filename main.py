from flask import Flask, render_template, redirect, request, jsonify
from data import find_speed_time, find_points, Table_get
app = Flask(__name__)

app.secret_key = "1235"


@app.route('/')
def Main_page():
    return render_template("main.html")


@app.route('/Scoring-points')
def Scoring_points():
    return render_template("Scoring_points_main.html")


@app.route('/Scoring-points/rez')
def Scoring_points_rez():
    return render_template("Scoring_points_rez.html")


@app.route('/Scoring-points/points')
def Scoring_points_points():
    return render_template("Scoring_points_point.html")


@app.route('/Table')
def Table():

    return render_template("Table.html")


@app.route('/response_points', methods=['POST'])
def response_points():
    data = request.json
    # Обработка данных, например, расчет времени в секундах
    points = str(data.get('points', 0) or 0)

    gender = str(data['gender'])
    style = str(data['style'])
    distance = str(data['distance'])

    gender, style, distance = lable_handler(gender, style, distance)

    speed, time = find_speed_time(gender, style, distance, points)

    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = int((time % 1) * 1000)

    time_formatted = f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}"

    result = {
        "speed": speed,
        "time": time_formatted,
    }

    return jsonify(result)


@app.route('/response_rez', methods=['POST'])
def response_rez():
    data = request.json

    # Получение данных
    hours = int(data.get('hours', 0) or 0)
    minutes = int(data.get('minutes', 0) or 0)
    seconds = int(data.get('seconds', 0) or 0)
    hundredths = int(data.get('hundredths', 0) or 0)

    gender = str(data['gender'])
    style = str(data['style'])
    distance = str(data['distance'])

    gender, style, distance = lable_handler(gender, style, distance)

    # Вычисление общего времени в секундах
    total_time_in_seconds = hours * 3600 + minutes * 60 + seconds + hundredths / 100.0

    # Вычисление количества очков и скорости
    points = find_points(gender, style, distance, total_time_in_seconds)
    speed = round(distance / total_time_in_seconds, 2)
    # Формирование результата
    result = {
        'average_speed': speed,
        'points': points
    }

    return jsonify(result)


def lable_handler(gender, style, distance):
    if gender == "Женский":
        handler_gender = 2
    else:
        handler_gender = 1

    if style == "Классический":
        handler_style = 2
    else:
        handler_style = 1

    distance = ''.join(filter(lambda x: x.isdigit() or x in ['.'], distance))

    handler_distance = int(float(distance) * 1000)

    return handler_gender, handler_style, handler_distance

@app.route('/get_data')
def get_data():
    state = int(request.args.get('state', 1))
    gender = int(request.args.get('gender', 1))
    style = int(request.args.get('style', 1))

    data = Table_get(state, gender, style)

    return jsonify(data)




if __name__ == "__main__":
    # app.run(host="77.232.128.6")
    app.run()
