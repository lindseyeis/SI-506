# SI 506 Midterm

import csv
from os import terminal_size
from typing import ItemsView


def calculate_points(club):
    """Computes club's total points after converting string values to integers
    based on the following equation:

    3 points per win + 1 point per draw. A loss nets zero points.

    Parameters:
        club (list): representation of a club

    Returns
        int: league points earned
    """
    # for item in club:
    #     wins = int(item[2])*3
    #     total_points = wins + int(item[3])
    #     print(total_points)
    # return total_points

    return club[2] * 3 + club[3]

def calculate_shot_conversation_rate(club, shot_category='shots'):
    """Calculates a club's goal scoring efficiency by dividing goals scored
    by either all shots attempted (< shots >) OR shots considered on target,
    i.e., shots on goal (< shots_on_goal >).

    Dividing a club's < goals_for > by < shots_on_goal > will result in a higher
    shot conversion rate than dividing by < shots >.

    The caller must pass in the string 'shots_on_goal' as an optional second
    argument in order to instruct the function to switch the divisor. Otherwise,
    the calculation is performed using the < shots > value as the divisor.

    Either way, the resulting conversion rate value is rounded to the third
    (3rd) decimal place before it is returned to the caller.

    Parameters:
        club (list): representation of a club
        shot_category (str): indicates the divisor to use when performing the
                             calculation (e.g., shots or shots on goal)

    Returns
        float: conversion rate rounded to the 3rd decimal place
    """
    rate = 0
    if shot_category == 'shots':
        rate = round(int(club[5]) / club[7], 3)
    elif shot_category == 'shots_on_goal':
        rate = round(int(club[5]) / club[8], 3)
    return rate


def calculate_goals_by_top_scorers_pct(club, top_scorers):
    """Calculates the percentage of club goals scored by league-recognized top
    scorers. The function delegates to < get_club_top_scorers > the task of
    retrieving the club's league-recognized top scorers. Divides a club's
    < goals_for > (GF) by the number of goals scored by its top scorers and then
    multipled by 100 to obtain the percentage value. The percentage value is
    then rounded to the second (2nd) decimal place

    The return value is a three-item tuple comprising a club's goals for,
    the top scorers goal count, and the computed percentage value of club
    goals scored by its league-recognized top scorers:

    (< goals for >, < top scorers goals >, < top scorers goals percent >)

    Parameters:
        club (list): representation of a club
        top_scorers (list): League-recognized top scorers

    Returns:
        tuple: comprising the club's goals for, top scorers goal count, and the
               percentage of club goals scored the club's top scorers rounded
               to the second (2nd) decimal place
     """

    top_scorers_for_team = get_club_top_scorers(top_scorers, club[0])
    total_goals = 0
    for scorer in top_scorers_for_team:
        total_goals += int(scorer[3])
    if total_goals > 0:
        percent = round((total_goals/club[5])*100, 2)
    else:
        percent = 0
    return (club[5], total_goals, percent)


def classify_club(club):
    """Classifies a club according to a three-tiered ranking system: 'top_tier',
    'middle_tier', 'bottom_tier'. Classifying a club is based on points earned
    during a particular season. The function delegates to < calculate_points >
    the task of calculating the club's points.

    Assigning a club to a tier is based on the following points scheme.

    Tiers:
        top_tier: > 35 points
        middle_tier: between 32 and 35 points (inclusive)
        bottom_tier: < 32 points

    Once the club is classified the function returns to the caller one of
    three labels: 'top_tier', 'middle_tier', or 'bottom_tier'.

    Parameters:
        club (list): representation of a club

    Returns:
        str: classification label
    """

    points = calculate_points(club)
    if int(points) > int(35):
        return 'top_tier'
    elif int(32) <= int(points) <= int(35):
        return 'middle_tier'
    elif int(points) < int(32):
        return 'bottom_tier'


def clean_club(club):
    """Converts number values read in as strings from the CSV file to integers.
    The club name string is ignored.

    Parameters:
        club (list): representation of a club

    Returns:
        list: mutated club list with "number" strings converted to integers
    """

 # TODO Implment
    for i in range(1,len(club)):
        club[i] = int(club[i])
    return club

