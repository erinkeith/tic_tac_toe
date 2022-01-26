import player

class Board(object):
    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.__board_size = 3
        self.__board = [[0 for x in range(self.__board_size)] for y in range(self.__board_size)]
        self.__player_X = player.Player()
        self.__player_O = player.Player()
        self.__current_player = ' '
        
    def __str__(self):
        return self.__board
        
    def change_player(self):
        if self.__current_player = ' ':
            self.__current_player = 'O'
        elif self.__current_player = 'O':
            self.__current_player = 'X'
        elif self.__current_player = 'X':
            self.__current_player = 'O'

    def mark_square(self, row, column):
        """
        Marks a square at coordinate (row, column) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark

        :return: (bool) whether or not the square was marked
        """

        success = False
        inbounds = (row <= self.__board_size and column <= self.__board_size)

        if inbounds:
            success = self.__board[row][column] == ' '

        if success:
            self.__board[row][column] = self.__current_player

            if player == 'X':
                self.__player_X.update(row, column)
            elif player == 'O':
                self.__player_O.update(row, column)

        return success

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: (bool) whether the current player has a winning combination or not
        """
        if self.__current_player == 'X':
            return self.__player_X.is_winner()

        elif self.__current_player == 'O':
            return self.__player_O.is_winner()

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        while not has_winner():
            print(self.__board)
            change_player()
            row = input("Player " + self.__current_player + ", enter your row: ")
            col = input("Player " + self.__current_player + ", enter your column: ")
            while not mark_square(row, col):
                print("Invalid Move)
                row = input("Player " + self.__current_player + ", enter your row: ")
                col = input("Player " + self.__current_player + ", enter your column: ")
        return self.__current_player


if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print(winner + " has won!")
