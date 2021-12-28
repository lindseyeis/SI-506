import sw_utils as utl


class Crew:
    """Represents a Starship or Vehicle crew.

    Attributes:
        Accepts a dictionary of Person and/or Droid crew members and assigns each key-value pair
        to the new `Crew` instance's `__dict__` dictionary of writable attributes.

        < role > (Person | Droid): Person or Droid instance identified by crew role (e.g., pilot)

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, crew_members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to create each instance variable and assign the value. The
        dictionary key (e.g., "pilot") serves as the instance variable name to which the
        accompanying < Person | Droid > instance is assigned as the value, e.g.,
        {< role >: < Person | Droid >, ...}

        Parameters:
            crew_members (dict): crew members dictionary

        Returns:
            None
        """

        for key, val in crew_members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person | Droid > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over a < Crew > instance's
        __dict__ items and assigns new key-value pairs to an empty dictionary using the existing
        key as the new key and a dictionary representation of the < Person > or < Droid > instance
        as the value. After the loop terminates the new dictionary is returned to the caller.
        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying
        and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person or droid object

        return crew


class Droid:
    """Represents a mechanical being that possesses artificial intelligence.

    Attributes:
       Required
            url (str): identifier/locator (required)
            name (str): droid name (required)
            model (str): droid model (required)
        Optional
            manufacturer (str): creator
            create_year (str): year of manufacture
            height_m (float): height in meters
            mass_kg (float): mass in kilograms
            equipment (list): equipment carried, if any

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = None
        self.create_year = None
        self.height_m = None
        self.mass_kg = None
        self.equipment = None


    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            manufacturer
            create_year
            height_m
            mass_kg
            equipment
        """

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'create_year': self.create_year,
            'height_m': self.height_m,
            'mass_kg': self.mass_kg,
            'equipment': self.equipment
        }


