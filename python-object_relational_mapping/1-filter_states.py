#!/usr/bin/python3
"""creating a class that list all the states with N"""

import MySQLdb
import sys
def list_states_starting_with_n(username, password, database):

    try:
        db = MySQLdb.connect