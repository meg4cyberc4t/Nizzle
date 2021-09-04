from random import shuffle 
import os
from datetime import datetime


def getOriginalMatrix() -> list:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 

def showMatrix(matrix: list) -> None:
    print('  4 5 6')
    for row in range(3):
        print(f"{row + 1} " + "|".join(map(str, matrix[row])))


def randomizeMatrix(matrix: list) -> list:
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
    banner = """

    ███╗░░██╗██╗███████╗███████╗██╗░░░░░███████╗
    ████╗░██║██║╚════██║╚════██║██║░░░░░██╔════╝
    ██╔██╗██║██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░
    ██║╚████║██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░
    ██║░╚███║██║███████╗███████╗███████╗███████╗
    ╚═╝░░╚══╝╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
    """
    print(banner)


def move(matrix: list, move: int):
    if move > 0:
        if move <= 3:
            move -= 1
            buffer = matrix[move][2] 
            matrix[move][2] = matrix[move][1]
            matrix[move][1] = matrix[move][0]
            matrix[move][0] = buffer  
        else:
            move -= 3 
            move -= 1
            buffer = matrix[2][move] 
            matrix[2][move] = matrix[1][move]
            matrix[1][move] = matrix[0][move]
            matrix[0][move] = buffer  
    else:
        move = -move
        if move <= 3:
            move -= 1
            buffer = matrix[move][0] 
            matrix[move][0] = matrix[move][1]
            matrix[move][1] = matrix[move][2]
            matrix[move][2] = buffer  
        else:
            move -= 1
            move -= 3 
            buffer = matrix[0][move] 
            matrix[0][move] = matrix[1][move]
            matrix[1][move] = matrix[2][move]
            matrix[2][move] = buffer  


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
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
        print('Exiting...')
    # gameMatrix = randomizeMatrix(originalMatrix)
    gameMatrix = [[1, 2, 3], [4, 5, 6], [9, 7, 8]]
    startTime = datetime.now()
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
            print('\nExiting...')
            exit(0)
    endTime = datetime.now()
    print(f'Congratulations. You passed the game for {endTime - startTime}')
    print('Come again! :)')
    print('The author of the project: https://github.com/meg4cyberc4t')

if "__main__" == __name__ :
    main()