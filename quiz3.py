import requests
import json
import os
from pathlib import Path

#Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.

if __name__ == '__main__':
    url_type_pokemon = 'https://pokeapi.co/api/v2/type/2/'
    
    requests_url = requests.get(url_type_pokemon)
    if requests_url.status_code == 200:

        json_type = requests_url.json()
        pokemon = json_type.get('pokemon', [])

        list_url_id = []
        for i in pokemon:
            id_pokemon = i['pokemon']['url']
            list_url_id.append(id_pokemon)
        
        list_id = []
        for x in list_url_id:
            split_list = x.split("/")
            y = split_list[6]
            list_id.append(y)

        id_o = []
        for id_i in list_id:
            convert = int(id_i)
            if convert <= 151:
                id_o.append(id_i)

    list_weight_pokemon = []
    for x in id_o:
        position_id = x

        with open(r"C:/Users/Fer/Desktop/test-houm/pokemon_weight/"+position_id+".json") as f:
            f_read = f.read()
            convert_dic = json.loads(f_read)
            weight_pokemon = convert_dic['weight'] 
            list_weight_pokemon.append(weight_pokemon)

    list_menor = []
    for acendente in list_weight_pokemon:
        if acendente < 1234:
            list_menor.append(acendente)
            list_menor.sort(reverse=True)
    print("el peso maximo y minimo de los pokemones tipo fighting de la primera generacion son: ", list_menor)
    
    
    

    


     
