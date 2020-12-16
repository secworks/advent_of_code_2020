#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day16.py
# --------
# Solutions to Advent of Code 2020, day 16.
# https://adventofcode.com/2020/day/16
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
# Extract nearby tickets.
#-------------------------------------------------------------------
def get_nearby_tickets(raw):
    tickets = []
    found_tickets = False

    for l in raw:
        if found_tickets:
            tickets.append(l)
        if "nearby tickets:" in l:
            found_tickets = True
    return tickets


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")
    raw = get_input(filename)
    nearby_tickets = get_nearby_tickets(raw)
    print(nearby_tickets)
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
    print("Advent of Code 2020, day 16")
    print("===========================")

    problem1("day16_input.txt")

    problem2("day16_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
