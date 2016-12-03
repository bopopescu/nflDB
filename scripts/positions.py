import pymysql
import csv

# connect to db
conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "nflDB")

# get cursor
cur = conn.cursor()

# create command
stmt = "INSERT INTO positions (pos_id, position_name) VALUES (%s, %s)"

# datafield is list in this case normaly csv for more data
data = [
  ('QB', 'Quarterback'),
  ('RB', 'Running Back'),
  ('WR', 'Wide Receiver'),
  ('TE', 'Tight End'),
  ('C', 'Center'),
  ('OG', 'Offensive Guard'),
  ('OT', 'Offensive Tackle'),
  ('DE', 'Defensive End'),
  ('DT', 'Defensive Tackle'),
  ('LB', 'Linebacker'),
  ('DB', 'Defensive Back'),
  ('K', 'Kicker'),
  ('P', 'Punter'),
]

# execute command for each line of data
cur.executemany(stmt, data)

# save
conn.commit()

# close
cur.close()
conn.close()
