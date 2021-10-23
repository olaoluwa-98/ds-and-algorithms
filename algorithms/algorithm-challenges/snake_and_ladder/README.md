# Snake and Ladder

Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from source or 1st cell. Basically, the player has total control over outcome of dice throw and wants to find out minimum number of throws required to reach last cell. If the player reaches a cell which is base of a ladder, the player has to climb up that ladder and if reaches a cell is mouth of the snake, has to go down to the tail of snake without a dice throw.

For example, consider the board shown, the minimum number of dice throws required to reach cell 30 from cell 1 is 3.
Following are the steps:

- First throw two on dice to reach cell number 3 and then ladder to reach 22
- Then throw 6 to reach 28.
- Finally through 2 to reach 30.

There can be other solutions as well like (2, 2, 6), (2, 4, 4), (2, 3, 5).. etc.
