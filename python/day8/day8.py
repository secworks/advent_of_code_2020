#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day8.py
# -------
# Solutions to Advent of Code 2020, day 8.
# https://adventofcode.com/2020/day/8
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
def get_code(filename):
    raw = get_input(filename)
    code = []
    for line in raw:
        (op, operand) = line.split(" ")
        code.append((op, operand[0], int(operand[1:]), False))
    return code


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    code = get_code(filename)
    print(code)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_loop(code):
    acc = 0
    pc = 0
    icnt = 0

    while True:
        (op, sign, operand, visited) = code[pc]
        if visited:
            return (icnt, acc, (op, sign, operand))

        if op == "acc":
            code[pc] = (op, sign, operand, True)
            icnt += 1
            pc += 1
            if sign == "+":
                acc += operand
            else:
                acc -= operand


        if op == "jmp":
            code[pc] = (op, sign, operand, True)
            icnt += 1
            if sign == "+":
                pc = pc + operand
            else:
                pc = pc - operand


        if op == "nop":
            code[pc] = (op, sign, operand, True)
            icnt += 1
            pc += 1


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    code = get_code(filename)
    (icnt, acc, instr) = find_loop(code)
    print("Loop detected after %d instructions. Acc: %d" % (icnt, acc))
    print("Instruction where loop occurs:", instr)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 8")
    print("==========================")

    problem1("day8_input.txt")

    problem2("day8_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
