# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:43:46 2021

@author: acybe
"""

import time


# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
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
    if 'path' in kwargs and position in kwargs['path']: value = 'p'
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
        # Get the last node (LIFO)
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
        # Unzip the current node position
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

# The main entry point for this module
def main():
    # Get a map (grid)
    start_time = time.time()
    map = {}
    chars = ['c']
    start = None
    end = None
    width = 0
    height = 0
    # Open a file
    fp = open('maze.txt', 'r')
    
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
    print("\nDFS")
    start_time = time.time()
    print()
    # Find the closest path from start(@) to end($)
    path = depth_first_search(map, start, end)
    end_time = time.time()
    #total = end_time - start_time
    #executionTime = end_time - start_time
    print("How long the code runing = ", end_time - start_time)
    #executionTime = time.time() - start_time
    #print("How long the code runing in sec = " + str(executionTime))
    #print("How long the code runing= ", end_time - start_time)
    #print (e.strftime("\n%M:%S\n"))
    print()
    print(path)
    print()
    draw_grid(map, width, height, spacing=1, path=path, start=start, goal=end)
    print()
    print('Steps to goal: {0}'.format(len(path)))
    print()

# Tell python to run main method
if __name__ == "__main__":
   
    main()

