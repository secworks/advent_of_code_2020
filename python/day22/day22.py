#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day22.py
# --------
# Solutions to Advent of Code 2020, day 22.
# https://adventofcode.com/2020/day/22
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
# Parse the input and extract the player cards.
#-------------------------------------------------------------------
def get_cards(raw):
    p1 = []
    p2 = []

    i = 1
    while raw[i] != "":
        p1.append(int(raw[i]))
        i += 1

    i += 2
    for l in raw[i:]:
        p2.append(int(l))

    return (p1, p2)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def play_game(p1, p2):
    r = 1
    while (len(p1) > 0) and (len(p2) > 0):
        print("--- Round %d ---" % (r))
        print("Player 1's deck:", p1)
        print("Player 2's deck:", p2)

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        print("Player 1 plays %d" % (c1))
        print("Player 2 plays %d" % (c2))

        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
            print("Player 1 wins the round!")

        else:
            p2.append(c2)
            p2.append(c1)
            print("Player 2 wins the round!")

        r += 1
        print("")

    if len(p1) > 0:
        return (1, p1, (r - 1))
    else:
        return (2, p2, (r - 1))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_score(cards):
    s = 0
    n = len(cards)
    while len(cards) > 0:
        s += cards.pop(0) * n
        n -= 1
    return s


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

#    print("Testing game:")
#    (player, cards, rounds) = play_game([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
#    print(player, cards, rounds)
#    print("Test score: %d" % (get_score(cards)))

    raw = get_input(filename)
    (p1, p2) = get_cards(raw)
    (player, cards, rounds) = play_game(p1, p2)
    score = get_score(cards)

    print("Winner was player %d after %d rounds." % (player, rounds))
    print("Final score was: %d" % (score))
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

    problem1("day22_input.txt")

    problem2("day22_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
