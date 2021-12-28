import json, requests, copy

from requests.models import Response


# Problem 01
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# Problem 02
def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


# Problem 03
def delete_items(dictionary, key_list):
    dict_copy = copy.deepcopy(dictionary)
    for key in key_list:
        if key in dict_copy.keys():
            del(dict_copy[key])

    return dict_copy

# Problem 04
def get_homeworld(person, key_list=None):
    homeworld_url = person['homeworld']
    homeworld = get_swapi_resource(homeworld_url)
    if key_list is not None:
        result_dict = {}
        for key in key_list:
            result_dict.update({key: homeworld[key]})
        return result_dict
    else:
        return homeworld

def get_species(person, key_list=None):
    if person['species'] is None or len(person['species']) < 1:
        return {}
    species_url = person['species'][0]
    species = get_swapi_resource(species_url)
    if key_list is not None and len(key_list) > 0:
        result_dict = {}
        for key in key_list:
            result_dict.update({key: species[key]})
        return result_dict
    else:
        return species
# Problem 05
def clean_person_dictionary(person, delete_list, home_list=None, species_list=None):
    deleting = delete_items(person, delete_list)
    homeworlds = get_homeworld(person, home_list)
    deleting.update({'homeworld': homeworlds})
    species = get_species(person, species_list)
    deleting.update({'species': species})
    return deleting
# Problem 06
def board_ship(ship, passengers):
    copy_ship = copy.deepcopy(ship)
    passengers_ordered = []
    for i in range(1, len(passengers)+1):
        for person in passengers:
            if person['boarding_order'] == i:
                passengers_ordered.append(person)
                continue
    copy_ship.update({'passengers': passengers_ordered})
    return copy_ship

# Problem 07
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

def main():
    """Program entry point."""

    # Problem 01
    passengers = read_json('./passengers.json')['passengers']

    print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = 'https://swapi.py4e.com/api/'
    falcon_params = {'search': 'falcon'}
    falcon = get_swapi_resource(f'{base_url}/starships/', falcon_params)['results'][0]

    print(f'\nProblem 02:\n{falcon}')

    # Problem 03
    falcon_keys_delete = list(falcon.keys())[-5:-1]
    falcon_updated = delete_items(falcon, falcon_keys_delete)
    print(f'\nProblem 03:\n{falcon_updated}')

    # Problem 04

    bail_data = get_swapi_resource(f"{base_url}/people/", {'search': 'bail organa'})['results'][0]
    print(bail_data)
    bail_home = get_homeworld(bail_data)
    home_keys_keep = list(bail_home.keys())[0:9]
    print(home_keys_keep)
    bail_species = get_species(bail_data)
    print(bail_species)

    # Problem 05
    delete = ['films', 'vehicles', 'starships', 'created', 'edited', 'url']
    for person in passengers:
        passenger_info = get_swapi_resource(f"{base_url}/people/", {'search': person['name']})['results'][0]
        passenger_delete = clean_person_dictionary(passenger_info, delete, home_keys_keep, ['name'])
        person.update(passenger_delete)
    print(passengers)

    # Problem 06
    all_aboard = board_ship(falcon_updated, passengers)
    print(all_aboard)

    # Problem 07
    leaving_tatooine = 'hyperspace_jump.json'
    write_json(data=all_aboard, filepath=leaving_tatooine)


if __name__ == '__main__':
    main()
