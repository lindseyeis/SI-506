import json
from os import write
import swapi_entities as ent

# Problem 1.0
def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# Problem 1.0
def write_json(filepath, data):
    """
    This function dumps the JSON object in the dictionary `data` into a file on
    `filepath`.
    Parameters:
        filepath (string): The location and filename of the file to store the JSON
        data (dict): The dictionary that contains the JSON representation of the objects.
    Returns:
        None
    """
    with open(filepath, 'w') as file_obj:
            json.dump(data, file_obj)


def main():
    # Problem 1.0
    planet_data = read_json('swapi_planets.json')
    print(planet_data)

    # Problem 2.0 - Problem 4.0
    # Complete in problem_set_10_utils.py
    converted_planet = ent.convert_data(planet_data[3])
    print(converted_planet)
    created_planets = ent.create_planet(converted_planet)
    print(created_planets)
    # Problem 5.2
    global planets
    planets = {}
    for planet in planet_data:
        cleaned_planet = ent.create_planet(planet)
        if cleaned_planet.name == 'Hoth':
            print(cleaned_planet)
        planets[cleaned_planet.name] = cleaned_planet
    print(planets)
    # Problem 6.0
    planets_with_surface_water = []
    planets_inhabited = []
    planets_uninhabited = []
    planets_desert_only = []
    planet_biggest = 0
    planet_smallest = 1000000
    planets_biggest_smallest = {"biggest": [], "smallest": []}
    for key, val in planets.items():
        if val.surface_water is not None and val.has_surface_water():
            planets_with_surface_water.append(val.jsonable())
        if val.population is not None and val.is_populated():
            planets_inhabited.append(val.jsonable())
        elif val.population is not None:
            planets_uninhabited.append(val.jsonable())
        if val.terrain is not None and len(val.terrain) == 1 and val.terrain[0] == 'desert':
            planets_desert_only.append(val.jsonable())
        if val.diameter is not None and val.diameter > planet_biggest:
            planet_biggest = val.diameter
            planets_biggest_smallest['biggest'] = [val.jsonable()]
        elif val.diameter is not None and val.diameter == planet_biggest:
            planets_biggest_smallest['biggest'].append(val.jsonable())
        if val.diameter is not None and val.diameter < planet_smallest:
            planet_smallest = val.diameter
            planets_biggest_smallest['smallest'] = [val.jsonable()]
        elif val.diameter is not None and val.diameter == planet_smallest:
            planets_biggest_smallest['smallest'].append(val.jsonable())
    write_json('stu_planets_with_surface_water.json', planets_with_surface_water)
    write_json('stu_planets_inhabited.json', planets_inhabited)
    write_json('stu_planets_uninhabited.json', planets_uninhabited)
    write_json('stu_planets_desert_only.json', planets_desert_only)
    write_json('stu_planets_biggest_smallest.json', planets_biggest_smallest)
if __name__ == '__main__':
    main()
