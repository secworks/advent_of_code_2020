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

    my_forest = get_input(filename)

    trees1 = count_trees(my_forest, 1, 1)
    trees2 = count_trees(my_forest, 3, 1)
    trees3 = count_trees(my_forest, 5, 1)
    trees4 = count_trees(my_forest, 7, 1)
    trees5 = count_trees(my_forest, 1, 2)

    trees_prod = trees1 * trees2 * trees3 * trees4 * trees5

    print("Number of trees encountered in slope 1: %d" % (trees1))
    print("Number of trees encountered in slope 2: %d" % (trees2))
    print("Number of trees encountered in slope 3: %d" % (trees3))
    print("Number of trees encountered in slope 4: %d" % (trees4))
    print("Number of trees encountered in slope 5: %d" % (trees5))

    print("The product of all trees: %d" % (trees_prod))

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
