import pymysql
import csv

conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "nflDB")
cur = conn.cursor()
stmt = "INSERT INTO owners (fname,lname) VALUES (%s, %s)"
cur = conn.cursor()
data = {
	"Bill":"Bidwill",
	"Arthur":"Blank",
	"Steve":"Bisciotti",
	"Kim":"Pergula",
	"Jerry":"Richardson",
	"Virginia":"McCaskey",
	"Mike":"Brown",
	"Jimmy":"Haslam",
	"Jerry":"Jones",
	"Pat":"Bowlen",
	"Martha":"Ford",
	"Green Bay":"Packers",
	"Robert C.":"McNair",
	"Jim":"Irsay",
	"Shahid":"Khan",
	"Clark":"Hunt",
	"Stan":"Kroenke",
	"Stephen":"Ross",
	"Zygi":"Wilf",
	"Robert":"Kraft",
	"Tom":"Benson",
	"John": "Mara",
	"Robert Wood":"Johnson IV",
	"Mark":"Davis",
	"Jeffery":"Lurie",
	"Dan":"Rooney",
	"Alex":"Spanos",
	"Jed":"York",
	"Paul":"Allen",
	"Bryan":"Glazer",
	"Amy Adams":"Strunk",
	"Dan":"Snyder"
}


for k,v in data.items():
	cur.execute(stmt,(k,v))

conn.commit()


cur.close()
conn.close()


