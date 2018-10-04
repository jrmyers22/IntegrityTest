import unittest
from DataCollection import VariableChecker


class MyTestCase(unittest.TestCase):

    def test_variable_checker(self):
        VariableChecker.create_table()
        VariableChecker.read_variables_in_code("RandomVariableTests", "Caleb Gould")
        VariableChecker.print_variables()
        VariableChecker.clear_table()


if __name__ == '__main__':
    unittest.main()
