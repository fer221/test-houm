import requests
import json
import itertools

#¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). Tu respuesta debe ser un número. Recuerda eliminar los duplicados.

if __name__ == '__main__':
    url_egg_grup5 = 'https://pokeapi.co/api/v2/egg-group/5/'
    
    
    response_egg_grup5 = requests.get(url_egg_grup5)
    if response_egg_grup5.status_code == 200:

        response_json_specie5 = response_egg_grup5.json()
    
        specie_pokemon5 = response_json_specie5.get('pokemon_species',[])
    
    list_specie5 = []
    if specie_pokemon5:
        for pokemon_specie in specie_pokemon5:
            name_pokemon = pokemon_specie['name']
            list_specie5.append(name_pokemon)
    
    url_egg_grup6 = 'https://pokeapi.co/api/v2/egg-group/6/'

    response_egg_grup6 = requests.get(url_egg_grup6)
    if response_egg_grup6.status_code == 200:

        response_json_specie6 = response_egg_grup6.json()
    
        specie_pokemon6 = response_json_specie6.get('pokemon_species',[])
    
    list_specie6 = []
    if specie_pokemon6:
        for pokemon_specie6 in specie_pokemon6:
            name_pokemon6 = pokemon_specie6['name']
            list_specie6.append(name_pokemon6)


    unir_dos_listas = list(itertools.chain(list_specie5, list_specie6))
    print(len(unir_dos_listas))
    list_sin_duplicidad = set(unir_dos_listas)
    print("puede procrear con 2 especies de pokemones, HADA y TIERRA, da un total de ", len(list_sin_duplicidad), " pokemones")
    
        








    