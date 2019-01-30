# Conway's - Game of Life


The Game of Life (an example of a cellular automaton) is played on an infinite two-dimensional rectangular grid of cells. Each cell can be either alive or dead. The status of each cell changes each turn of the game (also called a generation) depending on the statuses of that cell's 8 neighbors. Neighbors of a cell are cells that touch that cell, either horizontal, vertical, or diagonal from that cell.

Any live cell with fewer than two live neighbors dies, as if by underpopulation.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
(Excerpt from http://pi.math.cornell.edu/)

Key Notes:
* For this iteration of the code the game will not be made of square cells but instead be a 2D binary array.
* The game world dimensions are limited at the moment due to the amount of things python will allow to be printed to the output.
