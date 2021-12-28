# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

import csv
import copy


# PROBLEM 1 (4 Points)
def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line
    of decoded text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read.
        encoding (str): name of encoding used to decode the file.
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences.
        delimiter (str): delimiter that separates the row values

    Returns:
        list: a list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        #file_obj .txt
        # lines = file_obj.readlines()
        # content = file_obj.read()

        #.csv
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


# PROBLEM 2 (2 Points)
def create_header(header_string):
    """
    Returns a list of strings by splitting the input string. The input string should be split on the " | ".
    The space before and after the "|".

    Parameters:
        header (str): a string of headers' elements divided by the " | ".

    Return:
        list: a list of strings of the headers' elements without " | ".
    """
    header_split = header_string.split(' | ')
    return header_split

# PROBLEM 3 (2 Points)
def add_plants(plants, new_plants):
    """
    Returns a list of lists by adding all new plants not already in plants and
    removing the last special character of every string element in the single new plant (list) in new_plants (list).
    The name of duplicate plant in new plant (list) is 'Snake' which shouldn't be added to the plants (list).
    Use nested for loop to deal with every string elements in the single new plant (list) in new_plants (list).

    Parameters:
        plants (list): list of lists representing plants and their characteristics.
        new_plants (list): list of lists representing new arrival plants and their characteristics.

    Returns:
        list: list of lists includes all plants in the plants (list) and new_plants (list) without duplicates and special characters.
    """
    copy_plants = copy.deepcopy(plants)
    for new_plant in new_plants:
        for i in range(len(new_plant)):
            new_plant[i] = new_plant[i].strip('/')
        if new_plant in plants:
            continue
        else:
            copy_plants.append(new_plant)

    return copy_plants


# PROBLEM 4 (4 Points)
def count_avg_height(plants):
    """
    Returns the average height of all plants in plants (list) by looping through the plants list and
    calculating the average <"Max height"> value among all plants in the plants list.
    Find the position of <"Max height"> value according to the header. Change it from a string to an integer.

    Parameters:
        plants (list): list of lists representing plants and their characteristics.

    Return:
        int: average value of <"Max height"> among all plants.
    """
    height = 0
    for plant in plants:
        plant[1] = plant[1].strip(' feet')
        height += int(plant[1])
    average_height = height / len(plants)

    return int(average_height)


# PROBLEM 5 (4 Points)
def filter_large_plants(plants, avg_height):
    """
    Returns a list of plants whose < "Max height" > is larger than the avg_height.

    Parameters:
        plants (list): list of lists representing plants and their characteristics.
        avg_height (int): average value of < "Max height" >.

    Returns:
        list: list of lists that have the value of < "Max height" > larger than the average height.
    """
    max_height = []
    for plant in plants:
        height_string = plant[1].strip(' feet')
        height = int(height_string)
        if height > avg_height:
            max_height.append(plant)
    return max_height

# PROBLEM 6 (4 Points)
def write_csv(filepath, data, headers=None):
    """
    Returns a CSV file by writing data. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple.

    Returns:
        None
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        if(headers):
            writer.writerow(headers)
        writer.writerows(data)


def main():
    """
    Program entry point. Controls flow of execution. All function calls must be made from main().

    Parameters:
        None

    Returns:
        None
    """

    # SETUP
    header_string = "Name | Max height | Water | Sunlight | Price"
    # END SETUP

    # PROBLEM 1 (4 Points)
    houseplants_filepath = './houseplants.csv'
    houseplants = read_csv(houseplants_filepath)
    print(f'Houseplants list: {houseplants}')

    new_houseplants_filepath = './new_houseplants.csv'
    new_houseplants = read_csv(new_houseplants_filepath)
    print(f'New houseplants list: {new_houseplants}')

    # PROBLEM 2
    header = create_header(header_string)
    print(f'Header: {header}')

    # PROBLEM 3
    all_houseplants = add_plants(houseplants, new_houseplants)
    print(f'All houseplants list: {all_houseplants}')

    # PROBLEM 4
    avg_height = count_avg_height(all_houseplants)
    print(f'Average height: {avg_height}')

    # PROBLEM 5
    large_plants = filter_large_plants(all_houseplants, avg_height)
    print(f'Large plants: {large_plants}')

    # PROBLEM 6
    write_csv('all_houseplants.csv', all_houseplants, header)


if __name__ == '__main__':
    main()


# END LAB EXERCISE