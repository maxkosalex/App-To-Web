from flask import Flask, render_template, redirect, request, jsonify, url_for, flash
from data import find_speed_time, find_points, Table_get

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = "1235"

login_manager = LoginManager(app)

USER_CREDENTIALS = {
    "password": "scrypt:32768:8:1$wagTVWwOc3Ki6X5K$46073fde34c0caa8f9cd18d2365969593008dab5e905e2195bd5f43c81215542346b15a4ddff82b82dd723ad48c70825831c10f6f11c4f3e133205507c54c3a2",
    "login": "scrypt:32768:8:1$gMMVCc3uYX92xDqT$46a7ac0c954fdb39969a2da90c34c1fc20911baa9978a19b7c0d4933ee01081a626fcb2463233c02b435977e9b0fb3e21b817040f8a23f46375996690e210c1d"
}


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def Main_page():
    logout_user()
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
@login_required
def Table():

    return render_template("Table.html")


@app.route('/Login')
def Login():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_ = request.form['log']
        password = request.form['psw']
        # Проверка логина и пароля
        if check_password_hash(USER_CREDENTIALS["password"], password) and check_password_hash(USER_CREDENTIALS["login"], login_):
            user = User(user_id=login_)  # Используем login как user_id
            login_user(user)
            return redirect(url_for('Table'))

        flash("Неверная пара логин/пароль", "error")
    return render_template("login.html", title="Авторизация")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/response_points', methods=['POST'])
def response_points():
    data = request.json
    points = str(data.get('points', 0) or 0)
    gender = str(data['gender'])
    style = str(data['style'])
    distance = str(data['distance'])

    distance_value = distance.split()[0]
    distance = float(distance_value)

    gender, style, distance = lable_handler(gender, style, distance)

    speed, time = find_speed_time(gender, style, distance, points)

    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = int(str(int((time % 1) * 1000))[:2])
    if int(distance) < 3000:
        time_formatted = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    else:
        time_formatted = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"[:-1]


    result = {
        "speed": speed,
        "time": time_formatted,
    }

    return jsonify(result)


@app.route('/response_rez', methods=['POST'])
def response_rez():
    data = request.json
    hours = int(data.get('hours', 0) or 0)
    minutes = int(data.get('minutes', 0) or 0)
    seconds = int(data.get('seconds', 0) or 0)
    hundredths = int(data.get('hundredths', 0) or 0)

    gender = data['gender']

    if gender == "Женский":
        gender = 2
    else:
        gender = 1

    style = data['style']

    if style == "Классический":
        style = 2
    else:
        style = 1

    distance = data['distance']

    distance_value = distance.split()[0]
    distance = float(distance_value) * 1000

    # Вычисление времени в секундах
    total_time_in_seconds = hours * 3600 + minutes * 60 + seconds + hundredths / 100.0

    # Вычисление очков и скорости
    points = find_points(gender, style, distance, total_time_in_seconds)
    speed = round(distance / total_time_in_seconds, 2)

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
    app.run(host="147.45.254.51")
    #app.run()
