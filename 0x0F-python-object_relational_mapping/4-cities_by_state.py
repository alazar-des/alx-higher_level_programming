#!/usr/bin/python3
"""Print records of all a table.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # prepare a cursor object
    cursor = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN \
states ON states.id=cities.state_id ORDER BY id"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception:
        print("Error: Unable to fetch.")

    db.close()
