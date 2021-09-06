from random import shuffle # To randomize an array
import os # To clean the screen
from datetime import datetime  # To record the time


def getOriginalMatrix() -> list:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # correct array


def showMatrix(matrix: list) -> None:
    # This function allows you to output the matrix in this form:
    #   4 5 6
    # 1 1|2|3
    # 2 4|5|6
    # 3 7|8|9
    print('  4 5 6')
    for row in range(3):
        print(f"{row + 1} " + "|".join(map(str, matrix[row])))


def randomizeMatrix(matrix: list) -> list:
    # This function is used to randomize the array
    returnMatrix = [[], [], []]
    oneMatrix = [elem for j in matrix for elem in j]
    shuffle(oneMatrix)
    for index in range(len(oneMatrix)):
        if index < 3:
            returnMatrix[0].append(oneMatrix[index])
        elif 3 <= index < 6:
            returnMatrix[1].append(oneMatrix[index])
        else:
            returnMatrix[2].append(oneMatrix[index])
    return returnMatrix


def showBanner() -> None:
    # this function shows a banner (wow how unexpected :D)
    banner = """

    ███╗░░██╗██╗███████╗███████╗██╗░░░░░███████╗
    ████╗░██║██║╚════██║╚════██║██║░░░░░██╔════╝
    ██╔██╗██║██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░
    ██║╚████║██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░
    ██║░╚███║██║███████╗███████╗███████╗███████╗
    ╚═╝░░╚══╝╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
    """
    print(banner)
    print('The author of the project: https://github.com/meg4cyberc4t')



def move(matrix: list, move: int):
    # movement in the array
    if move > 0:
        if move <= 3:
            # on the right
            move -= 1
            buffer = matrix[move][2]
            matrix[move][2] = matrix[move][1]
            matrix[move][1] = matrix[move][0]
            matrix[move][0] = buffer 
        else:
            # on the down
            move -= 3
            move -= 1
            buffer = matrix[2][move]
            matrix[2][move] = matrix[1][move]
            matrix[1][move] = matrix[0][move]
            matrix[0][move] = buffer
    else:
        move = -move
        if move <= 3:
            # on the left
            move -= 1
            buffer = matrix[move][0]
            matrix[move][0] = matrix[move][1]
            matrix[move][1] = matrix[move][2]
            matrix[move][2] = buffer
        else:
            # on the up
            move -= 1
            move -= 3
            buffer = matrix[0][move]
            matrix[0][move] = matrix[1][move]
            matrix[1][move] = matrix[2][move]
            matrix[2][move] = buffer

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clearTerminal()
    showBanner()
    print('Welcome to Nizzle. Your task is to return the matrix to its original position:')
    originalMatrix = getOriginalMatrix()
    showMatrix(originalMatrix)
    print('You can do this by moving one column or row. To do this,' \
          'use the numbers from 1 to 6. If you use negative numbers from' \
          ' 1 to 6, then the movement will be in the opposite direction.')
    try:
        input("Let\'s start? (If not, press ctrl + c)\n")
    except KeyboardInterrupt:
        # intercepting a forced exit
        print('Exiting...')
        exit(0)
    gameMatrix = randomizeMatrix(originalMatrix)
    # gameMatrix = [[1, 2, 3], [4, 5, 6], [9, 7, 8]]
    startTime = datetime.now() # recording the start time
    errorMessage = ""
    while gameMatrix != originalMatrix:
        clearTerminal()
        showMatrix(gameMatrix)
        if (errorMessage):
            print(errorMessage)
        errorMessage = ""
        try:
            thisInput = int(input('Make a move: '))
            if thisInput == 0 or thisInput > 6 or thisInput < -6:
                raise ValueError
            move(gameMatrix, thisInput)
        except ValueError:
            errorMessage = "Incorrect input. Use numbers from 1 to 6, -1 to -6!"
            continue
        except KeyboardInterrupt:
            # intercepting a forced exit
            print('\nExiting...')
            exit(0)
    endTime = datetime.now() # recording the end time
    print(f'Congratulations. You passed the game for {endTime - startTime}')
    print('Come again! :)')
    print('The author of the project: https://github.com/meg4cyberc4t')

if "__main__" == __name__ :
    main()