import requests
import json
from collections import defaultdict

#Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. Tu respuesta debe ser un número.

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    
    response = requests.get(url)
    if response.status_code == 200:
        
        response_json = response.json()
        result = response_json.get('results',[])

        list_name = []
        if result:
            for pokemon_form in result:
                name_pokemon = pokemon_form['name']
                list_name.append(name_pokemon)

        list_pokemon_at = []
        count = 0
        for letras in list_name:
            if "at" in letras and letras.count('a') == 2:
                count += 1
                print(letras)
        print("la cantidad de pokemones que contienen AT y tienen 2 A:", count)




    







#Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.
                
            


                    
                    
                
                
                    
                