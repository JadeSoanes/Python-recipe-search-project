import requests
import json

def recipe_search(ingredient):
    app_id = ''
    app_key = ''
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']



