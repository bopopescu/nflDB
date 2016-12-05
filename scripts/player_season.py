import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO player_season (player_id, season_id) VALUES (%s, %s)"

    for player_id in range(1,2302):

        for season_id in range(2007,2017):

            data = [player_id, season_id]

            # execute command for each line of data
            cur.execute(stmt, data)

    # save
    conn.commit()

    # close
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
