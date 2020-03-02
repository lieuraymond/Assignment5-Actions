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
