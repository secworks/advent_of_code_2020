#!/usr/bin/env python3

# Solutions to Advent of Code 2020, day 1.

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
def problem1():
    print("Problem 1")
    my_list1 = get_input("day1_input.txt")
    my_list2 = my_list1[1:]
    for a in my_list1:
        for b in my_list2:
            if a + b == 2020:
                print("%d + %d = 2020" % (a, b))
                print("%d * %d = %d" % (a, b, (a * b)))
                print("")
                return


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    my_list1 = get_input("day1_input.txt")
    my_list2 = my_list1[1:]
    my_list3 = my_list1[2:]
    for a in my_list1:
        for b in my_list2:
            for c in my_list3:
                if a + b + c == 2020:
                    print("%d + %d + %d = 2020" % (a, b, c))
                    print("%d * %d * %d = %d" % (a, b, c, (a * b * c)))
                    print("")
                    return


#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
