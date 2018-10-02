import sqlite3
import re

connection = sqlite3.connect('Variables')
c = connection.cursor()


# reads through the entirety of the file and pulls variable names out and prints them with the students name
def read_variables_in_code(file_name, student_name):
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines :
            if line.__contains__(" = "):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                                VALUES ("{}", "{}");'''.format(student_name, varName))

    connection.commit()

# creates the table if it has been cleared
def create_table():
    c.execute('''CREATE TABLE variables
                       (username VARCHAR(30), variableName VARCHAR(60))''')

# Clears all variables from the list
def clear_table():
    c.execute("DROP TABLE variables")
    connection.commit()

# prints all current variables in the list
def print_variables():
    c.execute("SELECT * FROM variables")
    list = c.fetchall()
    for i in range(0, list.__len__()):
        print(list[i][0])
        print(list[i][1])


# return a 2d array with all of the variables and names associated with them
def get_variable_list():
    c.execute("SELECT * FROM variables")
    list = c.fetchall()
    return list;