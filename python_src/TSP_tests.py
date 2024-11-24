import unittest
from TSP import calculate

class TestCalculateFunction(unittest.TestCase):
    def test_basic_case(self):
        destinations = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        optimal_paths = [
            [0, 1, 3, 2, 0],
            [0, 2, 3, 1, 0]
        ]
        optimal_cost = 80.0
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

    def test_single_destination(self):
        destinations = [
            [0, 5],
            [5, 0]
        ]
        optimal_paths = [
            [0, 1, 0]
        ]
        optimal_cost = 10.0
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

    def test_three_destinations(self):
        destinations = [
            [0, 8, 15],
            [8, 0, 10],
            [15, 10, 0]
        ]
        optimal_paths = [
            [0, 1, 2, 0],
            [0, 2, 1, 0]
        ]
        optimal_cost = 33.0
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

    def test_large_float_values(self):
        destinations = [
            [0, 100.5, 200.25, 300.75],
            [100.5, 0, 400.5, 500.25],
            [200.25, 400.5, 0, 600.75],
            [300.75, 500.25, 600.75, 0]
        ]
        optimal_paths = [
            [0, 2, 3, 1, 0]
        ]
        optimal_cost = 1401.75
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

    def test_asymmetric_graph(self):
        destinations = [
            [0, 10, 20],
            [5, 0, 25],
            [10, 15, 0]
        ]
        optimal_paths = [
            [0, 1, 2, 0],
            [0, 2, 1, 0]
        ]
        optimal_cost = 40.0
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

    def test_decimal_values(self):
        destinations = [
            [0, 1.5, 2.5, 3.5],
            [1.5, 0, 4.5, 5.5],
            [2.5, 4.5, 0, 6.5],
            [3.5, 5.5, 6.5, 0]
        ]
        optimal_paths = [
            [0, 1, 2, 3, 0],
            [0, 3, 2, 1, 0]
        ]
        optimal_cost = 16.0
        path, cost = calculate(destinations)
        self.assertIn(path, optimal_paths)
        self.assertAlmostEqual(cost, optimal_cost)

if __name__ == '__main__':
    unittest.main()
