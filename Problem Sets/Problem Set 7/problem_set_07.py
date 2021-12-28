import csv
from os import write

def read_csv_to_dicts(filepath, encoding='utf-8-sig', newline='', delimiter=','):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data

def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    NOTE: This is a helper function - please do NOT edit or delete it.

    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)

# PROBLEM 2


def clean_data(data):
    """
    This function takes in data and returns a mutated version that converts string versions of numbers
    to their integer or float form depending on the type of value.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        (list): A list of dictionaries with the numerical values appropriately converted.
    """

    for dictionary in data:
        for key, val in dictionary.items():
            if key == 'points':
                dictionary['points'] = float(val)
                #val = float(val)
            if key == 'position':
                dictionary['position'] = int(val)
                #val = int(val)
    return data

# PROBLEM 3
def convert_time_to_ms(driver_dict):
    for key, val in driver_dict.items():
        if key == 'fastest_lap':
            time = val.split(':')
            time[0] = int(time[0])
            time[1] = int(time[1])
            time[2] = int(time[2])
            return time[0] * 60000 + time[1] * 1000 + time[2]


# PROBLEM 4
def add_fastest_lap_point(race_results):
    top_driver = None
    max_time = 3000000
    for item in race_results:
        lap_time = convert_time_to_ms(item)
        if lap_time < max_time and item['position'] <= 10:
            max_time = lap_time
            top_driver = item
    for driver in race_results:
        if driver == top_driver:
            driver['points'] += 1
    return race_results

# PROBLEM 5
def update_driver_standings(standings, race_result):
    for driver in standings:
        for results in race_result:
            if driver['driver'] == results['name']:
                driver['points'] += results['points']
    return standings

# PROBLEM 6


def compare_points_by_nation(standings, nationality1, nationality2):
    """
    This function calculates the average points for all drivers for two nations and returns
    a tuple with the name and average points for the nation with the higher average points.

    Parameters:
        standings (list): A list of dictionaries that contains the drivers' standings.
        nationality1 (str): A string signifying the first nationality to be checked for.
        nationality2 (str): A string signifying the second nationality to be checked for.

    Returns:
        (tuple): A tuple with the nationality and average points for the nation with
        the higher average points.
    """

    total_points_nationality1 = 0
    total_points_nationality2 = 0
    nationality_count_1 = 0
    nationality_count_2 = 0
    for driver in standings:
        if driver['nationality'] == nationality1:
            nationality_count_1 += 1
            total_points_nationality1 += driver['points']
        if driver['nationality'] == nationality2:
            nationality_count_2 += 1
            total_points_nationality2 += driver['points']
    nation1_avg = total_points_nationality1/nationality_count_1
    nation2_avg = total_points_nationality2/nationality_count_2
    if nation1_avg > nation2_avg:
        return (nationality1, round(nation1_avg,1))
    else:
        return (nationality2, round(nation2_avg,1))

#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """

    # PROBLEM 1
    standings = read_csv_to_dicts('driver_standings_pre_USGP.csv')
    race_result = read_csv_to_dicts('usgp_results.csv')

    print(f'\n{standings}')
    print(f'\n{race_result}')

    last_standing_keys = standings[-1].keys()
    print(f'\n{last_standing_keys}') # Uncomment to test

    third_standing_values = standings[2].values()
    print(f'\n{third_standing_values}') # Uncomment to test

    tenth_race_result_kv = race_result[9].items()
    print(f'\n{tenth_race_result_kv}') # Uncomment to test

    # PROBLEM 2
    cleaned_standings = clean_data(standings)
    print(f'\nCleaned standings:\n{cleaned_standings}')

    cleaned_race_result = clean_data(race_result)
    print(f'\nCleaned race results:\n{cleaned_race_result}')

    # PROBLEM 3 (Optional Check)
    convert_time = convert_time_to_ms(cleaned_race_result[0])
    print(f'\nConvert time:\n{convert_time}')
    # PROBLEM 4
    updated_race_results = add_fastest_lap_point(cleaned_race_result)
    print(f'\nUpdated Race Results:\n{updated_race_results}')
    # PROBLEM 5
    updated_standings = update_driver_standings(cleaned_standings, updated_race_results)
    print(f'\nUpdated Standings:\n{updated_standings}')
    # PROBLEM 6
    ger_vs_gbr = compare_points_by_nation(updated_standings, 'German', 'British')
    fra_vs_spa = compare_points_by_nation(updated_standings, 'French', 'Spanish')
    print(f'\nGerman vs British:\n{ger_vs_gbr}')
    print(f'\nFrance vs Spanish:\n{fra_vs_spa}')
    # PROBLEM 7
    write_filepath = 'driver_standings_post_USGP.csv'
    write_fieldnames = ['driver','team','nationality','points']
    write_dicts_to_csv(filepath=write_filepath, data=updated_standings, fieldnames=write_fieldnames)

    # DO NOT EDIT
    # return (last_standing_keys_str, third_standing_values_str, tenth_race_result_kv_str)

#DO NOT EDIT
if __name__ == '__main__':
    main()
