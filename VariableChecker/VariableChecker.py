import sqlite3
import re


connection = sqlite3.connect('Variables')
c = connection.cursor()

class VariableChecker:

    def __init__(self):

        c.execute('''CREATE TABLE variables
                    (name TEXT, variableName TEXT)''')


    def read_variables_in_code(self, file_name, student_name, ):
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines :
                if(line.__contains__("int")):
                    lineSplit = re.split(' ', line)
                    varName = lineSplit[2]
                    c.execute(''' INSERT INTO variables VALUES ({}, {},)
                    '''.format(student_name, varName))
                elif(line.__contains__("boolean")):
                    lineSplit = re.split(' ', line)
                    varName = lineSplit[2]
                    c.execute(''' INSERT INTO variables VALUES ({}, {},)
                               '''.format(student_name, varName))
                elif(line.__contains__("String")):
                    lineSplit = re.split(' ', line)
                    varName = lineSplit[2]
                    c.execute(''' INSERT INTO variables VALUES ({}, {},)
                                        '''.format(student_name, varName))
                elif(line.__contains__("double")):
                    lineSplit = re.split(' ', line)
                    varName = lineSplit[2]
                    c.execute(''' INSERT INTO variables VALUES ({}, {},)
                                        '''.format(student_name, varName))
                elif(line.__contains__("float")):
                    lineSplit = re.split(' ', line)
                    varName = lineSplit[2]
                    c.execute(''' INSERT INTO variables VALUES ({}, {},)
                                        '''.format(student_name, varName))