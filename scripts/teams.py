import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO Teams (team_id, team_name, location, owner_id, league_id, Coaches_coach_id) VALUES (%s, %s, %s, %s, %s, %s)"


    teams = csv.reader(open('csv/teams.csv'))
    records = csv.reader(open('csv/team_record.csv'))
    coaches = csv.reader(open('csv/coaches.csv'))

    teamsList = list(teams)
    recordList = list(records)
    coachList = list(coaches)

    # Delete top layer
    teamsList.remove(teamsList[0])
    recordList.remove(recordList[0])
    coachList.remove(coachList[0])



    for recordLine in recordList:

        teamLocation, teamName = splitName(recordLine[1])

        team_id = 1
        for coachLine in coachList:
            tempLocation, tempName = splitName(coachLine[2])
            if teamName == tempName:
                break
            team_id = team_id + 1

        coach_id = team_id
        owner_id = team_id
        league_id = getLeagueId(recordLine[2], recordLine[3])


        teamData = (int(team_id), teamName, teamLocation, int(owner_id), int(league_id), int(coach_id))
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

def getLeagueId(conf, div):
    leagueList = [
      ('AFC East'),
      ('AFC North'),
      ('AFC South'),
      ('AFC West'),
      ('NFC East'),
      ('NFC North'),
      ('NFC South'),
      ('NFC West'),

    ]
    league_id = 1
    for league in leagueList:
        league= league.split()

        if(league[0] == conf and league[1][0] == div[2]):
            return league_id
        league_id = league_id + 1

    return None

if __name__ == '__main__':
    main()
