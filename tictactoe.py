import random
from os import system, name

def screen_clear() :
    # for Windows
    if name == 'nt' :
        _ = system('cls')
    # for mac/linux
    else :
        _ = system('clear')

################################################
################################################
#Tic Tac Toe - THE GAME
################################################
################################################

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
        # For now make the AI Dumb as hell and just choose a random cell that is not occupied.
        # create a function in the game manager to return an array of open cell ID's ( from the legend )
        emptyCells = gameManager.GetEmptyCells()
        numEmptyCells = len(emptyCells)
        randomCellIndex = random.randint(0, numEmptyCells-1)
        randomCellVal = emptyCells[randomCellIndex]
        print("Its the AI's turn, they chose cell: " + str(randomCellVal))

        return int(randomCellVal)

    def IsHumanControlled(self):
        return False

############################
# Tic Tac Toe Game Manager
############################
class TTTGameManager:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.gameRows = boardSize
        self.gameColumns = boardSize
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

    # Get a list of empty cells
    def GetEmptyCells(self) :
        emptyCellIds = []

        count = 0
        for row in range(len(self.boardValues)) :
            for column in range(len(self.boardValues[row])) :
                value = self.boardValues[row][column]
                if value == ' ' :
                    emptyCellIds.append(int(count))
                count += 1

        print(emptyCellIds)

        return emptyCellIds

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

    # Check for winner or tie.
    def CheckForWin(self):
        print("Checking for win.")
        # Does python have enums?
        # for now -1 = no winner, -2 = tie, otherwise its the winning player index.
        winningPlayerIndex = -2 # no winner yet
        winAmount = self.GetWinRequirment()
        # Check for full rows of same char
        # Check for full columns of same char
        # check for full diagonals of same char.
        for player in self.Players :
            playerChar = player.character
            print(player.name)
            # Check row for win
            for row in range(self.gameRows) :
                numCharsInRow = self.GetNumCharactersInRow(row, playerChar)
                if numCharsInRow == winAmount :
                    print("WON ROW")
            
            # Check column for win
            for colum in range(self.gameColumns) :
                numCharsInColumn = self.GetNumCharactersInColumn(colum, playerChar)
                if numCharsInColumn == winAmount :
                    print("WON COLUMN")

            # Check for diagonal win
            diagCharsMax = self.GetHighestNumCharsInDiagonals(playerChar)
            if diagCharsMax == winAmount :
                print("WON DIAGONAL")

    # How many in a row to win.        
    def GetWinRequirment(self) :
        return self.gameRows    # eh eventually make sure rows and colums are equal

    # how many matching characters are in this row
    def GetNumCharactersInRow(self, rowIndex, character) :
        numChars = 0
        #for row in range(len(self.boardValues)) :
        #    for column in range(len(self.boardValues[row])) :
        #    value = self.boardValues[row][column]
        for colum in range(self.gameColumns) :
            value = self.boardValues[rowIndex][colum]
            if value == character :
                numChars += 1

        return numChars

    # how many matching characters are in this colum.
    def GetNumCharactersInColumn(self, columnIndex, character) :
        numChars = 0

        for row in range(self.gameRows) :
            value = self.boardValues[row][columnIndex]
            if value == character :
                numChars += 1

        return numChars

    # Get max count of characters in both diagonals.
    def GetHighestNumCharsInDiagonals(self, character) :
        # for a 3x3 these are the diagonal coordinates.
        # d1    d2
        # 0,0   0,2   
        # 1,1   1,1
        # 2,2   2,0
        # d1 first :    0+1 to (max-1)
        # d1 second:    0+1 to (max-1)
        # d2 first:     0+1 to (max-1)
        # d2 second:    (max-1) - 1 to 0
        ## Diagonal 1
        #d1CharCount = 0
        d1C = 0
        d1Count = 0
        for d1Row in range(self.boardSize) :
            value = self.boardValues[d1Row][d1C]
            d1C += 1
            if value == character :
                d1Count += 1

        d2C = self.boardSize - 1
        d2Count = 0
        for d2Row in range(self.boardSize) :
            value = self.boardValues[d2Row][d2C]
            d2C -= 1
            if value == character :
                d2Count += 1

        return int(max(d1Count, d2Count))

    def RunGame(self):
        print("---------->>>Welcome to Jacksquatch Tic-Tac-Toe<<<----------")
        self.DrawBoardAndLegend()

        # Choose random player to start.
        self.currentPlayerIndex = random.randint(0, len(self.Players)-1)
        print(self.Players[self.currentPlayerIndex].name + " is up first.")

        while self.NumOpenCells() > 0:
            self.RunTurn()
            self.CheckForWin()
            self.NextTurn()
            #screen_clear()
            self.DrawBoardAndLegend()

########################
# Globals
########################
gameManager = TTTGameManager(3)     # Make the game manager global so it can be accessed in other places.
                                    # Specifically so the AI Player can access it.
########################
# Main Game Function...
########################
def Run() :
    gameManager.AddHumanPlayer("Jack", "X")
    gameManager.AddAIPlayer("Moron Computer", "O")
    gameManager.RunGame()

################
# Run the game.
################
Run()
