# A Sudoku Solver

def print_board(board):
    """Function to print a sudoku board in readable format

    Args:
        board (list): Sudoku board to be printed
    """

    num_of_rows = len(board)        # saving the number of rows to reduce time complexity later
    num_of_cols = len(board[0])     # saving the number of columns to reduce time complexity later

    # Checking if the board is a sudoku board
    if num_of_rows != 9 and num_of_cols != 9:
        print("This is not a sudoku board")
        return None         # returning nothing if the board is not a sudoku board
    
    seperator = "-" * 25        # a border/line to create vertical lines for 3x3 grid
    print(seperator)        # printing the top border

    
    # loop to print the board
    # iterates each row
    for i in range(num_of_rows):
        
        # loop to print the contents in each row
        for j in range(num_of_cols):
            
            # adding left border and horizontal line for 3x3 grid
            if (j % 3 == 0):
                print('| ', end = "")
            
            number = board[i][j]        # saving the current number to reduce time complexity
            # printing the number only if it is not zero
            if number == 0:
                print("_ ", end = "")
            else:
                print("%d " %(number), end = "")

            # adding the right-side border
            if (j == num_of_rows - 1):
                print('| ', end = "")
        
        print() # new line
        
        # bottom border
        if (i+1) % 3 == 0:
            print(seperator)



def isPossible(board, number, position):
    """Function to check if a number can be put in a square

    Args:
        board (list): Sudoku board to be checked on
        number (int): Number to be checked
        position (tuple): Position to be checked (i, j)

    Returns:
        bool: True if number can be put in the given position, false if otherwise
    """
    
    # checking if the said number exists in its column
    # returns False if it exists
    for i in range(9):
        if board[i][position[1]] == number:
            return False
    
    # checking if the said number exists in its row
    # returns False if it exists
    for i in range(9):
        if board[position[0]][i] == number:
            return False

    # assigning and calculating the starting indices of mini 3x3 grid
    x_grid = (position[0] // 3) * 3
    y_grid = (position[1] // 3) * 3

    # checking if said number exists in the sub-grid
    # returns false if it exists
    for i in range(3):
        for j in range(3):
            if board [ x_grid + i ] [ y_grid + j ] == number:
                return False
    
    return True



def next_empty(board):
    """Function which looks for the next empty square in the board.

    Args:
        board (list): The sudoku board

    Returns:
        tuple: Tuple with co-ordinates of the square, None if no empty squares remains
    """

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    
    return None



# recursive function which solves an unsolved board
# makes changes in the input board itself
# only to be called using the solve_board function to avoid changing the input board
def return_solution(board):
    length = len(board)          # calculating length of the matrix

    # returning None if the length and breath of the board do not match
    if length != len(board[0]):
        return None
    
    # calling the next_empty functiona n=and storing the result
    empty_loc = next_empty(board)

    # returns True if no empty squares are found
    # this means the puzzle has been solved
    # if empty sqaures are found, co-ordinates are stored
    if  empty_loc == None:
        return True
    else:
        row, col = empty_loc

    # loop to check all numbers from 1 to 10 in the above co-ordinate
    for number in range(1, 10):
        
        # assigning the number to the sqaure if it is possible
        if isPossible(board, number, (row, col)):
            board[row][col] = number

            # recusrion
            if return_solution(board):
                return True
        
        # backtracking to the previous square if none of the numbers fit into the square
        board[row][col] = 0
    
    return False



# function which returns a solved sudoku puzzle
# creates a copy of the board and then passes in into the recursive function to retain original board
def solve_board(board):
    """Function which returns a solved board

    Args:
        board (list): The sudoku board

    Returns:
        list: Solved board
    """

    # creating a copy of the original board to retain the original board
    solution = []
    for i in range(len(board)):
        solution.append([])
        for j in range(len(board)):
            solution[i].append(board[i][j])

    return_solution(solution)
    return solution
