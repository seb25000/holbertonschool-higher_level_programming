#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 0. Get all states"""

import sys
import pymysql

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit('Use: 0-select_states.py <mysql username> <mysql password> <database name>')

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        conn = pymysql.connect(host='localhost', port=3306, user=username,
                               password=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            results = cur.fetchall()

        for row in results:
            print(row)

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if conn:
            conn.close()