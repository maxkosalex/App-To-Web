import sqlite3


# Создаем подключение к базе данных (или создаем базу данных, если её нет)
def Create_Table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Создание таблицы Points с использованием PointValue как ключа и значения
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Points (
        PointValue INTEGER PRIMARY KEY
    )
    ''')

    # Создание таблицы Distance с использованием DistanceValue как ключа и значения
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Distance (
        DistanceValue INTEGER PRIMARY KEY
    )
    ''')

    # Создание таблицы Gender
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Gender (
        GenderID INTEGER PRIMARY KEY AUTOINCREMENT,
        GenderName TEXT
    )
    ''')

    # Создание таблицы Style
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Style (
        StyleID INTEGER PRIMARY KEY AUTOINCREMENT,
        StyleName TEXT
    )
    ''')

    # Создание таблицы MeasurementsData
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MeasurementsData (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PointValue INTEGER,
        DistanceValue INTEGER,
        GenderID INTEGER,
        StyleID INTEGER,
        Speed REAL,
        Time REAL,
        FOREIGN KEY (PointValue) REFERENCES Points(PointValue) ON DELETE CASCADE,
        FOREIGN KEY (DistanceValue) REFERENCES Distance(DistanceValue),
        FOREIGN KEY (GenderID) REFERENCES Gender(GenderID),
        FOREIGN KEY (StyleID) REFERENCES Style(StyleID)
    )
    ''')
    conn.commit()
    conn.close()


# Функция для добавления данных в таблицу Points
def add_point(point_value):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Points (PointValue) VALUES (?)
    ''', (point_value,))
    db.commit()
    db.close()


# Функция для добавления данных в таблицу Distance
def add_distance(distance_value):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Distance (DistanceValue) VALUES (?)
    ''', (distance_value,))
    db.commit()
    db.close()


# Функция для добавления данных в таблицу Gender
def add_gender(gender_name):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Gender (GenderName) VALUES (?)
    ''', (gender_name,))
    db.commit()
    db.close()


# Функция для добавления данных в таблицу Style
def add_style(style_name):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Style (StyleName) VALUES (?)
    ''', (style_name,))
    db.commit()
    db.close()


# Функция для добавления данных в таблицу MeasurementsData
def add_measurement_data(point_value, distance_value, gender_id, style_id, value1, value2):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute('''
    INSERT or IGNORE INTO MeasurementsData (PointValue, DistanceValue, GenderID, StyleID, Speed, Time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (point_value, distance_value, gender_id, style_id, value1, value2))
    db.commit()
    db.close()


def find_speed_time(gender, style, distance, points):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    speed, time = cursor.execute("SELECT Speed, Time FROM MeasurementsData WHERE GenderID = ? AND StyleID = ? AND DistanceValue = ? AND PointValue = ?",
                                 (gender, style, distance, points)).fetchall()[0]
    db.close()
    return speed, time


def find_points(gender, style, distance, time):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    points = cursor.execute(
        f"SELECT CASE WHEN ABS(Time - {time}) > 1.0 OR Time = 0 THEN 0 ELSE PointValue END AS PointValue FROM MeasurementsData WHERE DistanceValue = {distance} AND GenderID = {gender} AND StyleID = {style} ORDER BY ABS(Time - {time}) LIMIT 1;").fetchall()[0]

    db.close()

    return points


def Table_get(state, gender, style):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    if state == 1:
        a = cursor.execute(
f"""WITH FormattedTimes AS (
    SELECT 
        PointValue, 
        DistanceValue, 
        printf('%02d:%02d:%02d:%03d',
    FLOOR(Time / 3600),         
    FLOOR((Time % 3600) / 60),      
    FLOOR(Time % 60),                 
    (Time * 1000) % 1000  
        ) AS FormattedTime
    FROM 
        MeasurementsData
    WHERE 
        GenderID = {gender} 
        AND StyleID = {style} 
        AND PointValue
    )
    SELECT 
        PointValue AS Очки,
        MAX(CASE WHEN DistanceValue = 1000 THEN FormattedTime END) AS '1 км',
        MAX(CASE WHEN DistanceValue = 2000 THEN FormattedTime END) AS '2 км',
        MAX(CASE WHEN DistanceValue = 3000 THEN FormattedTime END) AS '3 км',
        MAX(CASE WHEN DistanceValue = 5000 THEN FormattedTime END) AS '5 км',
        MAX(CASE WHEN DistanceValue = 7500 THEN FormattedTime END) AS '7.5 км',
        MAX(CASE WHEN DistanceValue = 10000 THEN FormattedTime END) AS '10 км',
        MAX(CASE WHEN DistanceValue = 15000 THEN FormattedTime END) AS '15 км',
        MAX(CASE WHEN DistanceValue = 20000 THEN FormattedTime END) AS '20 км',
        MAX(CASE WHEN DistanceValue = 30000 THEN FormattedTime END) AS '30 км',
        MAX(CASE WHEN DistanceValue = 50000 THEN FormattedTime END) AS '50 км',
        MAX(CASE WHEN DistanceValue = 70000 THEN FormattedTime END) AS '70 км'
    FROM 
        FormattedTimes
    GROUP BY 
        PointValue
    ORDER BY 
        PointValue""").fetchall()
        a = [
            [
                # Для первого элемента ничего не меняем
                item if idx == 0
                # Для элементов с индексами 1 и 2 оставляем 2 знака после двоеточия
                else item.rsplit(':', 1)[0] + '.' + item.rsplit(':', 1)[1][:2] if idx < 3 and ':' in item
                # Для остальных оставляем только 1 знак после точки
                else item.rsplit(':', 1)[0] + '.' + item.rsplit(':', 1)[1][0] if ':' in item
                # Если двоеточие не найдено, ничего не меняем
                else item
                for idx, item in enumerate(sublist)
            ]
            for sublist in a
        ]

    else:
        a = cursor.execute(
            f"SELECT PointValue AS Очки, MAX(CASE WHEN DistanceValue = 1000 THEN Speed END) AS '1км', MAX(CASE WHEN DistanceValue = 2000 THEN Speed END) AS '2км',MAX(CASE WHEN DistanceValue = 3000 THEN Speed END) AS '3км',MAX(CASE WHEN DistanceValue = 5000 THEN Speed END) AS '5 км',MAX(CASE WHEN DistanceValue = 7500 THEN Speed END) AS '7.5 км',MAX(CASE WHEN DistanceValue = 10000 THEN Speed END) AS '10 км',MAX(CASE WHEN DistanceValue = 15000 THEN Speed END) AS '15 км',MAX(CASE WHEN DistanceValue = 20000 THEN Speed END) AS '20 км',MAX(CASE WHEN DistanceValue = 30000 THEN Speed END) AS '30 км',MAX(CASE WHEN DistanceValue = 50000 THEN Speed END) AS '50 км',MAX(CASE WHEN DistanceValue = 70000 THEN Speed END) AS '70 км' FROM MeasurementsData WHERE GenderID = {gender} AND StyleID = {style} AND PointValue GROUP BY PointValue ORDER BY PointValue").fetchall()
        a = [tuple(map(lambda x: str(x).replace('.', ',') if isinstance(x, float) else x, sublist)) for sublist in a]

    db.close()
    return a
