import unittest
from quadratic import solve_quadratic


class TestSolveQuadraticSimplified(unittest.TestCase):

    def test_1_two_roots(self):
        result = solve_quadratic(1, -5, 6)  # x^2 - 5x + 6 = 0
        self.assertIsNotNone(result)
        self.assertEqual(set(round(r, 5) for r in result), {2.0, 3.0})

    def test_2_no_real_roots(self):
        result = solve_quadratic(1, 0, 1)  # d < 0
        self.assertEqual(result, tuple())

    def test_3_invalid_type(self):
        with self.assertRaises(TypeError):
            solve_quadratic("abc", 2, 3)

    def test_4_critical_case(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 0, 1)


if __name__ == '__main__':
    unittest.main()
