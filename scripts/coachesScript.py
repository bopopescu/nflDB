import pymysql
import csv

conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "nflDB")
cur = conn.cursor()

coaches = []

with open('csv/coaches.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		coaches.append(row.get('Coaches'))

stmt = "INSERT INTO Coaches (fname,lname) VALUES (%s, %s)"

for coach in coaches:
	split = coach.split()
	fname = split[0]
	lname = split[1]
	cur.execute(stmt,(fname,lname))

conn.commit()


cur.close()
conn.close()


