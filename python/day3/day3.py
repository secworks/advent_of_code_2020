#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day3.py
# -------
# Solutions to Advent of Code 2020, day 3.
# https://adventofcode.com/2020/day/3
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
def is_tree(forest, x, y):
    width = len(forest[0])
    row = forest[y]
    if row[(x % width)] == "#":
        return 1
    else:
        return 0


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def count_trees(forest, step_x, step_y):
    count = 0
    height = len(forest)
    x = 0
    y = 0

    while y < height:
        count += is_tree(forest, x, y)
        x += step_x
        y += step_y

    return count


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    my_forest = get_input(filename)
    trees = count_trees(my_forest, 3, 1)
    print("Number of trees encountered: %d" % (trees))
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
