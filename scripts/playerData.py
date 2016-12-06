import pymysql
import csv

def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command



    players = csv.reader(open('csv/Players.csv'))
    owners = csv.reader(open('csv/owners.csv'))
    offensivePlayers = csv.reader(open('csv/offensivePlayers.csv'))
    defensivePlayers = csv.reader(open('csv/defensivePlayers.csv'))
    kickers = csv.reader(open('csv/kickers.csv'))

    playersList = list(players)
    ownersList = list(owners)
    offensivePlayersList = list(offensivePlayers)
    defensivePlayersList = list(defensivePlayers)
    kickersList = list(kickers)

    # Delete top layer
    playersList.remove(playersList[0])
    ownersList.remove(ownersList[0])
    offensivePlayersList.remove(offensivePlayersList[0])
    defensivePlayersList.remove(defensivePlayersList[0])
    kickersList.remove(kickersList[0])

    season_id = 2016

    stmt = "INSERT INTO off_performance (player_id, season_id, passing_yds, passing_td, interceptions, rush_atts, rush_yds, rush_td, receiving_atts, receiving_yds, receiving_td) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


    for offensiveLine in offensivePlayersList:

        fullName = offensiveLine[1]
        player_id = getPlayerId(fullName, playersList)

        #"url","Name","passing","pass_td","int","rush_att","rush_yd","rush_td","rec_att","rec_yds","rec_td"

        pass_yd = offensiveLine[2]
        pass_td = offensiveLine[3]
        interception = offensiveLine[4]
        rush_att = offensiveLine[5]
        rush_yd = offensiveLine[6]
        rush_td = offensiveLine[7]
        rec_att = offensiveLine[8]
        rec_yds = offensiveLine[9]
        rec_td = offensiveLine[10]

        playerData = (player_id, season_id, pass_yd, pass_td, interception, rush_att, rush_yd, rush_td, rec_att, rec_yds, rec_td)




        # execute command for each line of data
        #if player_id != None:
            #cur.execute(stmt, playerData)

#"url","name","tackles","assist","sack","pd","int","force_fumble","fumble_recover"

    stmt = "INSERT INTO def_performance (player_id, season_id, tackles, assist, sacks, interceptions, forced_fumbles, recover_fumbles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    for defensiveLine in defensivePlayersList:
        name = defensiveLine[1]
        player_id = getPlayerId(name, playersList)

        tackles = defensiveLine[2]
        assist = defensiveLine[3]
        sacks = defensiveLine[4]
        interceptions = defensiveLine[6]
        forced_fumble = defensiveLine[7]
        recover_fumble = defensiveLine[8]


        playerData = (player_id, season_id, tackles, assist, sacks, interceptions, forced_fumble, recover_fumble)

        #if player_id != None:
            #cur.execute(stmt, playerData)

    stmt = "INSERT INTO kicker_performance (player_id, season_id, field_goal_att, field_goal_made) VALUES (%s, %s, %s, %s)"

    for kickerLine in kickersList:
        name = kickerLine[1]
        player_id = getPlayerId(name, playersList)

        fga = kickerLine[2]
        fgm = kickerLine[3]


        playerData = (player_id, season_id, fga, fgm)

        if player_id != None:
            cur.execute(stmt, playerData)


    #for line in positions:
        #print line

    # save
    conn.commit()

    # close
    cur.close()
    conn.close()



def splitNameWithoutCommas(name):

    temp = name.split()
    if len(temp) != 2:
        #print "not = 2"

        return ((temp[0]), (temp[1] + ' ' + temp[2]))

    else:
        temp[0] = temp[0].replace(',', '')

        return (temp[0], temp[1])

def splitNameWithCommas(name):

    temp = name.split()
    if(temp[0] == "Robert"):
        print temp
    if len(temp) != 2:
        #print "not = 2"
        if ',' in temp[0]:
            #print 'commma in temp[0]', temp

            temp[0] = temp[0].replace(',', '')
            return ((temp[1] + ' ' +temp[2]), (temp[0]))

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

def getPlayerId(name, playersList):
    player_id = 1
    for playerLine in playersList:
        lname, fname = splitNameWithCommas(playerLine[1])
        tempName = fname + ' ' + lname

        if name.lower() == tempName.lower():
            break
        player_id = player_id + 1

    if player_id >= 2302:
        print 'error player name not found'
        return None
    return player_id


def getTeamId(name):

    return None
if __name__ == '__main__':
    main()
