import unittest
from Day2_Assignment import *


class TestFunction(unittest.TestCase):
    def test_odd_one_out(self):   # Q1
        self.assertEqual(odd_one_out([3, 3, 3, 6, 3, 3, 3]), 6)
        self.assertEqual(odd_one_out([53, 53, 53, -16, 53, 53, 53]), -16)

    def test_closest_to_mean(self):   # Q2
        self.assertEqual(closest_to_mean([45, 78, 12, 4, -8, 6]), 12)
        self.assertEqual(closest_to_mean([45, -78, -12, 4, -8, 6]), -8)

    def test_find_speed(self):   # Q3
        self.assertEqual(find_speed([45, 90, 36, 80, 65], [5, 4, 2, 8, 5]), [9.0, 22.5, 18.0, 10.0, 13.0])
        self.assertEqual(find_speed([34, 78, 56, 12], [2, 5, 25, 2]), [17.0, 15.6, 2.24, 6.0])

    def test_missing_no(self):   # Q4
        self.assertEqual(missing_no([45, 78, 12, 65, 34, 31], [34, 65, 45, 31, 78]), 12)
        self.assertEqual(missing_no([56, -34, -23, 165, -78, -90], [-34, 165, 56, -23, -78]), -90)

    def test_difference_between_two_lowest(self):   # Q5
        self.assertEqual(difference_between_two_lowest([34, 78, 12, 9, 7, 4, 90, 86]), 3)
        self.assertEqual(difference_between_two_lowest([45, 78, 23, 12, 24, 8, 1]), 7)

    def test_count_smaller_than_mean(self):   # Q6
        self.assertEqual(count_smaller_than_mean([23, 56, 87, 12, 32, 43, 67]), 4)
        self.assertEqual(count_smaller_than_mean([12, 6, 8, 2, 3, 1, 3, 1]), 5)
