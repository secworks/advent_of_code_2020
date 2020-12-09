#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day9.py
# -------
# Solutions to Advent of Code 2020, day 9.
# https://adventofcode.com/2020/day/9
#
#=======================================================================

import sys


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(int(line.strip()))
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_sums(numlist):
    sums = set()
    js = 1
    for i in range(len(numlist) - 1):
        for j in range(js, len(numlist)):
            sums.add(numlist[i] + numlist[j])
        js += 1

    return sums


#-------------------------------------------------------------------
# Given a preamble, check if the given value is a sum of two
# values in the preamble.
#-------------------------------------------------------------------
def check_sum(val, preamble):
    sums = get_sums(preamble)
    return val in sums


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    numbers = get_input(filename)
    preamble = 25

    i = 0
    while check_sum(numbers[(i + preamble)], numbers[i:(i + preamble)]):
        i += 1
    print("The first number to not be a sum: %d" % numbers[(i + preamble)])
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
    print("Advent of Code 2020, day 9")
    print("==========================")

    problem1("day9_input.txt")

    problem2("day9_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
