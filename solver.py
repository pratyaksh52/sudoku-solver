# A Sudoku Solver

# function to print a sudoku board.
def print_board(board):
    num_of_rows = len(board)        # saving the number of rows to reduce time complexity later
    num_of_cols = len(board[0])     # saving the number of columns to redice time complexity later

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


# Function to check if a number can be put in a square
# Returns boolean value
# arguement 'board' is a 2-d list which has the board itself
# arguement 'number' is the number which is to be checked
# arguement 'position' is a tuple where position[0] is the ith row and position[1] is the jth column
def isPossible(board, number, position):
    
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


# function which looks for the next empty square in a board
# returns a tuple with co-ordinates of the square
# retuens None is no empty square is found
def next_empty(board):

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

    # creating a copy of the original board
    solution = []
    for i in range(len(board)):
        solution.append([])
        for j in range(len(board)):
            solution[i].append(board[i][j])

    return_solution(solution)
    return solution
