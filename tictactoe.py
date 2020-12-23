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
#gameRows = 3
#gameColumns = 3

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
        return int(turnCellValue)

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
        return int(0)

    def IsHumanControlled(self):
        return False

############################
# Tic Tac Toe Game Manager
############################
class TTTGameManager:
    def __init__(self, rows, columns):
        self.gameRows = rows
        self.gameColumns = columns
        self.boardValues = [[' ' for colums in range(self.gameRows)] for rows in range(self.gameColumns)]
        self.boardValuesLegend = [[0 for colums in range(self.gameRows)] for rows in range(self.gameColumns)]
        self.Players = []

        self.FillBoardLegend()
        random.seed()               # Seed randomness 

        self.currentPlayerIndex = 0

    ###
    ## Fill legend, with numbers corresponding to grid cells.
    def FillBoardLegend(self):
        count = 0
        for row in range(len(self.boardValuesLegend)) :
            for column in range(len(self.boardValuesLegend[row])) :
                self.boardValuesLegend[row][column] = count
                count = count + 1

    #######################
    # Draw The Game Board 
    #######################
    def DrawBoard(self, dataValues):
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

    # Add Player
    def AddHumanPlayer(self, name, character):
        self.Players.append(Player(name, character))

    # Add CPU Player
    def AddAIPlayer(self, name, character):
        self.Players.append(AIPlayer(name, character))

    # Run Turn
    def RunTurn(self):
        turnCellIndex = self.Players[self.currentPlayerIndex].RunTurn()

        bIsValidCellNumber = self.Validate(turnCellIndex)

        if bIsValidCellNumber == True :
            print("Valid choice!")
            self.UpdateCell(turnCellIndex, self.Players[self.currentPlayerIndex].character)
        else :
            print("Error invalid cell choice!")

    # Choose next player
    def NextTurn(self):
        nextTurnPlayerIndex = self.currentPlayerIndex + 1
        if nextTurnPlayerIndex > (len(self.Players)-1):
            nextTurnPlayerIndex = 0

        self.currentPlayerIndex = nextTurnPlayerIndex

    # How many cells are still left on the board
    def NumOpenCells(self):
        count = 0
        for row in range(len(self.boardValues)) :
            for column in range(len(self.boardValues[row])) :
                value = self.boardValues[row][column]
                if value == ' ':
                    count += 1

        return count

    # Validate value
    def Validate(self, cellIndex):
        # Make sure it is a valid cell 
        # Also make sure it's not taken alraedy.
        cellRow, cellColumn = self.GetCellLocation(cellIndex)

        bIsValidCell = False

        if cellRow >=0 and cellColumn >= 0 :
            cellValue = self.boardValues[cellRow][cellColumn]
            if cellValue == ' ' :
                bIsValidCell = True

        return bIsValidCell

    # Convert cell index into row, column
    def GetCellLocation(self, cellIndex) :
        boardRow = -1
        boardColumn = -1

        for row in range(len(self.boardValuesLegend)) :
            for column in range(len(self.boardValuesLegend[row])) :
                value = self.boardValuesLegend[row][column]

                if value == cellIndex :
                    boardRow = row
                    boardColumn = column
                    return boardRow, boardColumn

        return boardRow, boardColumn
    # Update cell on board.
    def UpdateCell(self, cellIndex, cellValue) :
        cellRow, cellColumn = self.GetCellLocation(cellIndex)

        if self.Validate(cellIndex) == True :
            self.boardValues[cellRow][cellColumn] = cellValue

    # Draw board and legend
    def DrawBoardAndLegend(self):
        print("---------------Legend-----------------------")
        self.DrawBoard(self.boardValuesLegend)
        print("--------------------------------------------")
        print("---------------GAME BOARD-------------------")
        print("--------------------------------------------")
        self.DrawBoard(self.boardValues)

    def RunGame(self):
        print("---------->>>Welcome to Jacksquatch Tic-Tac-Toe<<<----------")
        self.DrawBoardAndLegend()

        # Choose random player to start.
        self.currentPlayerIndex = random.randint(0, len(self.Players)-1)
        print(self.Players[self.currentPlayerIndex].name + " is up first.")

        t = 0
        while t < 2:
            self.RunTurn()
            self.NextTurn()
            self.DrawBoardAndLegend()
            t += 1

########################
# Main Game Function...
########################
def Run() :
    gameManager = TTTGameManager(3,3)
    gameManager.AddHumanPlayer("Jack", "X")
    gameManager.AddAIPlayer("Moron Computer", "O")
    gameManager.RunGame()

################
# Run the game.
################
Run()
