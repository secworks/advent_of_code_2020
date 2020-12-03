#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day3.py
# -------
# Solutions to Advent of Code 2020, day 3.
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
def problem1(filename):
    print("Problem 1")
    print("---------")

    my_input = get_input(filename)

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
    print("Advent of Code 2020, day 3")
    print("==========================")

    problem1("day3_input.txt")

    problem2("day3_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
