#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# dayN.py
# -------
# Solutions to Advent of Code 2020, day N.
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
    print("Advent of Code 2020, day N")
    print("==========================")

    problem1("dayN_input.txt")

    problem2("dayN_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
