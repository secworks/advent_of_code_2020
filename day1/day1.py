#!/usr/bin/env python3
#=======================================================================
#
# day1.py
# -------
# Solutions to Advent of Code 2020, day 1.
#
#=======================================================================

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
def problem1(my_sum):
    print("Problem 1")
    print("---------")
    print("Find product of two numbers that sum to %d." % (my_sum))
    my_list1 = get_input("day1_input.txt")
    my_list2 = my_list1[1:]
    for a in my_list1:
        for b in my_list2:
            if a + b == my_sum:
                print("%d + %d = %d" % (a, b, my_sum))
                print("%d * %d = %d" % (a, b, (a * b)))
                print("")
                return


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(my_sum):
    print("Problem 2")
    print("---------")
    print("Find product of three numbers that sum to %d." % (my_sum))
    my_list1 = get_input("day1_input.txt")
    my_list2 = my_list1[1:]
    my_list3 = my_list1[2:]
    for a in my_list1:
        for b in my_list2:
            for c in my_list3:
                if a + b + c == my_sum:
                    print("%d + %d + %d = %d" % (a, b, c, my_sum))
                    print("%d * %d * %d = %d" % (a, b, c, (a * b * c)))
                    print("")
                    return


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2020, day 1")
print("==========================")
problem1(2020)
problem2(2020)

#=======================================================================
#=======================================================================