class Passengers:
    """Represents passengers carried on a Starship or Vehicle.

    Attributes:
        Accepts a list of < Person > and/or < Droid > objects that are added as key-value pairs
        to the new Passengers instance's `__dict__` dictionary of writable attributes. The
        < Person > or < Droid > "name" value serves as the key and the instance itself as the
        value. Each key-value pair added to __dict__ represents a new instance variable and value.

        < "name" > (Person | Droid): Person or Droid instance identified by name

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid > instances and calls the built-in function < setattr() > to create the instance
        variable and assign the value. The < Droid > or < Person > instance's "name" value serves
        as the new instance variable name (see format below) while the < Person > or < Droid >
        instance is assigned as the value.

        Instance variable name formatting rules:
            1. Change name to lowercase
            2. Replace space (' ') with underscore ('_')
            3. Replace dash ('-') with underscore ('_')

            "Luke Skywalker" -> "luke_skywalker"
            self.luke_skywalker = < Person >

            "C-3PO" -> "c_3po"
            self.c_3po = < Droid >

        Parameters:
            passengers (list): list of < Person > and/or < Droid > objects

        Returns:
            None
        """

        for val in passengers:
            passenger_name = val.name
            passenger_name = passenger_name.lower()
            passenger_name = passenger_name.replace(' ', '_')
            passenger_name = passenger_name.replace('-', '_')
            setattr(self, passenger_name, val)

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > or < Droid > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = f"Passengers: {val.name}" # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over the < Passengers >
        instance's __dict__ values and converts each < Person > or < Droid > object encountered
        to a dictionary. Accumulates dictionaries in a < list >.  After the loop terminates the
        new list is returned to the caller. Do not simply return self.__dict__. It can be
        intercepted and mutated, adding, modifying and/or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            list: nested person or droid dictionaries
        """

        passengers = []
        for key, val in self.__dict__.items():
            passengers.append(val.jsonable()) # person or droid object

        return passengers


class Person:
    """Represents a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height_m (float): person's height in centimeters
        mass_kg (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        force_sensitive (bool): ability to harness the power of the Force.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.force_sensitive = force_sensitive
        self.height_m = None
        self.mass_kg = None
        self.homeworld = None


    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
           url
           name
           birth_year
           height_m
           mass_kg
           homeworld
           force_sensitive
        """

        return {
            'url': self.url,
            'name': self.name,
            'birth_year': self.birth_year,
            'height_m': self.height_m,
            'mass_kg': self.mass_kg,
            'homeworld': self.homeworld,
            'force_sensitive': self.force_sensitive
        }


class Planet:
    """Represents a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in
                                     standard days
        diameter_km (int): diameter of planet measured in kilometers
        gravity_std (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.region = None
        self.sector = None
        self.suns = None
        self.moons = None
        self.orbital_period_days = None
        self.diameter_km = None
        self.gravity_std = None
        self.climate = None
        self.terrain = None
        self.population= None


    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying and/or removing instance attributes
        as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            region
            sector
            suns
            moons
            orbital_period_days
            diameter_km
            gravity_std
            climate
            terrain
            population
        """

        return {
            'url': self.url,
            'name': self.name,
            'region': self.region,
            'sector': self.sector,
            'suns': self.suns,
            'moons': self.moons,
            'orbital_period_days': self.orbital_period_days,
            'diameter_km': self.diameter_km,
            'gravity_std': self.gravity_std,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
        }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length_m (float): starship length in meters
        max_atmosphering_speed (int): maximum sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew_members (Crew): Crew instance assigned to starship
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity_kg (float): cargo capacity in kilograms that the starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished

    Methods:
        assign_crew_members: assign < Crew > instance to starship
        add_passengers: assign < Passengers > instance to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = None
        self.length_m = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.armament = None
        self.cargo_capacity_kg = None
        self.consumables = None
        self.crew_members = None
        self.passengers_on_board = None

    def __str__(self):
        """String representation of the object."""

        return self.model # not name (which is usually too generic)

    def add_passengers(self, passengers):
        """Assigns passengers to the instance variable < self.passengers_on_board > if passenger
        accommodations on the starship are available. Confirms that the passed in < passengers >
        argument is an instance of the < Passengers > class. If not a < Passengers > instance the
        < self.passengers_on_board > variable assignment is NOT performed.

        Parameters:
            passengers (Passengers): object containing < Person | Droid > instances

        Returns:
            None
        """

        if isinstance(passengers, Passengers):
            self.passengers_on_board = passengers

    def assign_crew_members(self, crew):
        """Assigns crew members to the instance variable < self.crew_members > if the crew size
        can be accommodated. Confirms that the passed in < crew > argument is an instance of
        the < Crew > class. If not a < Crew > instance the < self.crew_members > variable assignment
        is NOT performed.

        Parameters:
            crew (Crew): object comprising crew members ('< role >': < Person> / < Droid >)

        Returns:
            None
        """

        if isinstance(crew, Crew):
            self.crew_members = crew

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables

        Key order:
            url
            name
            model
            starship_class
            manufacturer
            length_m
            max_atmosphering_speed
            hyperdrive_rating
            MGLT
            armament
            crew_members
            passengers_on_board
            cargo_capacity_kg
            consumables
        """

        if hasattr(self, 'crew_members') and self.crew_members and isinstance(self.crew_members, Crew):
            crew_members = self.crew_members.jsonable()
        else:
            crew_members = None

        if hasattr(self, 'passengers_on_board') and self.passengers_on_board and isinstance(self.passengers_on_board, Passengers):
            passengers = self.passengers_on_board.jsonable()
        else:
            passengers = None

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'length_m': self.length_m,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew_members': crew_members,
            'passengers_on_board': passengers,
            'cargo_capacity_kg': self.cargo_capacity_kg,
            'consumables': self.consumables
        }


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the `convert_to_*` functions located in the
    module `swapi_utils` the task of converting the specified strings to either int, float, or
    list. Converting empty or blank values to None is handled locally.

    Conversions:
        str to None: all blank or empty values
        str to int: 'series_season_num', 'series_episode_num', 'season_episode_num'
        str to float: 'episode_prod_code', 'episode_us_viewers_mm'
        str to list: 'episode_writers'

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """

    for episode in episodes:
        for key, val in episode.items():
            if not val:
                episode[key] = None
            elif key == 'series_season_num' or key == 'series_episode_num' or key == 'season_episode_num':
                episode[key] = utl.convert_to_int(val)
            elif key == 'episode_prod_code' or key == 'episode_us_viewers_mm':
                episode[key] = utl.convert_to_float(val)
            elif key == 'episode_writers':
                episode[key] = utl.convert_to_list(val, ', ')
    return episodes




def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director name >: < episode count >,
            < director name >: < episode count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """

    directors_dict = {}
    for episode in episodes:
        director_name = episode['episode_director']
        if director_name in directors_dict.keys():
            directors_dict[director_name] += 1
        else:
            directors_dict[director_name] = 1
    return directors_dict

def create_droid(data):
    """Creates a < Droid > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Adding special instructions constitutes a seperate
    operation.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Parameters:
        data (dict): source data

    Returns:
        Droid: new < Droid > instance
    """

    droid = Droid(data['url'], data['name'], data['model'])
    for key, val in data.items():
        val = utl.convert_to_none(val)
        if key == 'height':
            droid.height_m = utl.convert_to_float(val)
        if key == 'mass':
            droid.mass_kg = utl.convert_to_float(val)
        if key == 'equipment':
            droid.equipment = utl.convert_to_list(val, '|')
        if key == 'manufacturer':
            droid.manufacturer = val
        if key == 'create_year':
            droid.create_year = val

    return droid


def create_person(data, planets=None):
    """Creates a < Person > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible. Calls < utl.get_swapi_resource() > to retrieve homeworld
    data. Adds additional planet information to the homeworld data dictionary if an optional
    < planets > dictionary is passed in as a second argument. Calls < create_planet() > to add
    a < Planet > object to the person instance before returning the new instance to the caller.

    Type conversions:
        height -> height_m (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to Planet)

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        Person: new < Person > instance
    """

    person = Person(data['url'], data['name'], data['birth_year'])
    for key, val in data.items():
        val = utl.convert_to_none(val)
        if key == 'force_sensitive':
            person.force_sensitive = val
        if key == 'height':
            person.height_m = utl.convert_to_float(val)
        if key == 'mass':
            person.mass_kg = utl.convert_to_float(val)
        if key == 'homeworld':
            swapi_homeworld = utl.get_swapi_resource(utl.SWAPI_PLANETS, {'planet': val})['results'][0]
            if planets is not None:
                for planet in planets:
                    if planet['name'] == val:
                        swapi_homeworld.update(planet)
            person.homeworld = create_planet(swapi_homeworld).jsonable()
    return person


def create_planet(data):
    """Creates a < Planet > instance from dictionary data, converting optional string values to the
    appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moon -> moons (str->int)
        orbital_period_days -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Parameters:
        data (dict): source data

    Returns:
        Planet: new < Planet > instance
    """
    planet = Planet(data['url'], data['name'])
    for key, val in data.items():
        val = utl.convert_to_none(val)
        if key == 'region':
            planet.region = val
        if key == 'sector':
            planet.sector = val
        if key == 'suns':
            planet.suns = utl.convert_to_int(val)
        if key == 'moons':
            planet.moons = utl.convert_to_int(val)
        if key == 'orbital_period':
            planet.orbital_period_days = utl.convert_to_float(val)
        if key == 'diameter':
            planet.diameter_km = utl.convert_to_int(val)
        if key == 'gravity':
            planet.gravity_std = utl.convert_gravity_value(val)
        if key == 'climate':
            planet.climate = utl.convert_to_list(val, ', ')
        if key == 'terrain':
            planet.terrain = utl.convert_to_list(val, ', ')
        if key == 'population':
            planet.population = utl.convert_to_int(val)
    return planet

def create_starship(data):
    """Creates a < Starship > instance from dictionary data, converting optional string values to
    the appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to float)

    Parameters:
        data (dict): source data

    Returns:
        starship: a new < Starship > instance
    """

    starship = Starship(data['url'], data['name'], data['model'], data['starship_class'])
    for key, val in data.items():
        val = utl.convert_to_none(val)
        if key == 'manufacturer':
            starship.manufacturer = val
        if key == 'length':
            starship.length_m = utl.convert_to_float(val)
        if key == 'max_atmosphering_speed':
            starship.max_atmosphering_speed = utl.convert_to_int(val)
        if key == 'hyperdrive_rating':
            starship.hyperdrive_rating = utl.convert_to_float(val)
        if key == 'MGLT':
            starship.MGLT = utl.convert_to_int(val)
        if key == 'armament':
            starship.armament = utl.convert_to_list(val, ',')
        if key == 'cargo_capacity':
            starship.cargo_capacity_kg = utl.convert_to_int(val)
        if key == 'consumables':
            starship.consumables = val
    return starship

def get_least_viewed_episode(episodes):
    """Identifies and returns episode with the lowest recorded viewership. Ignores episodes with
    no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task of
    determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the lowest recorded viewership.
    """

    lowest_views = 5000000000
    lowest_viewed_episode = None
    for episode in episodes:
        if has_viewer_data(episode) and episode['episode_us_viewers_mm'] < lowest_views:
            lowest_views = episode['episode_us_viewers_mm']
            lowest_viewed_episode = episode
    return lowest_viewed_episode


def get_most_viewed_episode(episodes):
    """Identifies and returns the episode with the highest recorded viewership. Ignores episodes
    with no viewship value. Ignores ties. Delegates to the function < has_viewer_data > the task
    of determing if the episode includes viewership "episode_us_viewers_mm" data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: episode with the highest recorded viewership.
    """

    highest_views = 0
    highest_viewed_episode = None
    for episode in episodes:
        if has_viewer_data(episode) and episode['episode_us_viewers_mm'] > highest_views:
            highest_views = episode['episode_us_viewers_mm']
            highest_viewed_episode = episode
    return highest_viewed_episode


def group_episodes_by_writer(episodes):
    """Utilizes a dictionary to group individual episodes by a contributing writer. The writer's
    name comprises the key and the associated value comprises a list of one or more episode
    dictionaries. Duplicate keys are NOT permitted.

    Format:
        {
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            < writer name >: [{< episode_01 >}, {< episode_02 >}, ...],
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that groups episodes by a contributing writer
    """

    writers_dict = {}
    for episode in episodes:
        writers_names = utl.convert_to_list(episode['episode_writers'], ', ')
        for writers_name in writers_names:
            if writers_name in writers_dict.keys():
                writers_dict[writers_name].append(episode)
            else:
                writers_dict[writers_name] = [episode]
    return writers_dict


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """

    viewers = episode['episode_us_viewers_mm']
    if type(viewers) is int and viewers != 0:
        return True
    elif type(viewers) is float and viewers != 0.0:
        return True
    elif type(viewers) is bool and viewers == True:
        return True
    elif type(viewers) is dict and len(viewers) > 0:
        return True
    elif type(viewers) is str and len(viewers) > 0:
        return True
    else:
        return False



def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 8.1 CHALLENGE 01
    clone_wars = utl.read_csv('clone_wars.csv')
    print(f"\nCLONE WARS = {clone_wars}")

    clone_wars_22 = clone_wars[1:5]
    print(f"\nCLONE WARS 22 = {clone_wars_22}")

    clone_wars_2012 = clone_wars[4:6]
    print(f"\nCLONE WARS 2012 = {clone_wars_2012}")

    clone_wars_url = clone_wars[6][-1]
    print(f"\nCLONE WARS URL = {clone_wars_url}")

    clone_wars_even_num_seasons = clone_wars[2::2]
    print(f"\nCLONE WARS EVEN NUMS = {clone_wars_even_num_seasons}")

    # 8.2 CHALLENGE 02
    clone_wars_episodes = utl.read_csv_to_dicts('clone_wars_episodes.csv')
    print(f"\nCLONE WARS EPISODES = {clone_wars_episodes}")
    true_count = 0
    for episode in clone_wars_episodes:
        if has_viewer_data(episode):
            true_count += 1
    print(f"\nCLONE WARS VIEWER DATA = {true_count}")
    # 8.3 Challenge 03
    print(f"\nconvert_to_int converted = {utl.convert_to_int('506')}")
    print(f"\nconvert_to_int no change = {utl.convert_to_int('unknown')}")
    print(f"\nconvert_to_int no change = {utl.convert_to_int([506, 507])}")

    print(f"\nconvert_to_float converted = {utl.convert_to_float('506.72')}")
    print(f"\nconvert_to_float no change = {utl.convert_to_float('unknown')}")
    print(f"\nconvert_to_float no change = {utl.convert_to_float([506.1, 507.4])}")

    print(f"\nconvert_to_list converted = {utl.convert_to_list('apple,banana,cherry', ',')}")
    print(f"\nconvert_to_list no change = {utl.convert_to_list('apple,banana,cherry')}")
    print(f"\nconvert_to_list no change = {utl.convert_to_list([506.1, 507.4])}")

    # 8.4 Challenge 04
    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    utl.write_json('stu-clone_wars-episodes_converted.json', clone_wars_episodes)

    # 8.5 Challenge 05
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)
    print(f"\nMOST VIEWED EPISODE = {most_viewed_episode}")

    least_viewed_episode = get_least_viewed_episode(clone_wars_episodes)
    print(f"\nLEAST VIEWED EPISODE = {least_viewed_episode}")

    # 8.6 Challenge 06
    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    utl.write_json('stu-clone_wars-director_episode_counts.json', director_episode_counts)

    # 8.7 CHALLENGE 07
    writer_episodes = group_episodes_by_writer(clone_wars_episodes)
    utl.write_json('stu-clone_wars-writer_episodes.json', writer_episodes)

    # 8.8 CHALLENGE 08
    print(f"\nChallenge 08: convert_to_none('n/a') = {utl.convert_to_none('n/a')}")
    print(f"\nChallenge 08: convert_to_none('unknown') = {utl.convert_to_none('UNKNOWN')}")
    print(f"\nChallenge 08: convert_to_none[1, 2, 3]) = {utl.convert_to_none([1, 2, 3])}")
    print(f"\nChallenge 08: convert_to_none('planet') = {utl.convert_to_none('planet')}")

    print(f"\nChallenge 08: convert_gravity_value('1 standard') = {utl.convert_gravity_value('1 standard')}")
    print(f"\nChallenge 08: convert_gravity_value('1.56') = {utl.convert_gravity_value('1.56')}")
    print(f"\nChallenge 08: convert_gravity_value([1, 2, 3]) = {utl.convert_gravity_value([1, 2, 3])}")

    # 8.9 CHALLENGE 09
    wookiee_planets = utl.read_csv_to_dicts('wookieepedia_planets.csv')
    tatooine_data = utl.get_swapi_resource(utl.SWAPI_PLANETS, {'search': 'Tatooine'})['results'][0]
    # print(f"\nWOOKIE PLANETS = {wookiee_planets}")
    # print(f"\nTATOOINE DATA = {tatooine_data}")
    wookiee_planet_tatooine = {}
    for i in range(len(wookiee_planets)):
        if wookiee_planets[i]['name'] == 'Tatooine':
            wookiee_planet_tatooine = wookiee_planets[i]
    tatooine_data.update(wookiee_planet_tatooine)
    print(tatooine_data)
    tatooine = create_planet(tatooine_data)

    utl.write_json('stu-tatooine.json', tatooine.jsonable())
    # 8.10 CHALLENGE 10
    wookiee_droids = utl.read_json('wookieepedia_droids.json')
    r2_d2_data = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'R2-D2'})['results'][0]
    wookiee_r2_d2 = {}
    for i in range(len(wookiee_droids)):
        if wookiee_droids[i]['name'] == 'R2-D2':
            wookiee_r2_d2 = wookiee_droids[i]
    r2_d2_data.update(wookiee_r2_d2)
    r2_d2 = create_droid(r2_d2_data)
    utl.write_json('stu-r2_d2.json', r2_d2.jsonable())

    # 8.11 Challenge 11
    wookiee_people = utl.read_json('wookieepedia_people.json')
    anakin_data = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Anakin Skywalker'})['results'][0]
    wookiee_anakin = {}
    for i in range(len(wookiee_people)):
        if wookiee_people[i]['name'] == 'Anakin Skywalker':
            wookiee_anakin = wookiee_people[i]
    anakin_data.update(wookiee_anakin)
    anakin = create_person(anakin_data, wookiee_planets)
    utl.write_json('stu-anakin_skywalker.json', anakin.jsonable())

    # 8.12 CHALLENGE 12
    wookiee_starships = utl.read_csv_to_dicts('wookieepedia_starships.csv')
    twilight_data = {}
    for i in range(len(wookiee_starships)):
        if wookiee_starships[i]['name'] == 'Twilight':
            twilight_data = wookiee_starships[i]
    twilight = create_starship(twilight_data)
    utl.write_json('stu-twilight.json', twilight.jsonable())

    # 8.13 CHALLENGE 13
    obi_wan_data = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Obi-Wan Kenobi'})['results'][0]
    wookiee_obi_wan = {}
    for i in range(len(wookiee_people)):
        if wookiee_people[i]['name'] == 'Obi-Wan Kenobi':
            wookiee_obi_wan = wookiee_people[i]
    obi_wan_data.update(wookiee_obi_wan)
    obi_wan = create_person(obi_wan_data, wookiee_planets)

    crew_members = {'pilot': anakin, 'copilot': obi_wan}
    crew = Crew(crew_members)
    twilight.assign_crew_members(crew)

    # 8.14 CHALLENGE 14

    padme_data = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'Padmé Amidala'})['results'][0]
    wookiee_padme = {}
    for i in range(len(wookiee_people)):
        if wookiee_people[i]['name'] == 'Padme Amidala':
            wookiee_padme = wookiee_people[i]
    padme_data.update(wookiee_padme)
    padme = create_person(padme_data, wookiee_planets)

    c_3po_data = utl.get_swapi_resource(utl.SWAPI_PEOPLE, {'search': 'C-3PO'})['results'][0]
    wookiee_c_3po = {}
    for i in range(len(wookiee_droids)):
        if wookiee_droids[i]['name'] == 'C-3PO':
            wookiee_c_3po = wookiee_droids[i]
    c_3po_data.update(wookiee_c_3po)
    c_3po = create_droid(c_3po_data)

    passengers = [padme, c_3po, r2_d2]
    passengers = Passengers(passengers)
    twilight.add_passengers(passengers)

    utl.write_json('stu-twilight_departs.json', twilight.jsonable())

if __name__ == '__main__':
    main()