def combine_data(club_info, standings, top_scorers):
    """Modifies the < club_info > list to include club records, top scorer-based
    statistics, shot conversion metrics, and club classifications. Delegates a
    number of tasks to other functions to retrieve the additional data.

    Additional data added to each of the nested club records in < club_info > includes:
        1. club record statistics (e.g., all values from matches played to points earned )
            get_club_record
        2. count of a club's league-recognized top scorers, if any
            get club top scorers
        3. number of goals scored by a club's league-recognized top scorers, if any
            get_clubs_top_scorers_counts
        4. percentage of club's goals scored by league-recognized top scorers, if any
            calculate_goals_by_top_scorers_pct
        5. shot conversion rate (all shots taken)
            get_clubs_shot_conversion_rates
        6. shots on goal conversion rate
            get_clubs_shot_conversion_rates
        7. club classification (e.g., 'top_tier', 'middle_tier', 'bottom_tier')
            classify clubs

    Parameters:
        club (list): representation of a club
        standings (list): league standings
        top_scorers (list): League-recognized top scorers

    Returns:
       list: mutated < club_info > list containing additional data about each club
    """
    return_list = []
    club_scorers_counts = get_clubs_top_scorers_counts(standings, top_scorers)
    for club in club_info:
        for standing in standings:
            if club[0].lower() == standing[0].lower():
                club_record = get_club_record(standings, club[0])
                club_top_scorers = get_club_top_scorers(top_scorers, club[0])
                print(club_scorers_counts)
                name, goals, percent = calculate_goals_by_top_scorers_pct(standing, top_scorers)
                club_records = get_club_record(standings, club[0])
                club_conversion_rates = calculate_shot_conversation_rate(club_records, 'shots')
                shots_conversion_rates = calculate_shot_conversation_rate(club_records, "shots_on_goal")
                classify = classify_club(standing)
                # print(club_record)
                # print(club_top_scorers)
                # print(club_scorers_counts)
                # print(top_scorers_percent)
                # print(club_conversion_rates)
                # print(shots_conversion_rates)
                # print(classify)
                return_val = club
                return_val.extend(club_record[1:])
                return_val.append(len(club_top_scorers))
                return_val.append(goals)
                return_val.append(percent)
                return_val.append(club_conversion_rates)
                return_val.append(shots_conversion_rates)
                return_val.append(classify)
                return_list.append(return_val)
    return return_list

def get_club_record(standings, club_name):
    """Returns a club record by the club's name. The name check is case-insentive.
    If a match on the club name is not obtained None is returned.

    Parameters:
        standings (list): league standings
        club_name (str): club name

    Returns
        list: representation of a club if match obtained; otherwise returns None
    """
    for standing in standings:
        if standing[0].lower().startswith(club_name.lower()):
            return standing
    # for item in standings: # TODO Implement
    # if standings[0] == club_name.lower():
    #     print(standings)
    # else:
    #         None
    # return standings


def get_club_top_scorers(top_scorers, club_name):
    """Filters league's top scorers by club affiliation. Performs a case
    insensitive comparison of the player's club name with the passed in
    < club_name >.

    Parameters:
        top_scorers (list): League-recognized top scorers
        club_name (str): club name to which the top scorer(s) are affiliated

    Returns:
        list: top scorer(s), if any, affiliated with the club
    """
    top_scorers_list = []
    for item in top_scorers: # TODO Implement
        if str(item[2]).lower() == str(club_name).lower():
            top_scorers_list.append(item)
    return top_scorers_list

def get_clubs_shot_conversion_rates(standings, shot_category='shots'):
    """Tabulates shot conversion rates for all clubs in < standings >. The
    function delegates to < calculate_shot_conversation_rate >
    the task of returning either its shot conversion rate or shots on goal
    conversion rate depending on the < shot_category > passed to the function
    < calculate_shot_conversation_rate >.

    The conversion rate returned by calling < calculate_shot_conversation_rate >
    is added to a tuple along with the club name, e.g.,

    (< club name >, < shot conversion rate >)

    The tuple is then appended to a local accumulator list. After all club
    conversion rates have been retrieved, the list of nested tuples is returned
    to the caller.

    Parameters:
        standings (list): league standings
        shot_category (str): indicates the divisor to use when performing the
                             calculation (e.g., shots or shots on goal)

    Returns:
        list: nested tuples of club shot conversion rates
    """
    conversion_rate_list = []
    for item in standings:
        conversion_rate = calculate_shot_conversation_rate(item, shot_category)
        conversion_rate_list.append((item[0], conversion_rate))
    return conversion_rate_list


def get_clubs_top_scorers_counts(standings, top_scorers):
    """Tabulates counts of club affiliated league-recognized top scorers for
    all clubs in < standings>. The function delegates to < get_club_top_scorers >
    the task of retrieving each club's league-recognized top scorers. The number
    of elements in the list returned by < get_club_top_scorers > constitutes the
    count.

    The club's name along with the count is placed in a tuple, e.g.,
    (< club name >, < top scorers count> ) which is appended to a local
    accumulator list. After each club's top scorers, if any, are retrieved
    and counted the accumulator list is returned to the caller.

    Parameters:
        standings (list): league standings
        top_scorers (list): League-recognized top scorers

    Returns:
       list: nested tuples of top scorer counts for each passed in club
    """
    topscorer_touples = []
    for item in standings:
        clubname = item[0]
        top_scorers_count = 0
        for topscorer in top_scorers: # TODO Implement
            if str(topscorer[2]).lower() == str(clubname).lower():
                top_scorers_count +=1
        topscorer_touples.append((clubname,top_scorers_count))
    return topscorer_touples




