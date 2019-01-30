from lib.map import Map
from lib.cell import Cell
import numpy as np
"""
Assumptions made about the problem
1. The display of the live and dead cells including the grid did not have to have visual elements
2. The seed of the universe did not require to be changeable during execution
3. The dimensions of the world could be set to anything
"""

#Variables
x = int(input("Enter width 0 - 20: "))
y = int(input("Enter height 0 - 20: "))
max_generations = int(input("Enter maximum amount of generations you would like to generate e.g 10: "))
myMap = Map(x, y) # - Generate Map and create object
myCell = Cell()

#Seed - This activates some cells in advance before the game starts.
myMap.live([1,4])
myMap.live([1,5])
myMap.live([1,6])


def start():
    generation_count = 0
    while (np.any(myMap.world)) and (generation_count <= max_generations): #np.any checks if any cell is alive

        print ("Current generation: " + str(generation_count)) #Generation counter
        print(myMap.world, "\n")#Print cell world
        
        #Get pool of cells that are to be marked dead or live for the next generation
        cell_pool = myCell.cell_rules(myMap.world, x, y, myMap)

        #Apply states to cells for next generation
        myCell.cell_effect(cell_pool[0],cell_pool[1], myMap)
        generation_count+=1
        
    print("Final Generation ","\n") # Print final iteration of world after exiting while loop
    print(myMap.world, '\n') 
start()
