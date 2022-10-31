#Rocket League Career Simulator
#Game Simulator

import random

#Global variables
totalGames = 0
highestScore = 0
overTimeGames = 0
team1Wins = 0
team2Wins = 0


def rollD6():
    roll = random.randrange(0, 6, 1)
    return roll

def flipCoin():
    roll = random.randrange(0, 2, 1)
    return roll

def rollGoals(team):

    roll = rollD6()
    if roll == 5:
        bonusRoll = rollD6()
        while bonusRoll == 5:
            roll = roll + 1
            bonusRoll = rollD6()

    return roll

def gameSim(team1, team2, isFavored):
    global totalGames
    global highestScore
    global overTimeGames
    global team1Wins
    global team2Wins

    favored = isFavored
    overTime = False

    #Rolls amount of goals for each team
    if favored == False:
        team1Goals = rollGoals(team1)
        team2Goals = rollGoals(team2)
    elif favored == True:
        team1Roll1 = rollGoals(team1)
        team1Roll2 = rollGoals(team1)
        if team1Roll1 > team1Roll2:
            team1Goals = team1Roll1
        else:
            team1Goals = team1Roll2
        team2Goals = rollGoals(team2)
        
    #Check for Overtime
    if team1Goals == team2Goals:
        overTime = True
        overTimeGoal = flipCoin()
        overTimeGames = overTimeGames + 1
        if overTimeGoal == 0:
            team1Goals = team1Goals + 1
        elif overTimeGoal == 1:
            team2Goals = team2Goals + 1

    #Print result is team 1 wins
    if team1Goals > team2Goals:
        if overTime == True:
            print(team1," Wins in Overtime!")
        elif overTime == False:
            print(team1," Wins!")
        print(team1,": ", team1Goals)
        print(team2,": ", team2Goals)
        team1Wins = team1Wins + 1

        if team1Goals > highestScore:
            highestScore = team1Goals

    #Print results if team 2 wins
    if team1Goals < team2Goals:
        if overTime == True:
            print(team2," Wins in Overtime!")
        elif overTime == False:
            print(team2," Wins!")
        print(team2,": ", team2Goals)
        print(team1,": ", team1Goals)
        team2Wins = team2Wins + 1

        if team2Goals > highestScore:
            highestScore = team1Goals

    totalGames = totalGames + 1

def randomizeTeams(teams):
    random.shuffle(teams)
    return teams

def printTeams(teams1, teams2):
    teams = teams1 + teams2
    print(teams)

def create_balanced_round_robin(players):

    #Randomize list of teams sent in
    players = randomizeTeams(players)
    
    """ Create a schedule for the players in the list and return it"""
    s = []
    if len(players) % 2 == 1: players = players + [None]
    # manipulate map (array of indexes for list) instead of list itself
    # this takes advantage of even/odd indexes to determine home vs. away
    n = len(players)
    map = list(range(n))
    mid = n // 2
    for i in range(n-1):
        l1 = map[:mid]
        l2 = map[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = players[l1[j]]
            t2 = players[l2[j]]
            if j == 0 and i % 2 == 1:
                # flip the first match only, every other round
                # (this is because the first match always involves the last player in the list)
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        #randomize each week as its added to the schedule
        s.insert(random.randrange(len(s)+1), round)

        # rotate list by n/2, leaving last element at the end
        map = map[mid:-1] + map[:mid] + map[-1:]
        
    return s

def printSchedule(schedule):
    sLength = len(schedule)
    rLength = len(schedule[0])
    print("SCHEDULE\n**********************")
    for i in range(sLength):
        print("Week:", i + 1)
        for j in range(rLength):
            game = ("{} {}".format(schedule[i][j][0],schedule[i][j][1]))
            print(game)
        print()

def printScheduleExcel(schedule):
    sLength = len(schedule)
    rLength = len(schedule[0])
    print("SCHEDULE\n**********************")
    for i in range(sLength):
        print("Week:", i + 1)
        for j in range(rLength):
            game = ("{} 0 {}".format(schedule[i][j][0], schedule[i][j][1]))
            print(game)


def main():

    eastTeams = ["Bombers","Comets","Cyclones","Express","Guardians","Mammoths","Monarchs","Ravagers","Rebels","Rovers","Seekers"]
    westTeams = ["Baracudas","Bears","Crusadors","Destroyers","Dragons","Pharos","Predators","Reapers","Scorpians","Sky Hawks","Wolves"]


    while True:
        print("Press 1 to simulate a close game")
        print("Press 2 to simulate a game favored for Team 1")
        print("Press 3 to generate East Division Round Robin")
        print("Press 4 to generate West Division round robin")
        print("Press 5 to print teams")
        print("Press 0 to stop")
        userInput = input()
        print(userInput)

        if userInput == "1":
            print("---------------")
            gameSim("Team 1", "Team 2", False)
            print("---------------")
            print()
        elif userInput == "2":
            print("---------------")
            gameSim("Team 1*", "Team 2", True)
            print("---------------")
            print()
        elif userInput == "3":
            print("---------------")
            print("Create Round Robin for East Division\n")
            schedule = create_balanced_round_robin(eastTeams)
            printSchedule(schedule)
            printScheduleExcel(schedule)
            print("---------------")
            print()
        elif userInput == "4":
            print("---------------")
            print("Create Round Robin for West Division\n")
            schedule = create_balanced_round_robin(westTeams)
            printSchedule(schedule)
            printScheduleExcel(schedule)
            print("---------------")
            print()
        elif userInput == "5":
            print("---------------")
            print("Print Teams\n")
            teams = printTeams(eastTeams, westTeams)
            print("---------------")
            print()

        elif userInput == "0":
            break
        
    print("end of loop")
        
    print("Total Games: ", totalGames)
    print("Highest Score: ", highestScore)
    print("Over Time Games: ", overTimeGames)
    print("Team 1 Wins: ", team1Wins)
    print("Team 2 Wins: ", team2Wins)


main()



# ~%16.9 chance of going overtime, based on 2000 game test
