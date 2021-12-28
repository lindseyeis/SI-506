# SI 506 Problem Set 05

import csv
import copy
import os

print("Problem 01\n\n")

# Problem 01: Implement read_csv and load the election data.
# write a function read_csv defines one parameter
# filepath-string (path and name of file)
# load csv file and return contents (list of lists)-row csv file
def read_csv(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as file_obj:
        data = file_obj.readlines()
        output_list = []
        for line in data:
            list = line.replace('\n','').split(',')
            output_list.append(list)
            print(list)
        return output_list

raw_election_data_2021 = read_csv('election_data_2021.csv')
raw_election_data_2017 = read_csv('election_data_2017.csv')


print("\n\nProblem 02\n\n")

# Problem 02: Implement clean and clean the election data.

def clean(data):
    data_copy = copy.deepcopy(data)
    for list in data_copy[1:]:
        list[0] = list[0].strip()
        list[1] = int(list[1].strip())
        list[2] = list[2].strip().lower()
    return data_copy

clean_election_data_2021 = clean(raw_election_data_2021)
clean_election_data_2017 = clean(raw_election_data_2017)

print("\n\nProblem 03\n\n")

# Problem 03: Implement get_party_seat_differences and get the party seat differences for the 2021 election.

def get_seat_differences(current_election,previous_election):
    seat_differences = []
    for current_party_data in current_election[1:]:
        party_name = current_party_data[0]
        party_seats = current_party_data[1]
        for previous_party_data in previous_election[1:]:
            previous_party_name = previous_party_data[0]
            previous_party_seats = previous_party_data[1]
            if party_name == previous_party_name:
                seat_differences.append((party_name, party_seats - previous_party_seats))
    return seat_differences

party_seat_differences = get_seat_differences(clean_election_data_2021,clean_election_data_2017)
print(party_seat_differences)

print("\n\nProblem 04\n\n")


# Problem 04: Implement get_leaders and get the leaders for the 2021 election data.
party_leaders_2021 = [
                        ('AfD', 'Joerg Meuthen and Tino Chrupalla'),
                        ('FDP', 'Christian Lindner'),
                        ('CDU/CSU', 'Armin Laschet'),
                        ('SPD', 'Olaf Scholz'),
                        ('Greens', 'Annalena Baerbock and Robert Habeck'),
                        ('Left', 'Janine Wissler and Susanne Hennig-Wellsow')
                    ]

def get_leaders(election_data,party_leaders):
    copy_election_data = copy.deepcopy(election_data)
    copy_election_data[0].append('Party Leader(s)')
    for data in copy_election_data[1:]:
        party_name = data[0]
        for party_tuple in party_leaders:
            leader_party_name, leader_names = party_tuple
            if party_name == leader_party_name:
                data.append(leader_names)
    return copy_election_data
election_data_2021_with_leaders = get_leaders(clean_election_data_2021, party_leaders_2021)
print(election_data_2021_with_leaders)
print("\n\nProblem 05\n\n")

# Problem 05: Implement get_affiliation_percents and get affiliation percents for the 2021 election data.

def get_seats_percent(election_data):
    total_seats = 0
    left_seats = 0
    right_seats = 0
    center_seats = 0
    extreme_seats = 0

    for data in election_data[1:]:
        current_seats = data[1]
        current_affiliation = data[2]
        total_seats += current_seats
        if 'left' in current_affiliation:
            left_seats += current_seats
        elif 'right' in current_affiliation:
            right_seats += current_seats
        if 'far' in current_affiliation:
            extreme_seats += current_seats
        else:
            center_seats += current_seats

    left_percent = round(((left_seats / total_seats) * 100), 2)
    right_percent = round(((right_seats / total_seats) * 100), 2)
    center_percent = round(((center_seats / total_seats)) * 100, 2)
    extreme_percent = round(((extreme_seats / total_seats)) * 100, 2)

    return (left_percent, right_percent, extreme_percent, center_percent)

affiliation_percents = get_seats_percent(election_data_2021_with_leaders)
print(affiliation_percents)
print("\n\nProblem 06\n\n")


# Problem 06: Implement write_csv and write election_data_2021_with_leaders to a file called revised_election_data_2021.csv.

def write_csv(filepath,data):
    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(data)
write_csv('revised_election_data_2021.csv', election_data_2021_with_leaders)
