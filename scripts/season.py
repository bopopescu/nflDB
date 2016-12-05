import pymysql
import csv

# connect to db
conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

# get cursor
cur = conn.cursor()

# create command
stmt = "INSERT INTO season (season_id, team_id) VALUES (%s, %s)"

# datafield is list in this case normaly csv for more data = 2007
for season_id in range(2007,2017):
    for team in range(1,33):

        data = [season_id, team]

        # execute command for each line of data
        cur.execute(stmt, data)



# save
conn.commit()

# close
cur.close()
conn.close()
