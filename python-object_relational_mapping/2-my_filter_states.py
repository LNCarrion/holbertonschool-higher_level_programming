#!/usr/bin/python3
"""adding a 4th argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ displays values in states where name matched the argument 4 """
    password = '2792'
    dtb = MySQLdb.connect(host= 'localhost', user='root', port=3306,
    passwd="root", db='hbtn_0e_0_usa')
    """
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                          passwd=sys.argv[2], db=sys.argv[3])
                          """
    curs = dtb.cursor()
    curs.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)