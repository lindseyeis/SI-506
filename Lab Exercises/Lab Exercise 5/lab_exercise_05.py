# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

import csv
import os

# PROBLEM 01

def read_file(filepath):
    """Reads text file and returns each line as a list element.

    Parameters:
        filepath (str): path to file

    Returns
        list: list of all lines in the file
    """
    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.readlines()
        print(data)
        projects = []
        for item in data:
            print(item)
            item_without_n = item.strip()
            projects.append(item_without_n)
        return projects
filepath = 'project_data.txt' # Gradescope
projects = read_file(filepath)

# Create filepath using the os module (COMMENT OUT BEFORE SUBMITTING TO GRADESCOPE)
# abs_path = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(abs_path, 'project_data.txt')

print(f"\n1.0 {projects}")

# PROBLEM 02
def get_filtered_projects(projects,categories):
    """
    This function returns a filtered list of projects based on one or more passed in categories.

    Parameters:
        projects (list): a list of strings that represent project information.
        categories (list): list of categories used as filters

    Returns:
        list: A filtered list of tuples. Each tuple contains both project name and project goal
    """
    filtered_projects = []
    for item in projects:
        split = item.split(',')
        project_type, project_name, project_goal = split
        project_type = project_type.lower()
        for category in categories:
            category = category.lower()
            if category in project_type:
                filtered_projects.append((project_name, project_goal))
    return filtered_projects
categories = ['data', 'UI/UX']
data_ux_projects = get_filtered_projects(projects,categories)
print(f"\n2.0 {data_ux_projects}")

# PROBLEM 03

def write_file(file_name,list):
    with open(file_name, 'w', newline='', encoding='utf-8') as file_obj:
        for line in list:
            file_obj.write(str(line) + '\n')
    print(file_name)
write_file('data_ux_projects.txt',data_ux_projects)
