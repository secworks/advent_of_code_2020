#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day13.py
# --------
# Solutions to Advent of Code 2020, day 13.
# https://adventofcode.com/2020/day/13
#
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
def get_buses(raw):
    buses = []
    data = raw.split(",")
    for d in data:
        if d != 'x':
            buses.append(int(d))
    return buses


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    my_input = get_input(filename)
    my_departure = int(my_input[0])
    my_buses = get_buses(my_input[1])
    min_wait = 1000000000
    best_id = 0

    for bus in my_buses:
        wait = (bus * (1 + int(my_departure / bus)) - my_departure)
        if wait < min_wait:
            min_wait = wait
            best_id = bus

    print("Bus with id %d will cause wait of %d." % (best_id, min_wait))
    print("id * wait: %d" % (best_id * min_wait))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    my_input = get_input(filename)

    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 13")
    print("===========================")

    problem1("day13_input.txt")

    problem2("day13_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
