#!/usr/bin/env python3
#=======================================================================
#
# day2.py
# -------
# Solutions to Advent of Code 2020, day 2.
#
#=======================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l

#-------------------------------------------------------------------
# Parse given input into a list of tuples. Each tuple contains
# a possible range of chars, the specific char and the password.
#-------------------------------------------------------------------
def parse_input(my_input):
    r_p = []
    for line in my_input:
        (rule, pwd) = line.split(":")
        (r, c) = rule.split(" ")
        (low, high) = r.split("-")
        r_p.append(((int(low), int(high), c), pwd[1:]))
    return r_p


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_range(rule, pwd):
    (l, h, c) = rule
    c = pwd.count(c)
    if (c >= l) and (c <= h):
        return 1
    else:
        return 0



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_positions(rule, pwd):
    (p1, p2, c) = rule
    if ((pwd[(p1 - 1)] == c) and not (pwd[(p2 - 1)] == c)) or \
        ((pwd[(p2 - 1)] == c) and not (pwd[(p1 - 1)] == c)):
        return 1
    else:
        return 0


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    my_input = get_input("day2_input.txt")
    my_r_p = parse_input(my_input)

    valid = 0
    for (rule, pwd) in my_r_p:
        valid += check_range(rule, pwd)

    print("The number of valid passwords: %d" % (valid))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    my_input = get_input("day2_input.txt")
    my_r_p = parse_input(my_input)

    valid = 0
    for (rule, pwd) in my_r_p:
        valid += check_positions(rule, pwd)

    print("The number of valid passwords: %d" % (valid))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2020, day 2")
print("==========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
