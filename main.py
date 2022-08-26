import requests
import json

# function connecting to api

def recipe_search(ingredient):
    app_id = '2ce04194'
    app_key = '884c0755cdc7675a9bc6a788c0f4dcd1'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

# function asking user to input an ingredient

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
# function to print the recipe link, uri and calories each time quickly
    def output():
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['calories'])
        print()
# for loop to categorise recipe into low, moderate or high calorie
    for result in results:
        recipe = result['recipe']
        if recipe['calories'] <= 500:
            print('Low calorie recipe found')
            output()
        elif recipe['calories'] <= 1000:
            print('Moderate calorie recipe found')
            output()
        else:
            print('High calorie recipe found')
            output()

run()



