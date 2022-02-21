import pandas as pd

def matches_team(df, teamname):
    numbercounter = 0
    for i in range(len(df)):
        if df['HomeTeam'][i] == teamname  or df['AwayTeam'][i] == teamname:
            numbercounter = numbercounter + 1
            print('Match: ', numbercounter, ', Date: ', df['Date'][i], ', Teams: ', df['HomeTeam'][i], ' - ', df['AwayTeam'][i], ', Match scores: ', df['FTHG'][i], ' - ', df['FTAG'][i])
    if numbercounter == 0:
        print('This team name does not exist in data base or you made a mistake in the team name you entered.')

def matches_date(df, dateofthegame):
    numbercounter = 0
    for i in range(len(df)):
        if df['Date'][i] == dateofthegame:
            numbercounter = numbercounter + 1
            print('Match: ', numbercounter, ', Teams: ', df['HomeTeam'][i], ' - ', df['AwayTeam'][i], ', Match scores: ', df['FTHG'][i], ' - ', df['FTAG'][i])
    if numbercounter == 0:
        print('There were no matches on this day or you made a mistake in the date that you entered.')

def create_nameslist(df):
    nameslist = [df['HomeTeam'][0], df['AwayTeam'][0]]
    for i in range(1, len(df)):
        counter1 = 0
        counter2 = 0
        for j in range(len(nameslist)):
            if df['HomeTeam'][i] == nameslist[j]:
                counter1 = counter1 - 1
            if df['AwayTeam'][0] == nameslist[j]:
                counter2 = counter2 -1
        if counter1 == 0:
            nameslist.append(df['HomeTeam'][i])
        if counter2 == 0:
            nameslist.append(df['AwayTeam'][i])
    return nameslist

def create_gameslist(df, nameslist):
    gameslist = []
    for i in range(len(nameslist)):
        gamescounter = 0
        for j in range(len(df)):
            if df['HomeTeam'][j] == nameslist[i] or df['AwayTeam'][j] == nameslist[i]:
                gamescounter = gamescounter + 1
        gameslist.append(gamescounter)
    return gameslist

def create_goaldifference_list(df, nameslist):
    goaldifference = []
    for i in range(len(nameslist)):
        score = 0
        miss = 0
        goaldiffcounter = 0
        for j in range(len(df)):
            if df['HomeTeam'][j] == nameslist[i]:
                score = score + int(df['FTHG'][j])
                miss = miss + int(df['FTAG'][j])
            if df['AwayTeam'][j] == nameslist[i]:
                score = score + int(df['FTAG'][j])
                miss = miss + int(df['FTHG'][j])
        goaldiffcounter = score - miss
        goaldifference.append(goaldiffcounter)
    return goaldifference

def hthrecords_hthgoaldifference(df, speciallist, nameslist):
    for i in range(len(speciallist)-1):
        #Changing the special list according to head-to-head records
        currentpoint = speciallist[i]
        tieslist = []
        for j in range(i, len(speciallist)):
            if currentpoint == speciallist[j]:
                tieslist.append(j)
            if len(tieslist) > 1:
                for m in range(len(tieslist)-1):
                    for n in range(m+1,len(tieslist)):
                        for k in range(len(df)):
                            if df['HomeTeam'][k] == nameslist[tieslist[m]]  and df['AwayTeam'][k] == nameslist[tieslist[n]] and int(df['FTHG'][k]) > int(df['FTAG'][k]):
                                speciallist[tieslist[m]] = speciallist[tieslist[m]] + 3*(10**7)
                            if df['HomeTeam'][k] == nameslist[tieslist[m]]  and df['AwayTeam'][k] == nameslist[tieslist[n]] and int(df['FTHG'][k]) < int(df['FTAG'][k]):
                                speciallist[tieslist[n]] = speciallist[tieslist[m]] + 3*(10**7)
                            if df['HomeTeam'][k] == nameslist[tieslist[n]]  and df['AwayTeam'][k] == nameslist[tieslist[m]] and int(df['FTHG'][k]) > int(df['FTAG'][k]):
                                speciallist[tieslist[n]] = speciallist[tieslist[n]] + 3*(10**7)
                            if df['HomeTeam'][k] == nameslist[tieslist[n]]  and df['AwayTeam'][k] == nameslist[tieslist[m]] and int(df['FTHG'][k]) < int(df['FTAG'][k]):
                                speciallist[tieslist[m]] = speciallist[tieslist[m]] + 3*(10**7)
                            if df['HomeTeam'][k] == nameslist[tieslist[n]]  and df['AwayTeam'][k] == nameslist[tieslist[m]] and df['FTHG'][k] == df['FTAG'][k]:
                                speciallist[tieslist[m]] = speciallist[tieslist[m]] + 1*(10**7)
                                speciallist[tieslist[n]] = speciallist[tieslist[n]] + 1*(10**7)
            #Changing the special list according the goal difference of head-to-head games
            tieslist = []
            for j in range(i, len(speciallist)):
                if currentpoint == speciallist[j]:
                    tieslist.append(j)
            if len(tieslist) > 1:
                for m in range(len(tieslist)-1):
                    for n in range(m+1,len(tieslist)):
                        goalsA = 0 #Hypothetical team A
                        goalsB = 0 #Hypothetical team B
                        for k in range(len(df)):
                            if df['HomeTeam'][k] == nameslist[tieslist[m]] and df['AwayTeam'][k] == nameslist[tieslist[n]]:
                                goalsA = goalsA + int(df['FTHG'][k])
                                goalsB = goalsB + int(df['FTAG'][k])
                            if df['HomeTeam'][k] == nameslist[tieslist[n]] and df['AwayTeam'][k] == nameslist[tieslist[m]]:
                                goalsA = goalsA + int(df['FTAG'][k])
                                goalsB = goalsB + int(df['FTHG'][k])
                        goaldifferenceA = goalsA - goalsB
                        goaldifferenceB = goalsB - goalsA
                    speciallist[tieslist[m]] = speciallist[tieslist[m]] + goaldifferenceA*(10**5)
                    speciallist[tieslist[n]] = speciallist[tieslist[n]] + goaldifferenceB*(10**5)
        return speciallist
    
