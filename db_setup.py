from pymongo import MongoClient
import json

def setup_database():
    # Conectar a MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['nobel_db']
    
    # Crear colección para los ganadores de premios Nobel
    if 'nobel_winners' in db.list_collection_names():
        # Eliminar la colección si ya existe
        db.nobel_winners.drop()
    
    # Cargar datos desde el archivo JSON
    try:
        with open('short_output_nobel_winners.json', 'r', encoding='utf-8') as file:
            nobel_data = json.load(file)
            
        # Insertar datos en la colección
        db.nobel_winners.insert_many(nobel_data)
        print(f"Se han insertado {len(nobel_data)} documentos en la base de datos.")
        
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

if __name__ == "__main__":
    setup_database()
