from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

flowers = load_data('flowers.json')
suppliers = load_data('suppliers.json')
sellers = load_data('sellers.json')

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

@app.route('/add_seller', methods=['POST'])
def add_seller():
    data = request.json
    sellers.append(data)
    save_data(sellers, 'sellers.json')
    return jsonify(sellers)

if __name__ == '__main__':
    app.run(debug=True)
