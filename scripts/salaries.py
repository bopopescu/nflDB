import pymysql
import csv
import re
def main():
    # connect to db
    conn = pymysql.connect(host = "ix.cs.uoregon.edu", port = 3637, user = "modere", password = "michaelodere1", db = "NFLDB")

    # get cursor
    cur = conn.cursor()

    # create command
    stmt = "INSERT INTO salaries (amount, player_id) VALUES (%s, %s)"


    players = csv.reader(open('csv/Players.csv'))
    salary = csv.reader(open('csv/salaries.csv'))

    playersList = list(players)
    salaryList = list(salary)

    # Delete top layer
    playersList.remove(playersList[0])

    countNoMatch = 0
    countMatch = 0
    for salaryLine in salaryList:

        name, trash = salaryLine[1].split('\\')
        salary = salaryLine[4]
        salary = salary.strip('$')
        player_id = 1
        for playerLine in playersList:
            lastname, firstname = splitStripName(playerLine[1])
            tempName = firstname + lastname
            #name = name.strip(' \t\n\r')
            #tempName = tempName.strip(' \t\n\r')
            tempName = re.sub('[\s+]', '', tempName)

            name = re.sub('[\s+]', '', name)
            if tempName.lower() == name.lower():
                break
            #print tempName

            player_id = player_id + 1

        if player_id == 2302:
            print name, tempName
        else:
            teamData = (salary, player_id)
            print teamData

            # execute command for each line of data
            cur.execute(stmt, teamData)


    #for line in positions:
        #print line

    # save
    conn.commit()

    # close
    cur.close()
    conn.close()

def splitStripName(name):

    temp = name.split()
    if len(temp) != 2:
        #print "not = 2"
        if ',' in temp[0]:
            #print 'commma in temp[0]', temp
            temp[0] = temp[0].replace(',', '')
            return ((temp[1] + ' ' +temp[2]), (temp[0]))

            return temp[1] + temp[2] + temp[0]
        elif ',' in temp[1]:
            #print 'commma in temp[1]',  temp
            temp[1] = temp[1].replace(',', '')
            return (temp[2], temp[0])
        else:
            'did not work'
            return None
    else:
        temp[0] = temp[0].replace(',', '')

        return (temp[0], temp[1])


if __name__ == '__main__':
    main()
