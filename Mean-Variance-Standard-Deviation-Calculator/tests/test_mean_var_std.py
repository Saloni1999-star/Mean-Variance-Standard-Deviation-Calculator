import unittest
from mean_var_std import calculate

class TestMeanVarStdCalculator(unittest.TestCase):

    def test_valid_input(self):
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_output = {
            'mean': [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [6.0, 6.0, 6.0], 6.0],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [2.449489742783178, 2.449489742783178, 2.449489742783178], 2.449489742783178],
            'max': [[7, 8, 9], [3, 6, 9], 9],
            'min': [[1, 2, 3], [1, 4, 7], 1],
            'sum': [[12, 15, 18], [6, 15, 24], 45]
        }
        self.assertEqual(calculate(input_data), expected_output)

    def test_invalid_input_length(self):
        input_data = [1, 2, 3]
        with self.assertRaises(ValueError):
            calculate(input_data)

    def test_invalid_input_type(self):
        input_data = [1, 2, 'three', 4, 5, 6, 7, 8, 9]
        with self.assertRaises(ValueError):
            calculate(input_data)

if __name__ == '__main__':
    unittest.main()