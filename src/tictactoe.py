import player

class Board(object):
    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.__board_size = 3
        self.__board = [[0 for x in range(self.__board_size)] for y in range(self.__board_size)]
        self.__player_X = player.Player()
        self.__player_Y = player.Player()
        self.__current_player = ''

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: (bool) whether or not the square was marked
        """

        success = False
        inbounds = (row <= self.__board_size and column <= self.__board_size)

        if inbounds:
            success = self.__board[row][column] == 0

        if success:
            self.__board[row][column] = player

            if player == 'X':
                self.__player_X.update(row, column)
            elif player == 'Y':
                self.__player_Y.update(row, column)

        return success

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: (bool) whether the current player has a winning combination or not
        """
        if self.__current_player == 'X':
            return self.__player_X.is_winner()

        elif self.__current_player == 'Y':
            return self.__player_Y.is_winner()

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """

        pass


if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))