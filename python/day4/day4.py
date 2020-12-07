#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day4.py
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
# Load the file and extract the raw ticket data.
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
# Create a list of dicts, each dict corresponds to a ticket with
# fields matching the key-value pairs in the ticket.
#-------------------------------------------------------------------
def get_db(tickets):
    tickets_db = []
    for ticket in tickets:
        ticket_db = {}
        for field in ticket:
            (key, value) = field.split(":")
            ticket_db.update({key:value})
        tickets_db.append(ticket_db)
    return tickets_db


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_all_fields_or_no_cid(d):
    if ((len(d.keys()) == 8) or
        ((len(d.keys()) == 7) and "cid" not in d)):
        return True
    else:
        return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_birth_year(d):
    if 'byr' in d.keys() and \
      (int(d['byr']) >= 1920) and (int(d['byr']) <= 2002):
        return True
    else:
        return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_issue_year(d):
    if 'iyr' in d.keys() and \
      (int(d['iyr']) >= 2010) and (int(d['iyr']) <= 2020):
        return True
    else:
        return False

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def check_expiry_year(d):
    if 'eyr' in d.keys() and \
      (int(d['eyr']) >= 2020) and (int(d['eyr']) <= 2030):
        return True
    else:
        return False


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1(filename):
    print("Problem 1")
    print("---------")

    # Get tickets and parse into a list of dicts.
    tickets = get_tickets(filename)
    db = get_db(tickets)

    valid = 0
    for d in db:
        if check_all_fields_or_no_cid(d):
            valid += 1
    print("Number of valid tickets: %d" % (valid))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2(filename):
    print("Problem 2")
    print("---------")

    # Get tickets and parse into a list of dicts.
    tickets = get_tickets(filename)
    db = get_db(tickets)

    valid = 0
    for d in db:
        if check_all_fields_or_no_cid(d) and \
          check_birth_year(d) and \
          check_issue_year(d) and \
          check_issue_year(d):

            valid += 1

    print("Number of valid tickets: %d" % (valid))
    print("")

    print("")




#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2020, day 4")
    print("==========================")

    problem1("day4_input.txt")

    problem2("day4_example.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
