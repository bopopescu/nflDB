import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO team_season_performance (season_id, team_id, wins, losses, ties, home, road, points_for, points_against, touchdowns) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


    records = csv.reader(open('csv/Team_Record_2007-2016.csv'))
    owners = csv.reader(open('csv/owners.csv'))

    recordList = list(records)
    ownersList = list(owners)

    # Delete top layer
    recordList.remove(recordList[0])
    ownersList.remove(ownersList[0])


    season_id = 2006
    teamNumber = 0
    for recordLine in recordList:
        if teamNumber % 32 == 0:
            season_id = season_id + 1

        teamLocation, teamName = splitName(recordLine[1])

        team_id = 1
        for ownerLine in ownersList:
            tempLocation, tempName = splitName(ownerLine[2])
            if teamName == tempName:
                break
            team_id = team_id + 1


        #"url","Team","Wins","Losses","Tie","Points For","Points Against","Touchdowns","Home","Road"

        wins = recordLine[2]
        losses = recordLine[3]
        ties = recordLine[4]
        points_for = recordLine[5]
        points_against = recordLine[6]
        touchdowns = recordLine[7]
        home = recordLine[8]
        road = recordLine[9]
        teamData = (season_id, team_id, wins, losses, ties, home, road, points_for, points_against, touchdowns)

        print teamData

        # execute command for each line of data
        cur.execute(stmt, teamData)
        teamNumber = teamNumber + 1

    # save
    conn.commit()

    # close
    cur.close()
    conn.close()



def splitName(name):
    temp = name.split()
    if len(temp) > 2:
        teamLocation = temp[0] + ' ' + temp[1]
        teamName = temp[2]
        return (teamLocation, teamName)

    elif len(temp) > 1:
        teamLocation = temp[0]
        teamName = temp[1]
        return (teamLocation, teamName)
    return None


if __name__ == '__main__':
    main()
