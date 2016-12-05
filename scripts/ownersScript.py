import pymysql
import csv

conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")
cur = conn.cursor()
stmt = "INSERT INTO owners (fname,lname) VALUES (%s, %s)"
cur = conn.cursor()
data = [
	"Bill Bidwill",
	"Arthur Blank",
	"Steve Bisciotti",
	"Kim Pergula",
	"Jerry Richardson",
	"Virginia McCaskey",
	"Mike Brown",
	"Jimmy Haslam",
	"Jerry Jones",
	"Pat Bowlen",
	"Martha Ford",
	"Green Bay Packers",
	"Robert McNair",
	"Jim Irsay",
	"Shahid Khan",
	"Clark Hunt",
	"Stan Kroenke",
	"Stephen Ross",
	"Zygi Wilf",
	"Robert Kraft",
	"Tom Benson",
	"John Mara",
	"Robert Johnson",
	"Mark Davis",
	"Jeffery Lurie",
	"Dan Rooney",
	"Alex Spanos",
	"Jed York",
	"Paul Allen",
	"Bryan Glazer",
	"Amy Strunk",
	"Dan Snyder"
]

for name in data:
	split = name.split()
	cur.execute(stmt,(split[0],split[1]))

conn.commit()


cur.close()
conn.close()



