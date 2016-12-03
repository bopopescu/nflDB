import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "nflDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO team_record (wins, loses, season, team_id) VALUES (%s, %s, %s, %s)"


    records = csv.reader(open('csv/team_record.csv'))
    owners = csv.reader(open('csv/owners.csv'))

    recordList = list(records)
    ownersList = list(owners)

    # Delete top layer
    recordList.remove(recordList[0])
    ownersList.remove(ownersList[0])



    for recordLine in recordList:

        teamLocation, teamName = splitName(recordLine[1])

        team_id = 1
        for ownerLine in ownersList:
            tempLocation, tempName = splitName(ownerLine[2])
            if teamName == tempName:
                break
            team_id = team_id + 1

        wins = recordLine[4]
        losses = recordLine[5]
        teamData = (wins, losses, 2016, team_id)

        # execute command for each line of data
        cur.execute(stmt, teamData)


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
