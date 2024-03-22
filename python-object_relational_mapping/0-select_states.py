#!/usr/bin/python3
"""creating a class"""
import MySQLdb
import sys


def list_states(username, password, database):
    """creating a class"""

    try:
        db = MySQLdb.Connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error:", e)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states(username, password, database)
