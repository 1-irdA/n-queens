from board import *

if __name__ == '__main__':
    try:
        nb_queens= int(input("Input an even number greater or equal than 4 : ")) 
        board = Board(nb_queens)
        board.solve_n_queens(0)
        board.display()
    except ValueError:
        print("Needs an even integer greater or equal than 4")