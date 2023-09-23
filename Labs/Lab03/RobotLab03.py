import random
import numpy as np
    # Adopted from https://www.annytab.com/depth-first-search-algorithm-in-python/
    # This class represent a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
#creat new project when you use _init_ 
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

	# Draw a grid
def draw_grid(map, width, height, spacing=2, **kwargs):
    for y in range(height):
        for x in range(width):
            print('%%-%ds' % spacing % draw_tile(map, (x, y), kwargs), end='')
        print()

	# Draw a tile
def draw_tile(map, position, kwargs):
    
    # Get the map value
    value = map.get(position)
    
    # Check if we should print the path
    if 'path' in kwargs and position in kwargs['path']: value = 'P'
    
    # Check if we should print start point
    if 'start' in kwargs and position == kwargs['start']: value = 'S'
    
    # Check if we should print the goal point
    if 'goal' in kwargs and position == kwargs['goal']: value = 'G'
    
    # Return a tile value
    return value 

	# Depth-first search (DFS)
def depth_first_search(map, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Get the last node (LIFO - stack)
        current_node = open.pop(-1)
        
			# Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #path.append(start) 
            # Return reversed path
            return path[::-1]
        
			# Get the current node position
        (x, y) = current_node.position
        
			# Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
			# Loop neighbors
        for next in neighbors:
            # Get value from map
            map_value = map.get(next)
            
            # Check if the node is a wall
            if(map_value == '#'):
                continue
            
            # Create a neighbor node
            neighbor = Node(next, current_node)
            
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            
            # Everything is green, add the node if it not is in open
            if (neighbor not in open):
                open.append(neighbor)
    
		# Return None, no path is found
    return None

def MoveRobot(path):
    for position in path:
        print(position)
    for x, y in path:
        print(x, y)
    
    
    # Assume first and last row is wall and first and last column is wall
    TaskEnvModel = [
        [1,1,1,1,1],
        [1,0,2,0,1],
        [1,0,0,0,1],
        [1,0,0,2,1],
        [1,1,1,1,1]]
     
        
class Robot:

    def __init__(self, x, y):
        # set initial position of robot within task environment.
        self.positionX = x
        self.positionY = y
        self.EnergyConsumed = 0

        # Sensor values.
        self.LeftSensor = 0
        self.RightSensor = 0
        self.FrontSensor = 0
        self.BackSensor = 0
        self.DirtSensor = 0
        
        self.b=[]
        
        # Set initial orientation for robot in assigned cell.
        self.Orientation = "North"
        
        # Set goal for robot - All non-wall cells cleaned
        # self.NumberOfCellsToClean = 9     # suboptimal
        # self.NewCellsVisited = 0          # suboptimal
        self.AllCellsCleaned = False
        self.count = 0
 

    
    def Clean(self):
        if TaskEnvModel[self.positionX][self.positionY] == 2:
            TaskEnvModel[self.positionX][self.positionY] = 0
            self.EnergyConsumed = 2
            print("Current position [" + str(self.positionX) + "][" + 
                  str(self.positionY) + "] before moving has been cleaned")
        else:
           print("Current position before moving was already clean")

	# The main entry point for this module
def main():
    # Get a map (grid)
    map = {}
    chars = ['c']
    start = None
    end = None
    width = 0
    height = 0
    
		# Open a file
    fp = open('maze-in2.txt', 'r') #only reading 
    
    # Loop until there is no more lines
    while len(chars) > 0:
        # Get chars in a line
        chars = [str(i) for i in fp.readline().strip()]
        
			# Calculate the width
        width = len(chars) if width == 0 else width
        
			# Add chars to map
        for x in range(len(chars)):
            map[(x, height)] = chars[x]
            if(chars[x] == 'S'):
                start = (x, height)
            elif(chars[x] == 'G'):
                end = (x, height)
        
        # Increase the height of the map
        if(len(chars) > 0):
            height += 1
    
		# Close the file pointer
    fp.close()
    
		# Find the closest path from start(@) to end($)
    path = depth_first_search(map, start, end)
    print()
    print(path)
    print()
    draw_grid(map, width, height, spacing=1, path=path, start=start, goal=end)
    print()
    print('Steps to goal: {0}'.format(len(path)))
    print()
    MoveRobot(path)
    
    
	# Tell python to run main method
if __name__ == "__main__":
    main()

    
"""
Created on Wed Sep 29 16:28:08 2021
In the grid maze loaded on Brightspace (maze-in2), modify the grid with a new robot starting position in
the second row of the maze. Modify the goal for the robot to move to in a position in the second to last
row in the maze. Modify the program you wrote in lab 2 to use the Depth First Search code (provided
on Brightspace) to search for a path from start to goal for the robot. Use the result from the DFS search
(which will be a list of maze grid positions) to move the robot one grid position at a time until it reached
its goal. When you get to the goal, clean the space. Write this program using Python.

@author: Ghadir
"""