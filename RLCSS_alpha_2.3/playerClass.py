class PlayerClass:
    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.assists = 0
        self.saves = 0
        self.shots = 0
        self.wins = 0
        self.losses = 0

    #Setters
    def setName(self, name):
        self.name = name

    def setGoals(self, goals):
        self.goals = goals

    def setAssists(self, assists):
        self.assists = assists

    def setSaves(self, saves):
        self.saves = saves

    def setShots(self, shots):
        self.saves = shots

    def setWins(self, wins):
        self.wins = wins

    def setLosses(self, losses):
        self.losses = losses

    #Getters
    def getName(self, name):
        return self.name

    def getGoals(self, goals):
        return self.goals

    def getAssists(self, assists):
        return self.assists

    def getSaves(self, saves):
        return self.saves

    def getShots(self, shots):
        return self.shots

    def getWins(self, wins):
        return self.wins

    def getLosses(self, losses):
        return self.losses
