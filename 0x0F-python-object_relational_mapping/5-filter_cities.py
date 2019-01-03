#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name\
            FROM cities\
            INNER JOIN states\
            ON states.id = state_id\
            WHERE states.name = '{}'".format(argv[4]))
    results = cur.fetchall()
    print(", ".join([result[0] for result in results]))
    cur.close()
    db.close()
