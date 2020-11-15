from solver import solve_board, print_board
import os


# getting the path of the input file
THIS_FOLDER = os.getcwd()
my_file = os.path.join(THIS_FOLDER, 'input.txt')

# saving the ocntents of the file in a variable
with open(my_file, 'r') as f1:
    string_list = f1.read()

string_list = string_list.split()       # converting the string into a list

# terminating the program if the list is not 9x9
if len(string_list) != 81:
    print("Please enter a 9x9 board")
    exit()

unsolved = []

index = 0       # counter to keep track of the string list's index

# saving the contents of the string list into a 2-d list
for i in range(9):
    unsolved.append([])
    for j in range(9):
        unsolved[i].append(int(string_list[index]))
        index += 1


print("input board: ")
print_board(unsolved)
solution = solve_board(unsolved)
print()
print('Solution: ')
print_board(solution)
