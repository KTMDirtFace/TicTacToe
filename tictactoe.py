import random

################################################
################################################
#Tic Tac Toe - THE GAME
################################################
################################################

##############
# Game Config stuff, should be in data or data file somewhere so its not hardcoded
##############
gameErrorStringGeneric = "...[ERROR] Go take a dump!..."
gameNumHumanPlayers = 1
gameNumAIPlayers = 1
gameRows = 3
gameColumns = 3

############################
# Tic Tac Toe Game Manager
############################
#class TTTGameManager:

###############
# Player Class
###############
class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def RunTurn(self):
        #print("PlayerTurn")
        turnCellValue = input("Its your turn enter cell:")
        print("Turn Value is: " + str(turnCellValue))

    def IsHumanControlled(self):
        return True

##################
# AI Player Class
##################
class AIPlayer(Player):
    #pass    # pass makes it so no other properties or methods are added to the class
    def __init__(self, name, character):
        super().__init__(name, character)

    def RunTurn(self):
        print("AITurn")

    def IsHumanControlled(self):
        return False

##########################
# Game Data - global barf
##########################
playerCharacter = [ 'X', 'O']
players = [ "Jack", "Moron Computer" ]
#print(playerCharacter)
# Where all the game X and O's live.
boardValues = [[' ' for colums in range(gameRows)] for rows in range(gameColumns)]
boardValuesLegend = [[0 for colums in range(gameRows)] for rows in range(gameColumns)]

#########################
# Fill Board Legend 
#########################
def FillBoardLegend():
    count = 0
    for row in range(len(boardValuesLegend)) :
        for column in range(len(boardValuesLegend[row])) :
            boardValuesLegend[row][column] = str(count)
            count = count + 1
    #print(boardValuesLegend)

#######################
# Draw The Game Board 
#######################
def DrawBoard(dataValues):
#    for row in range(len(dataValues)) :
#        for column in range(len(dataValues[row])) :
#            print(dataValues[row][column])

    numRows         = len(dataValues)
    numColumns      = len(dataValues[0])
    #print("NumRows: " + str(numRows) + " NumColums: " + str(numColumns))

    cellSize        = 3 # number of characters in a cell ex. " X " two spaces and a character.
    cellCharIndex   = 1
    numCharsInRow   = numColumns*cellSize + (numColumns-1)
    
    ############################################
    # Build the horizonal separator between rows
    horizontalSeparator = []
    for chars in range(numCharsInRow):
        horizontalSeparator.append("-")

    horizontalSeparatorAsString = "".join(horizontalSeparator)

    #################
    # Build the rows
    for row in range(numRows):
        currentRow = []
        for column in range(numColumns):
            cellValue = dataValues[row][column]
            #print(cellValue)
            for cell in range(cellSize):
                if cell != 1:
                    currentRow.append(' ')
                else:
                    currentRow.append(str(cellValue))
            
            # finish it off with a |
            bIsLastColum = (column == numColumns-1)
            if bIsLastColum != True:
                currentRow.append('|')
        
        rowAsString = "".join(currentRow)
        print(rowAsString)

        bIsLastRow = (row == numRows-1)
        if bIsLastRow != True:
            print(horizontalSeparatorAsString)

######################
## MORON COMPUTER AI
######################
#def PerformComptuerTerm():
    # for now choose a random ass cell
    # find empty cells

######################################
# Draw the game legend and the board.
######################################
def DrawLegendAndBoard():
    print("---------------Legend-----------------------")
    DrawBoard(boardValuesLegend)
    print("--------------------------------------------")
    print("---------------GAME BOARD-------------------")
    print("--------------------------------------------")
    DrawBoard(boardValues)

#######
# Init
#######
def Init() :
    print("---------->>>Welcome to Jacksquatch Tic-Tac-Toe<<<----------")

    FillBoardLegend()           # Fill legend with data.
    random.seed()               # Seed randomness 

########################
# Main Game Function...
########################
def Run() :
    Init()
    #Choose random player to start.
    firstPlayerIndex = random.randint(0, len(players)-1)
    firstPlayer = players[firstPlayerIndex]

    #First player is always X?
    firstPlayerCharacter = playerCharacter[0]

    print("Player1: " + firstPlayer)
    print(firstPlayer + " Character: " + firstPlayerCharacter)

    DrawLegendAndBoard()


    print("")
    p1 = Player("Jack", 'X')
    p1.RunTurn()

################
# Run the game.
################
Run()
