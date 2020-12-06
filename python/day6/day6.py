#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day6.py
# -------
# Solutions to Advent of Code 2020, day 6.
# https://adventofcode.com/2020/day/6
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
def get_groups(filename):
    print("Getting groups from the input file %s" % filename)

    groups = []
    my_input = get_input(filename)
    group = ""

    for line in my_input:
        if len(line) > 0:
            group += line + " "
        else:
            groups.append((group.split(" ")[:-1]))
            group = ""

    # Include the final group.
    groups.append((group.split(" ")[:-1]))
    return groups


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    answer_sum = 0

    groups = get_groups(filename)

    for group in groups:
        answers = set()
        for person in group:
            for answer in person:
                answers.add(answer)
        print("Different answers in group: %s" % (len(answers)))
        answer_sum += len(answers)

    print("Total number of answers: %d" % (answer_sum))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    answer_sum = 0

    groups = get_groups(filename)

    for group in groups:
        gset = []
        for person in group:
            pset = set()
            for answer in person:
                pset.add(answer)
            gset.append(pset)
        # The cool thing here is the "*gset" iterable.
        answer_sum += len(set.intersection(*gset))

    print("Total number of answers: %d" % (answer_sum))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 6")
    print("==========================")

    problem1("day6_input.txt")

    problem2("day6_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
