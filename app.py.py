from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# Conexión a MongoDB
def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['nobel_db']
    return db

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# API para obtener 5 premios Nobel aleatorios
@app.route('/api/random_nobel_winners', methods=['GET'])
def random_nobel_winners():
    db = get_db()
    winners = list(db.nobel_winners.aggregate([{"$sample": {"size": 5}}]))
    
    # Convertir ObjectId a string para que sea serializable
    for winner in winners:
        winner['_id'] = str(winner['_id'])
    
    return jsonify(winners)

# API para obtener el conteo de ganadores por país
@app.route('/api/winners_by_country', methods=['GET'])
def winners_by_country():
    db = get_db()
    result = db.nobel_winners.aggregate([
        {"$match": {"country": {"$ne": ""}}},
        {"$group": {"_id": "$country", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    
    countries = []
    counts = []
    
    for r in result:
        countries.append(r['_id'])
        counts.append(r['count'])
    
    return jsonify({
        'countries': countries,
        'counts': counts
    })

# API para obtener categorías por país (punto extra)
@app.route('/api/categories_by_country', methods=['GET'])
def categories_by_country():
    db = get_db()
    result = db.nobel_winners.aggregate([
        {"$match": {"country": {"$ne": ""}}},
        {"$group": {
            "_id": {"country": "$country", "category": "$category"},
            "count": {"$sum": 1}
        }},
        {"$sort": {"_id.country": 1, "_id.category": 1}}
    ])
    
    data = {}
    for r in result:
        country = r['_id']['country']
        category = r['_id']['category']
        count = r['count']
        
        if country not in data:
            data[country] = {}
        
        data[country][category] = count
    
    return jsonify(data)

# Función para inicializar la base de datos con los datos del JSON
def init_db():
    db = get_db()
    
    # Verificar si la colección ya tiene datos
    if db.nobel_winners.count_documents({}) == 0:
        # Cargar el archivo JSON
        with open('short_output_nobel_winners.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Insertar los datos en la colección
        db.nobel_winners.insert_many(data)
        print("Base de datos inicializada con éxito.")
    else:
        print("La base de datos ya tiene datos.")

if __name__ == '__main__':
    # Inicializar la base de datos antes de ejecutar la aplicación
    init_db()
    app.run(debug=True)
