#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb
if __name__ == "__main__":
    states = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = states.cursor()
    cur.execute("SELECT * from states ORDER BY id ASC")
    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    states.close()
