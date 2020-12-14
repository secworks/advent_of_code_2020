#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day11.py
# -------
# Solutions to Advent of Code 2020, day 11.
# https://adventofcode.com/2020/day/11
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
def compare_seatings(s1, s2):
    assert len(s1) == len(s2), "Error: Size of seatings are not equal."
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def occupy_seat(seat, left, right):
    if seat = ".":
        return False

    if seat = "L":
        tmp = True
        for s in left:
            if s = "L" or s = ".2"
    return False


#-------------------------------------------------------------------
# Implement the seating update logic.
#-------------------------------------------------------------------
def update_seating(seating):
    tmp = seating[:]
    w = len(seating[1])
    print("Width of seating row: %d" % (w))

    # Handle the middle 1..(w-2) seats
    for i in range(1, w - 2):
        if
    return tmp


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    seating = get_input(filename)
    new_seating = update_seating(seating)
    print(compare_seatings(seating, new_seating))
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
    print("Advent of Code 2020, day 11")
    print("==========================")

    problem1("day11_example.txt")

    problem2("day11_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
