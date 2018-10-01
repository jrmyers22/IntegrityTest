import sqlite3
import re

connection = sqlite3.connect('Variables')
c = connection.cursor()
#c.execute('''DROP TABLE variables''')


def read_variables_in_code(file_name, student_name):
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines :
            if line.__contains__("int"):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                                VALUES ("{}", "{}");'''.format(student_name, varName))
            elif line.__contains__("boolean"):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                                VALUES ("{}", "{}");'''.format(student_name, varName))
            elif line.__contains__("String"):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                VALUES ("{}", "{}");'''.format(student_name, varName))
            elif line.__contains__("double"):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                                VALUES ("{}", "{}");'''.format(student_name, varName))
            elif line.__contains__("float"):
                lineSplit = re.split(' ', line)
                varName = lineSplit[1]
                c.execute(''' INSERT INTO variables (username, variableName)
                                VALUES ("{}", "{}");'''.format(student_name, varName))
    connection.commit()


def create_table():
    c.execute('''CREATE TABLE variables
                       (username VARCHAR(30), variableName VARCHAR(60))''')


def clear_table():
    c.execute("DROP TABLE variables")
    connection.commit()


def print_variables():
    c.execute("SELECT * FROM variables")
    list = c.fetchall()
    for i in range(0, list.__len__()):
        print(list[i][0])
        print(list[i][1])

