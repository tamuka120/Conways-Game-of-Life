import numpy as np

class Map:
    
    #__init__ works as constructor 
    def __init__(self, x, y):
       self.world = np.zeros((x, y)) # generate cells of the game world array using numpy

    def live(self,live_cells):
        self.world[live_cells[0], live_cells[1]] =  1.0
        #print("live",[live_cells[0], live_cells[1]])
        
    def die(self,dead_cells):
        self.world[dead_cells[0], dead_cells[1]] =  0.0
        #print("dead",[dead_cells[0], dead_cells[1]])
        
    #Get total number of neighbors for given coordinates
    def neighbors(self, x, y):
        
        #Checks the relevant coordinates for if the cell is currently on the border and changes neighbor slice
        if x ==0 and y == 0:
            self.num_neighbors = np.sum(self.world[x:x + 2, y:y + 2]) - self.world[x,y]
        elif x == 0:
            self.num_neighbors = np.sum(self.world[x:x + 2, y - 1:y + 2]) - self.world[x,y]
        elif y == 0:
            self.num_neighbors = np.sum(self.world[x - 1:x + 2, y:y + 2]) - self.world[x,y]
        else:
            self.num_neighbors = np.sum(self.world[x - 1:x + 2, y - 1:y + 2]) - self.world[x,y]
        return self.num_neighbors
        
        

        
  
       
