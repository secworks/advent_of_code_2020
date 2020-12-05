#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day3.py
# -------
# Solutions to Advent of Code 2020, day 4.
# https://adventofcode.com/2020/day/4
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
def get_tickets(filename):
    print("Getting tickets from the input file %s" % filename)

    tickets = []
    my_input = get_input(filename)
    ticket = ""

    for line in my_input:
        if len(line) > 0:
            ticket += line + " "
        else:
            tickets.append((ticket.split(" ")[:-1]))
            ticket = ""

    # Include the final ticket.
    tickets.append((ticket.split(" ")[:-1]))
    return tickets


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    tickets = get_tickets(filename)
    for ticket in tickets:
        print(ticket)
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
    print("Advent of Code 2020, day 4")
    print("==========================")

    problem1("day4_example.txt")

    problem2("day4_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
