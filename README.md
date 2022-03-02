
=====================================
Objective
=====================================

The beginning of a Python program to play TicTacToe, built around the outline provided by Abuv Media.


=====================================
Operation
=====================================

Navigate to the 'src' folder and run the tictactoe.py script. I used the nosetests package to automatically detect and run my unit test suites. 


=====================================
Design Decisions & Issues
=====================================

I was able to implement the Board member functions, with the exception of the play_game function. I left that function for last as it depended on design decisions made in the supporting functions. 

I created an additional class to keep track of Players and their potential winning combinations. 

To facilitate a switch type structure, I created a function for converting the board "coordinates" to a base 10 value. That function can be found in the utility file.

I was also able to provide some unit tests for the mark_square function and the utility function, though ideally coverage would have been more complete.


=====================================
Time Spent
=====================================

In the spirit of full disclosure, I spent roughly a half an hour planning my solution. The main decision was going from a brute force board searching algorithm to letting the Player class keep track of their winning combinations, especially since there are only eight possible ways to win. I would have liked to reduce the winning check to between moves 5 and 9, since you can't win before then and the board is full after.

I also spent about a half an hour preparing my development environment and creating this documentation. 

Finally, the total time I spent coding was precisely one hour.