def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line
    of decoded text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: a list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Challenge 01

    # TODO 01.1-2 (required)
    filepath = 'nwsl-top_scorers-2021.csv'
    scorers_data = read_csv(filepath)
    print(f"\nProblem 1.1 = {scorers_data}")
    top_scorers_seven_goals = scorers_data[6:9]
    print(f"\nProblem 1.2 = {top_scorers_seven_goals}")

    # TODO 01.3-4 (required)
    filepath = 'nwsl-standings-2021.csv'
    standings_data = read_csv(filepath)
    print(f"\nProblem 1.3 = {standings_data}")
    standings_reversed = standings_data[::-1]
    print(f"\nProblem 1.4 = {standings_reversed}")

    # TODO 01.5-6 (required)
    filepath = 'nwsl-club_info-2021.csv'
    club_info_data = read_csv(filepath)
    print(f"\nProblem 1.5 = {club_info_data}")
    kc_stadium_name = club_info_data[3][5]
    print(f"\nProblem 1.6 = {kc_stadium_name}")

    # Challenge 02

    # TODO 02.1-4 (required)
    standings_header = standings_data[0]
    standings = standings_data [1:]
    print(f"\nProblem 2.1 = {standings_header}")
    print(f"\nProblem 2.1.1 = {standings}")

    for standing in standings:
        standing = clean_club(standing)
    print(f"\nProblem 2.2 = {standings}")

    pride_record = get_club_record(standings, club_name='Orlando Pride')
    print(f"\nProblem 2.3 = {pride_record}")

    # TODO 03.1-3 (required)

    standings_header.append('points')
    for club in standings:
        points = calculate_points(club)
        club.append(points)

    # Challenge 04

    # TODO 04.1 (required)
    clubs_classified = []
    # for i in range(1,len(club)):
        # club[i] = int(club[i])
    # for standing in standings:
    #     get_tiers = classify_club(standing)
    #     clubs_classified.append(get_tiers)
    # for tier in standings:
    #     print(tier)
    #     tier = classify_club(int(club[-1]))
    #     # clubs_classified.append(standings[0],tier)
    # # write_csv('stu-nwsl_clubs_classified-2021.csv', clubs_classified, headers=('club_name', 'tier'))
    for team in standings:
        tier = classify_club(team)
        touple = (team[0], tier)
        clubs_classified.append(touple)
    # clubs_classified = (get_tiers[0], get_tiers[-1])
    write_csv('stu-nwsl_clubs_classified-2021.csv', clubs_classified, headers=('club_name', 'tier'))
    # print(f"\nProblem 4 = {get_tiers}")

    # Challenge 05

    # TODO 05.1-2 (required)
    print(f"\nProblem 5.3 = {scorers_data}")
    scorers_header = scorers_data[0]
    print(f"\nProblem 5.3 = {scorers_header}")
    scorers = scorers_data[1:]
    ol_reign_scorers = get_club_top_scorers(scorers_data, 'OL Reign')
    print(f"\nProblem 5.1 = {ol_reign_scorers}")

    # Challenge 06

    # TODO 06.1 (required)
    top_scorer_count = get_clubs_top_scorers_counts(standings, scorers_data)
    print(f"\nProblem 6 = {top_scorer_count}")

    # Challenge 07

    # TODO 07.1 (required)
    portland_record = get_club_record(standings, 'Portland Thorns FC')
    conversion_rate = calculate_shot_conversation_rate(portland_record, 'shots_on_goal')
    print(f"\nProblem 7 = {conversion_rate}")
    # Challenge 08

    # TODO 08.1 (required)
    shots_on_goal_conversion_rates = get_clubs_shot_conversion_rates(standings, 'shots_on_goal')
    print(f"\nProblem 8 = {shots_on_goal_conversion_rates}")

    # Challenge 09

    # TODO 09.1 (required)
    club_goals_top_scorers_pct = []
    for item in standings:
        scorers_percent = calculate_goals_by_top_scorers_pct(item, scorers_data)
        goals_for, top_scorers_goals, top_scorers_goals_pct = scorers_percent
        club_goals_top_scorers_pct.append([item[0], goals_for, top_scorers_goals, top_scorers_goals_pct])
    # print(club_goals_top_scorers_pct)
    write_csv('stu-nwsl_club_goals_top_scorers_pct.csv', club_goals_top_scorers_pct, headers=('club','goals_for','top_scorer_goals','top_scorer_goals_pct'))

    # Challenge 10

    # TODO 10.1-5 (require)
    club_info_headers = club_info_data[0]
    club_info = club_info_data[1:]
    club_info_headers.extend(standings_header[1:])
    club_info_headers.append('top_scorers_count')
    club_info_headers.append('top_scorers_goals')
    club_info_headers.append('top_scorers_goals_pct')
    club_info_headers.append('shot_conversion_rate')
    club_info_headers.append('shots_on_goal_conversion_rate')
    club_info_headers.append('club_classification')
    combined_data = combine_data(top_scorers=scorers, standings=standings, club_info=club_info)
    write_csv('stu-nwsl_combined_data.csv', combined_data, headers=club_info_headers)

# WARN: Do not delete __name__ value check.
if __name__ == '__main__':
    main()
