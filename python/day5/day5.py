#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day5.py
# -------
# Solutions to Advent of Code 2020, day 5.
# https://adventofcode.com/2020/day/5
#
#=======================================================================

import sys

TEST = True

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
# Given a seating code, calculate return the row and column.
#-------------------------------------------------------------------
def get_row_column_id(seating):
    row_distance = 64
    row = 0
    column_distance = 4
    column = 0
    for c in seating:
        if c == "F":
            row_distance = int(row_distance / 2)

        if c == "B":
            row += row_distance
            row_distance = int(row_distance / 2)

        if c == "L":
            column_distance = int(column_distance / 2)

        if c == "R":
            column += column_distance
            column_distance = int(column_distance / 2)


    return (row, column, (row * 8 + column))



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    tickets = get_input(filename)

    # Tests with the given examples.
    print("Seat (row, columnm id) for BFFFBBFRRR is:", get_row_column_id("BFFFBBFRRR"))
    print("Seat (row, columnm id) for FFFBBBFRRR is:", get_row_column_id("FFFBBBFRRR"))
    print("Seat (row, columnm id) for BBFFBBFRLL is:", get_row_column_id("BBFFBBFRLL"))

    ms = (0, 0, 0)
    for ticket in tickets:
        (srow, scolumn, sid) = get_row_column_id(ticket)
        if sid > ms[2]:
            ms = (srow, scolumn, sid)

    print("Seat with max id:", ms)
    print("Max id: %d" % ms[2])

    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def occupied_seats(row):
    seats = 0
    for seat in row:
        if seat == 1:
            seats += 1
    return seats


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_free_seat(row):
    for i in range(8):
        if row[i] == 0:
            return i


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    tickets = get_input(filename)

    # Create an empty plane.
    plane = [[0] * 8 for i in range(128)]

    # Fill the plane with people.
    for ticket in tickets:
        (r, c, i) = get_row_column_id(ticket)
        plane[r][c] = 1

    for i in range(128):
        if occupied_seats(plane[i]) == 7:
            column = get_free_seat(plane[i])
            print("id for my seat: %d" % (8 * i + column))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 5")
    print("==========================")

    problem1("day5_input.txt")

    problem2("day5_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
