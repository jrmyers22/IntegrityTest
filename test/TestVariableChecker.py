import unittest
from VariableChecker import VariableChecker


class MyTestCase(unittest.TestCase):

    def test_variable_checker(self):
        VariableChecker.read_variables_in_code("../TestFiles/RandomVariableTests.txt", "Caleb Gould")



if __name__ == '__main__':
    unittest.main()
