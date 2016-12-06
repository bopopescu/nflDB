import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO Players (fname, lname, team_id, position_id) VALUES (%s, %s, %s, %s)"


    players = csv.reader(open('csv/Players.csv'))
    owners = csv.reader(open('csv/owners.csv'))

    playersList = list(players)
    ownersList = list(owners)

    # Delete top layer
    playersList.remove(playersList[0])
    ownersList.remove(ownersList[0])


    for playerLine in playersList:

        lname,fname = splitName(playerLine[1])
        teamLocation, teamName = splitTeamName(playerLine[3])
        position_id = playerLine[2]

        team_id = 1
        for ownerLine in ownersList:
            tempLocation, tempName = splitTeamName(ownerLine[2])
            if teamName == tempName:
                break
            team_id = team_id + 1

        if '/' in position_id:
            position = position_id.split('/')
            position = position[0]
            position_id = position

        #if position_id not in positions:
        #    positions.append(position_id)

        teamData = (fname, lname, team_id, position_id)


        # execute command for each line of data
        #cur.execute(stmt, teamData)


    #for line in positions:
        #print line

    # save
    #conn.commit()

    # close
    cur.close()
    conn.close()



def splitName(name):

    temp = name.split()
    if len(temp) != 2:
        #print "not = 2"
        if ',' in temp[0]:
            #print 'commma in temp[0]', temp
            temp[0] = temp[0].replace(',', '')

            return ((temp[1] + ' ' +temp[0]), (temp[1]))

            return temp[1] + temp[2] + temp[0]
        elif ',' in temp[1]:
            #print 'commma in temp[1]',  temp
            temp[1] = temp[1].replace(',', '')

            return ((temp[2]), (temp[0] + ' ' + temp[1]))
        else:
            'did not work'
            return None
    else:
        temp[0] = temp[0].replace(',', '')

        return (temp[0], temp[1])

def splitTeamName(name):
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
