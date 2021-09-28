#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day23.py
# --------
# Solutions to Advent of Code 2020, day 24.
# https://adventofcode.com/2020/day/24
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
#-------------------------------------------------------------------
def get_steps(s):
    cmd = []
    i = 0
    while i < len(s):
        if s[i] == "e" or s[i] == "w":
            cmd.append((s[i]))
            i += 1

        elif s[i] == "s" or s[i] == "n":
            cmd.append((s[i] + s[(i + 1)]))
            i += 2
    return cmd


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_name(x, y):
    return "tile_" + str(x) + "_" + str(y)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def walk_tiles(steps):
    x = 0
    y = 0
    num_steps = 0

#    print("Will walk the follwing steps:", steps)

    for step in steps:
#        print("step: %s" % (step))

        if step == "e":
            x -= 2

        elif step == "w":
            x += 2

        elif step == "se":
            x -= 1
            y -= 1

        elif step == "sw":
            x += 1
            y -= 1

        elif step == "ne":
            x -= 1
            y += 1

        elif step == "nw":
            x += 1
            y += 1

        num_steps += 1
        tile_name = get_name(x, y)
#        print("step: %d. Moving %s to %s" % (num_steps, step, tile_name))
    return tile_name


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_tiles(steplists):
#    print("My list of steps: ", steplists)

    tiles = {}
    init_tile = get_name(0,0)
    tiles[init_tile] = "white"

    for l in steplists:
        steps = get_steps(l)
        end_tile = walk_tiles(steps)
        print("end tile is %s" % (end_tile))

        if end_tile in tiles:
            if tiles[end_tile] == "black":
                tiles[end_tile] = "white"
            else:
                tiles[end_tile] = "black"

            print("Tile %s has been seen before. Flipping it to %s" %\
                  (end_tile, tiles[end_tile]))
        else:
            tiles[end_tile] = "black"
            print("Tile %s is a new tile." % (end_tile))
        print("")
    return tiles


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def print_stats(tiles):
    black = 0
    for t in tiles:
        if tiles[t] == "black":
            black += 1
    print("Total number of tiles: %d" % (len(tiles)))
    print("Number of black tiles: %d" % (black))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def example1():
    print("Example 1")
    print("---------")

    filename = "day24_example.txt"
    my_input = get_input(filename)
    my_tiles = get_tiles(my_input)
    print_stats(my_tiles)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    filename = "day24_input.txt"
    my_input = get_input(filename)
    my_tiles = get_tiles(my_input)
    print_stats(my_tiles)
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
    print("Advent of Code 2020, day 22")
    print("===========================")

    example1()
    problem1()

    sys.exit(0)

#=======================================================================
#=======================================================================
