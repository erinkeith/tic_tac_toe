import utility

class Player(object):
    def __init__(self):
        """
        Initializes the Player
        """
        self.__top_horizontal = 0
        self.__mid_horizontal = 0
        self.__low_horizontal = 0
        self.__left_vertical = 0
        self.__mid_vertical = 0
        self.__right_vertical = 0
        self.__upper_left_diagonal = 0
        self.__upper_right_diagonal = 0

    def update(self, row, column):
        convertedPosition = utility.base3tobase10(row, column)

        if convertedPosition == 0:
            self.__top_horizontal += 1
            self.__left_vertical += 1
            self.__upper_left_diagonal += 1

        elif convertedPosition == 1:
            self.__top_horizontal += 1
            self.__mid_vertical += 1

        elif convertedPosition == 2:
            self.__top_horizontal += 1
            self.__right_vertical += 1
            self.__upper_right_diagonal += 1

        elif convertedPosition == 3:
            self.__mid_horizontal += 1
            self.__left_vertical += 1

        elif convertedPosition == 4:
            self.__mid_horizontal += 1
            self.__mid_vertical += 1
            self.__upper_right_diagonal += 1
            self.__upper_left_diagonal += 1

        elif convertedPosition == 5:
            self.__mid_horizontal += 1
            self.__right_vertical += 1

        elif convertedPosition == 6:
            self.__low_horizontal += 1
            self.__left_vertical += 1
            self.__upper_right_diagonal += 1

        elif convertedPosition == 7:
            self.__low_horizontal += 1
            self.__mid_vertical += 1

        elif convertedPosition == 8:
            self.__low_horizontal += 1
            self.__right_vertical += 1
            self.__upper_left_diagonal += 1

    def is_winner(self, winning_number):
        return (self.__top_horizontal == winning_number
                or self.__mid_horizontal == winning_number
                or self.__low_horizontal == winning_number
                or self.__left_vertical == winning_number
                or self.__mid_vertical == winning_number
                or self.__right_vertical == winning_number
                or self.__upper_left_diagonal == winning_number
                or self.__upper_right_diagonal == winning_number)
