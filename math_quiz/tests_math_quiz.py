import unittest
from math_quiz import generate_random_integer, generate_operator, calculate_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        Valid_operators= ['+','-','*']
        for _ in range(1000):
            operator= generate_operator()
            self.assertIn(operator, valid_operators)
        

    def test_calculate_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 5, '*', '4 * 5',20)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer =function_C(num1,num2,operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
            

if __name__ == "__main__":
    unittest.main()
