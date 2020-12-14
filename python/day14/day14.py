#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day14.py
# --------
# Solutions to Advent of Code 2020, day 14.
# https://adventofcode.com/2020/day/14
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
# Extract write instructions ans associated mask from the
# input file.
#-------------------------------------------------------------------
def get_instructions(filename):
    iset = []
    raw = get_input(filename)
    instr = []
    for l in raw:
        if "mask" in l:
            # New set of instructions.
            # If not first add previous instr.
            if instr != []:
                iset.append(instr)

            # Start new instruction list for the given mask.
            instr = [("set_mask", l.split("=")[1][1:])]

        else:
            # Extract the actual mem operations.
            addr = int(l.split("=")[0][4:-2])
            data = int(l.split("=")[1])
            instr.append(("write_mem", addr, data))

    # Add final inst.
    iset.append(instr)
    return iset


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def num_x(mask):
    s = 0
    for i in range(len(mask)):
        if mask[i] == "X":
            s += 1
    return s


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def new_mask(mask, b):
    r = ""
    bp = 0
    for i in range(len(mask)):
        if mask[i] == "X":
            r += b[bp]
            bp += 1
        else:
            r += mask[i]
    return r

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def masked_addr(mask, addr):
    res = ""
    for i in range(len(mask)):
        if mask[i] == '0':
            res += addr[i]

        if mask[i] == '1':
            res += '1'
    return res

#-------------------------------------------------------------------
# Given a mask and a base address return all possible addresses.
#-------------------------------------------------------------------
def decode_addr(mask, addr):
    xs = num_x(mask)
    bs = []
    al = []

    # Create set of bit patterns
    for i in range((2 ** xs)):
        bs.append(format(i, 'b').zfill(xs))

    # For each bit patten get new mask.
    # Then use the mask to ceate a final address.
    for b in bs:
        nm = new_mask(mask, b)
        oa = format(addr, 'b').zfill(len(mask))
        ma = masked_addr(nm, oa)
        al.append(ma)

    return al


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def masked_update(mask, curr, data):
    cs = format(curr, 'b').zfill(len(mask))
    ds = format(data, 'b').zfill(len(mask))

    us = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            us += ds[i]

        if mask[i] == '1':
            us += '1'

        if mask[i] == '0':
            us += '0'
    return int(us, 2)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def execute_instructions(iset):
    mem = {}
    curr_mask = ""
    for instr in iset:
        for i in instr:
            if i[0] == "set_mask":
                curr_mask = i[1]

            if i[0] == "write_mem":
                (cmd, addr, data) = i
                if addr in mem:
                    curr_value = mem[addr]
                else:
                    curr_value = 0

                mem[addr] = masked_update(curr_mask, curr_value, data)
    return mem


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def sum_memory(mem):
    s = 0
    for a in mem:
        s += mem[a]
    return s

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    iset = get_instructions(filename)
    mem = execute_instructions(iset)
    msum = sum_memory(mem)
    print("Total sum: %d" % msum)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")
    iset = get_instructions(filename)

    wa = 0
    num_addrs = 0
    for instr in iset:
        for i in instr:
            if i[0] == "set_mask":
                curr_mask = i[1]

            if i[0] == "write_mem":
                wa += 1
                (cmd, addr, data) = i
                al = decode_addr(curr_mask, addr)
                num_addrs += len(al)
    print("Original num: %d" % (wa))
    print("Total number of addresses: %d" % (num_addrs))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 14")
    print("===========================")

    problem1("day14_input.txt")

    problem2("day14_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
