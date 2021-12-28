# Problem 2.0
class Planet:
    """Representation of a planet.
    Attributes:
        url (str): identifier/locator
        name (str): planet name
        rotation_period (int): rotation period
        orbital_period (int): orbital period
        diameter (int): diameter of the planet
        climate (list): climate type(s) found on planet
        gravity (dict): gravity level
        terrain (list): terrain type(s) found on planet
        surface_water (float): surface water
        population (int): population size
    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    # Problem 2.1
    def __init__(self, url, name, rotation_period=None, orbital_period=None, diameter=None, climate=None, gravity=None, terrain=None, surface_water=None, population=None):
        """Initialize a Planet instance."""
        self.url = url
        self.name = name
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population


    # Problem 2.2
    def __str__(self):
        """Return a string representation of the object."""
        return self.name

    # Problem 2.3
    def has_surface_water(self):
        """Return a boolean representation of whether the planet has surface water."""
        if self.surface_water > 0:
            return True
        else:
            return False

    # Problem 2.5
    def is_populated(self):
        """Return a boolean representation of whether the planet has population."""
        if self.population > 0:
            return True
        else:
            return False

    # Problem 2.6
    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use the order specified in the Docstring above.
        Use a dictionary literal rather than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        return {
            'url': self.url,
            'name': self.name,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'diameter': self.diameter,
            'climate': self.climate,
            'gravity': self.gravity,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'population': self.population
        }

# Problem 3.0
def convert_data(planet):
    """Convert string values of a dictionary to the appropriate type whenever possible.
    Remember to set the value to None when the string is "unknown".

    Type conversions:
        rotation_period (str->int)
        orbital_period (str->int)
        diameter (str->int)
        climate (str->list) e.g. ["hot", "humid"]
        gravity (str->dict) e.g. {"measure": 0.75, "unit"; "standard"}
        terrain (str->list) e.g. ["fungus", "forests"]
        surface_water (str->float)
        population (str->int)

    Parameters:
        dict: dictionary of a planet
    Returns:
        dict: dictionary of a planet with its values converted
    """

    for key, val in planet.items():
        if isinstance(val, str):
            if val.strip().lower() == 'unknown':
                planet[key] = None
            elif key == 'rotation_period':
                planet[key] = int(val)
            elif key == 'orbital_period':
                planet[key] = int(val)
            elif key == 'diameter':
                planet[key] = int(val)
            elif key == 'climate':
                planet[key] = val.split(', ')
            elif key == 'gravity':
                split_vals = val.split(' ')
                if len(split_vals) == 1:
                    split_vals.append('standard')
                planet[key] = {'measure': float(split_vals[0]), 'unit': split_vals[1]}
            elif key == 'terrain':
                planet[key] = val.split(', ')
            elif key == 'surface_water':
                planet[key] = float(val)
            elif key == 'population':
                planet[key] = int(val)

    return planet

# Problem 4.0
def create_planet(planet):
    """Creates a < Planet > instance from dictionary data. You must call the convert_data() function
    to clean up the planet dictionary first, then assign the dictionary to the instance.

    Parameters:
        planet (dict): planet as a dictionary
    Returns:
        Planet: new < Planet > instance
    """

    cleaned_planet = convert_data(planet)
    new_planet = Planet(cleaned_planet['url'], cleaned_planet['name'], cleaned_planet['rotation_period'], cleaned_planet['orbital_period'], cleaned_planet['diameter'], cleaned_planet['climate'], cleaned_planet['gravity'], cleaned_planet['terrain'], cleaned_planet['surface_water'], cleaned_planet['population'])
    return new_planet
