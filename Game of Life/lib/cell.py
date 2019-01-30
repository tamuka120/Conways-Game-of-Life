class Cell:

    #Checks each cell in the current generation against the rules of the game
    def cell_rules(self,world, x, y, map_object):
        self.dead_pool = []
        self.live_pool = []

        for i in range(x):
            for j  in range(y):
                self.alive = map_object.neighbors(i,j)#Get neighbor for the current set of coordinates
                
                # Cell under-population and over-population 
                if world[i][j] == 1.0 and (self.alive < 2 or self.alive > 3):
                    self.dead_pool.append([i,j])

                # A new cell is born
                if world[i][j] == 0.0 and self.alive == 3:
                    self.live_pool.append([i,j])
                    
                # Remains the same 
                else:
                    pass
        return self.dead_pool, self.live_pool
    
    #Applies rule effect on to the cells for the next generation
    def cell_effect(self, dead_pool,live_pool, map_object):
        for i in dead_pool:
            map_object.die(i)

        for k in live_pool:
            map_object.live(k)
