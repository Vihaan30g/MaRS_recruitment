
# Hard Dose: Q1

# Matrix is made with sufficient size to include all obstacles, initial pt & destination pt.

import numpy as np

def create_map(obstacles):   # obstacles is a matrix

    # farthest points to consider  ( 1 extra layer is created so as to ensure that there is enough space for the shortest path to exist. From online sources: 2 extra layers will be better as it can prevent almost all edge cases. )
    north = max(10, np.max(obstacles[:,1])) +1
    south = abs(min(0, np.min(obstacles[:,1])) -1)
    east = max(10, np.max(obstacles[:,0])) +1
    west = abs(min(0, np.min(obstacles[:,0])) -1)

    n = max(north+south, west+east)  # order of square grid map

    # Building the map, (initializing with all elements = 1)
    map_grid = np.ones((n,n))

    map_grid[n-1-south,west] = 8  # marking initial position of rover
 
    map_grid[n-1-south-10,west+10] = 9  # marking target destination

    map_grid[n-1-south - obstacles[:,1]  ,  west+obstacles[:,0]] = 0  # marking obstacles

    return map_grid



# Extracting obstacle info from given txt file
obstacles = np.genfromtxt('file1.txt',delimiter=' ')


# Processing input to get a simple array of coordinates of obstacles(x,y)
obstacles = obstacles.reshape(-1,2)    # Changes matrix shape. { -1 => whatever num of rows is suitable }
for i in range(0,len(obstacles),2):    
    obstacles[i,0] -= obstacles[i+1,0]
    obstacles[i,1] -= obstacles[i+1,1]
obstacles = np.delete(obstacles, np.arange(1,len(obstacles)+1,2), axis=0)   # removing unwanted part
    

# Sample input :  obstacles = np.array( [[-2,-3], [-4,0], [1,6], [5,5], [6,8], [3,2], [7,8]] )
 

answer = create_map(obstacles)   # FINAL MAP
print(answer)


