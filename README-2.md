# Aplicación Web de Premios Nobel

Esta aplicación web muestra información sobre los ganadores de premios Nobel utilizando una base de datos MongoDB, una API Flask y visualizaciones con Chart.js.

## Características

- Base de datos MongoDB para almacenar la información de los premios Nobel
- API Flask para acceder a los datos
- Interfaz de usuario con gráficas interactivas:
  - Gráfica de barras que muestra la cantidad de ganadores por país
  - Lista de 5 ganadores aleatorios cargados mediante AJAX
  - Gráfica adicional que muestra las categorías por país (punto extra)

## Requisitos

- Python 3.8 o superior
- MongoDB
- Paquetes Python listados en `requirements.txt`

## Instalación

1. Clona este repositorio o descarga los archivos

2. Instala las dependencias de Python:
   ```
   pip install -r requirements.txt
   ```

3. Asegúrate de tener MongoDB instalado y funcionando en localhost:27017

4. Asegúrate de que el archivo `short_output_nobel_winners.json` esté en el directorio raíz

## Uso

1. Inicializa la base de datos (opcional, ya que la aplicación lo hace automáticamente):
   ```
   python db_setup.py
   ```

2. Ejecuta la aplicación Flask:
   ```
   python app.py
   ```

3. Abre tu navegador y accede a: http://localhost:5000

## Estructura del Proyecto

- `app.py`: Aplicación principal Flask
- `db_setup.py`: Script para inicializar la base de datos
- `requirements.txt`: Lista de dependencias
- `templates/index.html`: Interfaz de usuario HTML
- `short_output_nobel_winners.json`: Datos de premios Nobel en formato JSON

## API Endpoints

- `/api/random_nobel_winners`: Devuelve 5 ganadores de premio Nobel aleatorios
- `/api/winners_by_country`: Devuelve el conteo de ganadores por país
- `/api/categories_by_country`: Devuelve el desglose de categorías por país

## Tecnologías utilizadas

- Backend:
  - Flask
  - PyMongo
  - MongoDB
- Frontend:
  - HTML5
  - CSS3 (Bootstrap)
  - JavaScript
  - Chart.js para visualizaciones

## Notas

- La aplicación inicializa automáticamente la base de datos si está vacía
- Para mejor visualización, la gráfica de ganadores por país muestra solo los 10 principales países
- La gráfica de categorías por país muestra los 5 principales países
