import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_area_circle(self):
        radius = 5
        self.assertEqual(task.area_circle(5), math.pi * pow(radius, 2))

    def test_list_ends(self):
        test_list = ["apple", "banana", "orange"]
        first, last = task.list_ends(test_list)
        self.assertEqual(first, "apple")
        self.assertEqual(last, "orange")
