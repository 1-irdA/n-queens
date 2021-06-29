EMPTY_PLACE = '.'
QUEEN = 'Q'

class Board:

    def __init__(self, size):
        if size < 4 or size % 2 != 0:
            raise ValueError
        self.size = size
        self.board = [[EMPTY_PLACE for i in range(self.size)] for j in range(self.size)]

    def solve_n_queens(self, column) -> bool:
        if column == self.size:
            return True

        for row in range(self.size):
            if self.__is_safe(row, column):
                self.board[row][column] = QUEEN

                if self.solve_n_queens(column + 1):
                    return True
                
                self.board[row][column] = EMPTY_PLACE   

        return False     
    
    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=' ')
            print()
        
    def __is_safe(self, row, column) -> bool:
        return self.__is_safe_row(row, column) \
            and self.__is_safe_up_anti_diagonal(row, column) \
            and self.__is_safe_low_anti_diagonal(row, column)
           
    def __is_safe_row(self, row, column) -> bool:
        row = [self.board[row][j] for j in range(column)]
        return all([elt == EMPTY_PLACE for elt in row])

    def __is_safe_up_anti_diagonal(self, row, column) -> bool:
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if self.board[i][j] != EMPTY_PLACE:
                return False
        return True

    def __is_safe_low_anti_diagonal(self, row, column) -> bool:
        for i, j in zip(range(row, self.size, 1), range(column, -1, -1)):
            if self.board[i][j] != EMPTY_PLACE:
                return False
        return True