from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# initialize Flask application

app = Flask(__name__) 

# function takes an ingredient and optional health param
# retrieves id & key  and builds URL for Edamam API request
# if health params are provided they are added to the URL
# Then parses the JSON response and returns the list of recipes          

def recipe_search(ingredient, health=None):
    app_id = os.getenv('APP_ID')
    app_key = os.getenv('APP_KEY')

    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

    if health:
        health_query = '&'.join([f'health={h}' for h in health])
        url += f'&{health_query}'

    result = requests.get(url)
    data = result.json()
    return data['hits']

     # defines route that accepts POST requests
     # Extracts JSON data from request
     # Retrieves ingredient and health params from request data
     # returns the search results as a JSON response

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    ingredient = data.get('ingredient')
    health = data.get('health')
    results = recipe_search(ingredient, health)
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
