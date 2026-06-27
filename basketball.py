import sqlite3

database = 'basketball.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd

tables = pd.read_sql("""SELECT *
                    FROM SQLITE_MASTER
                    WHERE TYPE='table';""", conn)
print(tables)

player = pd.read_sql("""SELECT *
                    FROM PLAYER""", conn)
print(player)

player_salary = pd.read_sql("""SELECT *
                            FROM PLAYER_SALARY""", conn)
print(player_salary)

data = pd.read_sql("""SELECT NAMETEAM, NAMEPLAYER, VALUE, IS_ACTIVE
                    FROM (SELECT ps.NAMETEAM, ps.NAMEPLAYER, ps.VALUE, p.IS_ACTIVE,
                    ROW_NUMBER() OVER (PARTITION BY ps.NAMETEAM ORDER BY ps.NAMEPLAYER) AS rn
                    FROM PLAYER_SALARY ps
                    JOIN PLAYER p
                    ON ps.NAMEPLAYER = p.FULL_NAME)
                    WHERE rn = 1
                    ORDER BY NAMETEAM;""", conn)
print(data)