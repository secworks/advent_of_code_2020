#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day12.py
# -------
# Solutions to Advent of Code 2020, day 12.
# https://adventofcode.com/2020/day/12
#
#=======================================================================

import sys


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_directions(filename):
    raw = get_input(filename)
    d = []
    for l in raw:
        d.append((l[0], int(l[1:])))
    return d


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def turn_left(h, d):
    t = int(d / 90.0)

    for i in range(t):
        if h == 'N':
            nh = 'W'

        if h == 'E':
            nh = 'N'

        if h == 'S':
            nh = 'E'

        if h == 'W':
            nh = 'S'
        h = nh
    return h


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def turn_right(h, d):
    t = int(d / 90.0)

    for i in range(t):
        if h == 'N':
            nh = 'E'

        if h == 'E':
            nh = 'S'

        if h == 'S':
            nh = 'W'

        if h == 'W':
            nh = 'N'

        h = nh
    return h


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_state(s, d):
    (h, x , y) = s
    (dh, dd) = d

    if dh == 'N':
        y -= dd

    if dh == 'S':
        y += dd

    if dh == 'W':
        x -= dd

    if dh == 'E':
        x += dd

    if dh == 'F':
        if h == 'N':
            y -= dd

        if h == 'S':
            y += dd

        if h == 'W':
            x -= dd

        if h == 'E':
            x += dd

    if dh == 'L':
        h = turn_left(h , dd)

    if dh == 'R':
        h = turn_right(h , dd)


    return (h, x, y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def calc_manhattan_distance(s):
    (h, x, y) = s
    return abs(x) + abs(y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    directions = get_directions(filename)

    # State is position and heading.
    ship_state = ('E', 0, 0)

    for d in directions:
        ship_state = update_state(ship_state, d)

    md = calc_manhattan_distance(ship_state)
    print("Travel distance: %s" % (md))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 12")
    print("===========================")

    problem1("day12_input.txt")

    problem2("day12_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
