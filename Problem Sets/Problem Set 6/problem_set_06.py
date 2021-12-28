import csv
import copy
from os import strerror

#Problem 01
def read_csv(filepath, encoding='utf-8'):
    """
    This function reads in a csv and returns its contents as a list

    Parameters:
        filepath (str): A str representing the filepath for the file to be read
        encoding (str): A str representing the character encoding of the file

    Returns:
        (list): A list with the content of the file
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        data = file_obj.readlines()
        output_list = []
        for line in data:
            list = line.replace('\n', '').split(',')
            output_list.append(list)
        return output_list

#Problem 02
def add_ratings(shows, ratings):
    """
    This function makes a copy of a show list and adds the shows IMDb rating to it

    Parameters:
        shows (list): A list of shows
        ratings (list): A list of IMDb ratings for the shows

    Returns:
        (list): A list of shows with the ratings added
    """
    copy_shows = copy.deepcopy(shows)
    copy_shows[0].append('IMDb Rating')
    for show in copy_shows[1:]:
        show_name = show[0]
        for show_rating in ratings[1:]:
            if show_name.lower() == show_rating[0].lower():
                show.append(show_rating[1])
    return copy_shows

#Problem 03
def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    copy_shows = copy.deepcopy(shows)
    for show in copy_shows[1:]:
        show[3] = float(show[3])
        show[1] = show[1].split('/')
        show[2] = show[2].split('/')
    return copy_shows

#Problem 04
def get_highest_rated_show(shows):
    max_rating = 0
    title_creator = ()
    for show in shows[1:]:
        if show[3] > max_rating:
            max_rating = show[3]
            title_creator = (show[0], show[1])
    return title_creator


#Problem 05
def filter_by_genre(shows, search_genre):
    genre_list = []
    for show in shows[1:]:
        show_genres = show[2]
        for show_genre in show_genres:
            if show_genre.lower() == search_genre.lower():
                genre_list.append(show)
    return genre_list
#Problem 06
def stringify(shows):
    copy_shows = copy.deepcopy(shows)
    for show in copy_shows[1:]:
       show[1] = '/'.join(show[1])
       show[2] = '/'.join(show[2])
    return copy_shows
#Problem 07
def write_csv(filepath, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(data)
#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """
    #Problem 01
    netflix_data = read_csv('./netflix_data.csv') #TODO: Replace
    disney_data = read_csv('./disney_data.csv') #TODO: Replace
    netflix_ratings = read_csv('./netflix_ratings.csv') #TODO: Replace
    disney_ratings = read_csv('./disney_ratings.csv') #TODO: Replace

    #Problem 02
    netflix_data_with_ratings = add_ratings(netflix_data,netflix_ratings) #TODO: Replace
    disney_data_with_ratings = add_ratings(disney_data,disney_ratings) #TODO: Replace
    print(netflix_data_with_ratings)
    print(disney_data_with_ratings)
    #Problem 03
    clean_netflix_data = clean_show_data(netflix_data_with_ratings) #TODO: Replace
    clean_disney_data = clean_show_data(disney_data_with_ratings) #TODO: Replace
    print(clean_netflix_data)
    print(clean_disney_data)
    #Problem 04
    best_netflix_show = get_highest_rated_show(clean_netflix_data) #TODO: Replace
    best_disney_show = get_highest_rated_show(clean_disney_data) #TODO: Replace
    print(best_netflix_show)
    print(best_disney_show)
    #Problem 05
    netflix_sci_fi_shows = filter_by_genre(clean_netflix_data, 'Science Fiction')
    disney_sci_fi_shows = filter_by_genre(clean_disney_data, 'Science Fiction')
    sci_fi_shows = []
    header = [['Title', 'Creator(s)', 'Genre(s)', 'IMDb Rating']]
    sci_fi_shows.extend(header + netflix_sci_fi_shows + disney_sci_fi_shows)
    print('problem 5')
    print(sci_fi_shows)
    #print(clean_netflix_data)
    #print(header)
    #Problem 06
    stringified_sci_fi_shows = stringify(sci_fi_shows)
    print('problem 6')
    print(stringified_sci_fi_shows)

    #Problem 07
    write_csv('sci_fi_shows.csv', stringified_sci_fi_shows)
    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
    disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show
    )

#Do not delete
if __name__ == '__main__':
    main()
