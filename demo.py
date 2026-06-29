import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import numpy as np
import pandas as pd

tables = pd.read_sql("""SELECT *
                     FROM SQLITE_MASTER
                     WHERE TYPE='table';""", conn)
print(tables)


#INNER JOIN
country = pd.read_sql("""SELECT *
                    FROM COUNTRY""", conn)
print(country)

city = pd.read_sql("""SELECT *
                    FROM CITY""", conn)
print(city)

inner_join = pd.read_sql("""SELECT c.COUNTRY_ID, c.COUNTRY_NAME, ci.CITY_NAME
                      FROM COUNTRY C
                      INNER JOIN CITY ci
                      ON c.COUNTRY_ID == ci.COUNTRY_ID;""", conn)
print(inner_join)


#LEFT JOIN
players = pd.read_sql("""SELECT *
                    FROM PLAYER""", conn)
print(players)

seasons = pd.read_sql("""SELECT *
                    FROM SEASON""", conn)
print(seasons)

left_join = pd.read_sql("""SELECT *
                          FROM PLAYER
                          LEFT JOIN SEASON
                          ON PLAYER.PLAYER_ID == SEASON.MAN_OF_THE_SERIES;""", conn)
print(left_join)


#CROSS JOIN
cross_join = pd.read_sql("""SELECT c.COUNTRY_ID, c.COUNTRY_NAME, ci.CITY_NAME
                         FROM COUNTRY c
                         CROSS JOIN CITY ci;""", conn)
print(cross_join)


#UNION
teams = pd.read_sql("""SELECT *
                    FROM TEAM""", conn)
print(teams)

union = pd.read_sql("""SELECT PLAYER_NAME
                    FROM PLAYER
                    UNION
                    SELECT TEAM_NAME
                    FROM TEAM;""", conn)
print(union)