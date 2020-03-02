import math


def firstrun():
    return "success"


def area_circle(radius):
    return math.pi * math.pow(radius, 2)


def list_ends(list_in):
    return list_in[0], list_in[len(list_in)]


def days_between(date1, date2):
    return date2 - date1
