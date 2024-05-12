from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Тест
flowers = [
    {"name": "Роза", "type": "Садовый", "country": "Голландия", "season": "Лето", "sort": "Красная", "price": "$10"},
    {"name": "Тюльпан", "type": "Садовый", "country": "Голландия", "season": "Весна", "sort": "Жёлтый", "price": "$8"},
    {"name": "Орхидея", "type": "Комнатный", "country": "Таиланд", "season": "Весь год", "sort": "Фиолетовая", "price": "$15"}
]

# Тест
suppliers = [
    {"name": "Иванов Иван Иванович", "type": "Оранжерея", "address": "ул. Оранжерейная, 10"},
    {"name": "Петров Петр Петрович", "type": "Тепличное хозяйство", "address": "пр. Тепличный, 5"}
]

# Тест
sellers = [
    {"name": "Сидоров Сидор Сидорович", "address": "ул. Продавцов, 1"},
    {"name": "Николаев Николай Николаевич", "address": "пр. Продаж, 20"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_flowers', methods=['GET'])
def get_flowers():
    return jsonify(flowers)

@app.route('/get_suppliers', methods=['GET'])
def get_suppliers():
    return jsonify(suppliers)

@app.route('/get_sellers', methods=['GET'])
def get_sellers():
    return jsonify(sellers)

@app.route('/filter_by_season/<string:season>', methods=['GET'])
def filter_by_season(season):
    filtered_flowers = [flower for flower in flowers if flower['season'] == season]
    return jsonify(filtered_flowers)

@app.route('/filter_by_country/<string:country>', methods=['GET'])
def filter_by_country(country):
    filtered_flowers = [flower for flower in flowers if flower['country'] == country]
    return jsonify(filtered_flowers)

if __name__ == '__main__':
    app.run(debug=True)
