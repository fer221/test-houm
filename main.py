import requests
import json

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    
    response = requests.get(url)
    if response.status_code == 200:
        
        response_json = response.json()
        result = response_json.get('results',[])

        if result:
            for pokemon_form in result:
                name_pokemon = pokemon_form['name']
                list_name = []
                list_name.append(name_pokemon)
                print(list_name)
                