def overall_goaldifference_goalsscored(df, speciallist, nameslist, goaldifference):
    for i in range(len(speciallist)-1):
        #Changing the special list according to the goal difference overall
        currentpoint = speciallist[i]
        tieslist = []
        for j in range(i, len(speciallist)):
            if currentpoint == speciallist[j]:
                tieslist.append(j)
        if len(tieslist) > 1:
            for m in range(len(tieslist)):
                speciallist[tieslist[m]] = speciallist[tieslist[m]] + goaldifference[tieslist[m]]*100
        #Changing the speciallist according to the overall number of goals scored
        tieslist = []
        for j in range(i, len(speciallist)):
            if currentpoint == speciallist[j]:
                tieslist.append(j)
        if len(tieslist) > 1:
            for m in range(len(tieslist)):
                goalscorecounter = 0
                for k in range(len(df)):
                    if df['HomeTeam'][k] == nameslist[tieslist[m]]:
                        goalscorecounter = goalscorecounter + int(df['FTHG'][k])
                    if df['AwayTeam'][k] == nameslist[tieslist[m]]:
                        goalscorecounter = goalscorecounter + int(df['FTAG'][k])
                speciallist[tieslist[m]] = speciallist[tieslist[m]] + goalscorecounter
    return speciallist

def create_rankinglist(df, speciallist, nameslist):
    #Turning the special list into the list of ranks by saying that the team with higher special score has higher rank
    rank = 1
    while rank <= len(nameslist):
        maxinspeciallist = speciallist[0]
        plusrank = 0
        for i in range(len(nameslist)):
            if speciallist[i] > maxinspeciallist:
                maxinspeciallist = speciallist[i]
        for j in range(len(nameslist)):
            if speciallist[j] == maxinspeciallist:
                plusrank = plusrank + 1 #In case some teams still have the same rank
                speciallist[j] = rank
        rank = rank + plusrank
    return speciallist

def arranging_by_ranks(df_ranking_table):
    #Putting the teams in the ranking tables in the correct positions according to their ranks
    for i in range(1, len(df_ranking_table) + 1):
        for j in range(len(df_ranking_table)):
            if df_ranking_table['Rank'][j] == i and j+1 != i:
                extrateamname = df_ranking_table['Team Name'][i-1]
                extrarank = df_ranking_table['Rank'][i-1]
                extranumberofgames = df_ranking_table['Number of games'][i-1]
                extranumberofwins = df_ranking_table['Number of wins'][i-1]
                extranumberofdraws = df_ranking_table['Number of draws'][i-1]
                extranumberoflosses = df_ranking_table['Number of losses'][i-1]
                extragoaldifference = df_ranking_table['Goal difference'][i-1]
                extrapoints = df_ranking_table['Points'][i-1]
                df_ranking_table['Team Name'][i-1] = df_ranking_table['Team Name'][j]
                df_ranking_table['Rank'][i-1] = i
                df_ranking_table['Number of games'][i-1] = df_ranking_table['Number of games'][j]
                df_ranking_table['Number of wins'][i-1] = df_ranking_table['Number of wins'][j]
                df_ranking_table['Number of draws'][i-1] = df_ranking_table['Number of draws'][j]
                df_ranking_table['Number of losses'][i-1] = df_ranking_table['Number of losses'][j]
                df_ranking_table['Goal difference'][i-1] = df_ranking_table['Goal difference'][j]
                df_ranking_table['Points'][i-1] = df_ranking_table['Points'][j] 
                df_ranking_table['Team Name'][j] = extrateamname
                df_ranking_table['Rank'][j] = extrarank
                df_ranking_table['Number of games'][j] = extranumberofgames
                df_ranking_table['Number of wins'][j] = extranumberofwins
                df_ranking_table['Number of draws'][j] = extranumberofdraws
                df_ranking_table['Number of losses'][j] = extranumberoflosses
                df_ranking_table['Goal difference'][j] = extragoaldifference 
                df_ranking_table['Points'][j] = extrapoints
    return df_ranking_table


