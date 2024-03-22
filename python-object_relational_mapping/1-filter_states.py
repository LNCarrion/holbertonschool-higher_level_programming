#!/usr/bin/python3
"""creating a class that list all the states with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", port=3306,
                         user="root", passwd=" ", db="hbtn_0e_0_usa")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE BINARY 'N%' \
                   ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