print('If you want to know informationt about English Footall League 2013/2014, enter eng2013.')
print('If you want to know informationt about English Footall League 2017/2018, enter eng2017.')
print('If you want to know informationt about Italian Footall League 2017/2018, enter itl2017.')
print('Enter your option:')
menuoption1 = str(input())
if menuoption1 == 'eng2017' or menuoption1 == 'eng2013' or menuoption1 == 'itl2017':
    if menuoption1 == 'eng2013':
        df = pd.read_csv('englishleague2013.csv', sep=',')
    if menuoption1 == 'eng2017':
        df = pd.read_csv('englishleague2017.csv', sep=',')
    if menuoption1 == 'itl2017':
        df = pd.read_csv('italianleague2017.csv', sep=',')
    print('To see all matches of a given team, enter 1')
    print('To see all matches matches played on a given date, enter 2')
    print('To see the ranking table, enter 3')
    print('Enter your option:')
    menuoption2 = int(input())
    #See all the matches of the given team    
    if menuoption2 == 1:
        if menuoption1 == 'eng2013' or menuoption1 == 'eng2017':
            print('Enter the name of the team (example: Arsenal): ')
        else:
            print('Enter the name of the team (example: Roma): ')
        teamname = str(input())
        matches_team(df, teamname)
    #See all the matches played on the given date
    elif menuoption2 == 2:
        if menuoption1 == 'eng2013':
            print('Enter the date (example: 25/08/13): ')
        elif menuoption1 == 'eng2017':
            print('Enter the date (example: 19/08/2017): ')
        else:
            print('Enter the date (example: 19/08/17): ')
        dateofthegame = str(input())
        matches_date(df, dateofthegame)
    #See the ranking table
    elif menuoption2 == 3:
        #Searching for all the team names and creting a list out of them
        nameslist = create_nameslist(df)
        #Counting the amount of games each team played and putting it in the list in the order of team names
        gameslist = create_gameslist(df, nameslist)
        #Counting all the wins, draws and losses of the each team and putting them in the lists in the order of theam names
        #Counting the points according to the system (3 points for the win, 1 point for the draw, 0 points for the loss) and putting them in the list in the order of theam names
        winslist = []
        drawslist = []
        losseslist = []
        pointslist = []
        for i in range(len(nameslist)):
            winscounter = 0
            drawscounter = 0
            lossescounter = 0
            pointscounter = 0
            for j in range(len(df)):
                if (df['HomeTeam'][j] == nameslist[i] and int(df['FTHG'][j]) > int(df['FTAG'][j])) or (df['AwayTeam'][j] == nameslist[i] and int(df['FTHG'][j]) < int(df['FTAG'][j])):
                    winscounter = winscounter + 1
                    pointscounter = pointscounter + 3
                if (df['HomeTeam'][j] == nameslist[i] and int(df['FTHG'][j]) < int(df['FTAG'][j])) or (df['AwayTeam'][j] == nameslist[i] and int(df['FTHG'][j]) > int(df['FTAG'][j])):
                    lossescounter = lossescounter + 1
                if (df['AwayTeam'][j] == nameslist[i] or df['HomeTeam'][j] == nameslist[i]) and df['FTHG'][j] == df['FTAG'][j]:
                    drawscounter = drawscounter + 1
                    pointscounter = pointscounter + 1
            winslist.append(winscounter)
            drawslist.append(drawscounter)
            losseslist.append(lossescounter)
            pointslist.append(pointscounter)
        #Counting the goal difference and putting it in the list in the order of theam names
        goaldifference = create_goaldifference_list(df, nameslist)
        #Creating special list that is used to defined the ranking positions
        speciallist = []
        #English League uses 2-level system of breaking the ties, so in the begining special list for EL contains points of the each team * 100000 
        if menuoption1 == 'eng2017' or menuoption1 == 'eng2013':
            for i in range(len(pointslist)):
                speciallist.append(pointslist[i]*100000)
        #Italian League uses 4-level system of breaking the ties, so in the begining special list for IL contains points of the each team * 10^10 
        else:
            for i in range(len(pointslist)):
                speciallist.append(pointslist[i]*(10**10))
            speciallist = hthrecords_hthgoaldifference(df, speciallist, nameslist)
        speciallist = overall_goaldifference_goalsscored(df, speciallist, nameslist, goaldifference)
        rankinglist = create_rankinglist(df, speciallist, nameslist)
        #Creating ranking table
        ranking_table = [{'Team Name':nameslist[i], 'Rank':rankinglist[i], 'Number of games':gameslist[i], 'Number of wins':winslist[i], 'Number of draws':drawslist[i], 'Number of losses':losseslist[i], 'Goal difference':goaldifference[i], 'Points':pointslist[i]} for i in range(20)]  
        df_ranking_table = pd.DataFrame(ranking_table)
        print(arranging_by_ranks(df_ranking_table))
    
    else:
        print('This option does not exist. Please restart the program.')
    
else:
    print('This option does not exist. Please restart the program.')