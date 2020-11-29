#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time
from collections import deque


def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : [list]
        [description]

    Returns
    -------
    [list]
        [description]
    """
    
    empty_tree= []
    #current_row = []

    rows = len(maze_map)
    columns = len(maze_map[0])
    for i in range(0,rows):
        currrent_row = []
        for j in range(0,columns):
            currrent_row.append(Element_Node(i,j))
        empty_tree.append(currrent_row)
    return  empty_tree


def write_to_file(file_name, path):
    """Function to write output to console and the optimal path
    from start to each goal to txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.
    path : [type]
        [description]

    """
    '''f = open(path+file_name+".txt", "a")
    f.write()
    f.close()'''
    f = open(path + file_name + ".txt", "w")
    print('Filename:', file_name, file=f)


def get_start(maze_map):
    """

    Parameters
    ----------
    maze_map

    Returns
    -------

    """
    for i in range(0,maze_map.__len__()):
        for j in range(maze_map[i].__len__()):
            if maze_map[i][j] == 's':
                return [i,j]


def get_goal(maze_map):
    """

    Parameters
    ----------
    maze_map

    Returns
    -------

    """
    goals=[]
    for i in range(0,maze_map.__len__()):  
        for j in range(0,maze_map[i].__len__()):
            if maze_map[i][j] == '*':
                goals.append([i,j])
    return goals

def get_tree_node(tree, node):
    """

    Parameters
    ----------
    tree: [maze map as tree containing Element_Nodes]
    node: [Coordinates]

    Returns
    -------
    Element_Node : Complex datatype of Node, containing parent etc.

    """
   
    return tree[node[0]][node[1]]

def show_way(maze_map, the_way):
    """

    Parameters
    ----------
    maze_map
    the_way

    Returns
    -------
    maze_map with drawn the_way line

    """

     #same way as in printing the map
    modded_map = []
    
    for row in maze_map:
        rows = []
        for char in row:
            rows.append(char)
        modded_map.append(rows)
    #use the char map for inserting the line with help function
    for i in range(1,the_way.__len__()):
        modded_map = assign_character_for_nodes(modded_map,i, the_way) 
    modded_map= tuple(modded_map)
    return modded_map


def this_is_the_way(start, goal):
    """

    Parameters
    ----------
    start
    goal

    Returns
    -------

    """
    the_way = []
    start_node = start# get_tree_node(tree,start)
    node = goal#get_tree_node(tree,goal)
    #print(start_node.get_coord())
    #print(node.get_coord())
    #print(type(node))
    while node.get_coord() != start_node.get_coord():
        the_way.append(node.get_coord())
        node= node.get_parent()#get_tree_node(tree,node.get_parent)
    the_way.append(start_node.get_coord())
    the_way.reverse
    return the_way

class Element_Node:
    
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.parent = None
        self.depth = None
    
    def get_coord(self):
        return [self.i,self.j]
    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent
    def set_depth(self, depth):
        self.depth = depth
    def get_depth(self):
        return self.depth
    def is_visited(self):
        if (self.parent is None):
            return False
        return True
    def __eq__(self, other):
        """

        Parameters
        ----------
        other

        Returns
        -------

        """
        return self.i == other.i & self.j == other.j

    def get_neighbour(self, maze_map):
        """

        Parameters
        ----------
        maze_map

        Returns
        -------

        """
        coord_list = []
        coordinate = [self.i,self.j]
        #print(coordinate)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for k in range(0,4):
            try:
                i = coordinate[0] + directions[k][0]
                j = coordinate[1] + directions[k][1]
                if(maze_map[i][j] !='|' and maze_map[i][j] !='='):
                    coord_list.append([i,j])
            except Exception:
                pass

        return coord_list

def iterative_search(maze_map, start_pos, goal_pos, depth):
    """
    Parameters
    ----------
    maze_map : []
        [2d array of chars]
    start_pos : [tuple]
        [coordinates of the start point in the map]
    goal_pos : [tuple]
        []

    Returns
    -------
    [maze_map]
        [modded_maze_map with drawn line fitting to the algorythm: dfs]
    """
    
    queue = deque()
    queue.append(start_pos)

    # Fill in your BFS algorithm here
    tree = maze_map_to_tree(maze_map)
    start_node = get_tree_node(tree, start_pos)
    start_node.set_depth(0)
    goal_node = get_tree_node(tree, goal_pos)
    #goal_node.set_depth(0)
    #print(goal_node.get_coord)
    #print(goal_pos)
    while queue.__len__() > 0:
        current_node = queue.pop() #only difference to bfs in this implementation, Stack(LIFO)
        current_node_node = get_tree_node(tree, current_node)
        #print(current_node_node.get_coord())
        #print(current_node)
        if current_node_node.get_coord() == goal_node.get_coord():
            the_way = this_is_the_way(start_node, goal_node)
            new_maze_map = show_way(maze_map, the_way)

            #print(the_way)
            return new_maze_map
        if current_node_node.get_depth() < depth:

            neighbour = current_node_node.get_neighbour(maze_map)
            #print(neighbour)
            for neigh in neighbour:
                neigh_node = get_tree_node(tree, neigh)
                if neigh_node.is_visited() == False:
                    queue.append(neigh)
                    neigh_node.set_parent(current_node_node)
                    neigh_node.set_depth(current_node_node.get_depth()+1)


    return maze_map


def assign_character_for_nodes(modded_map, i, the_way):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    modded_map : [list of list of Element_Nodes]
        [representation of the maze, that gets the drawn line injected]
    index : [int]
        [positional argument for the_way list]
    the_way [list of coordinates]
        [way from s to *]

    Returns
    -------
    modded_map : [list of list of Element_Nodes]
        [new maze_map with drawn line]
    """
    vertical = "\u2502"     
    horizontal = "\u2500"   
    left_down = "\u2510"    
    up_right = "\u2514"     
    left_up = "\u2518"      
    down_right = "\u250c"   


    current_X = the_way[i][0]
    current_Y = the_way[i][1]
    previous_X = the_way[i-1][0]
    previous_Y = the_way[i-1][1]

    #four possibilities: left/right/above/under

    if (current_X > previous_X):    #above
        modded_map[current_X][current_Y] = vertical
        if i < 2: return modded_map
        if the_way[i-2][1] > the_way[i-1][1]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = down_right
        if the_way[i-2][1] < the_way[i-1][1]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = left_down

    if (current_X < previous_X):    #under
        modded_map[current_X][current_Y] = vertical
        if i < 2: return modded_map
        if the_way[i-2][1] > the_way[i-1][1]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = up_right
        if the_way[i-2][1] < the_way[i-1][1]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = left_up

    if (current_Y < previous_Y):    #right
        modded_map[current_X][current_Y] = horizontal
        if i < 2: return modded_map
        if the_way[i-2][0] > the_way[i-1][0]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = left_down
        if the_way[i-2][0] < the_way[i-1][0]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = left_up

    if (current_Y > previous_Y):    #left
        modded_map[current_X][current_Y] = horizontal
        if i < 2: return modded_map
        if the_way[i-2][0] > the_way[i-1][0]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = down_right
        if the_way[i-2][0] < the_way[i-1][0]: 
            modded_map[the_way[i-1][0]][the_way[i-1][1]] = up_right

    if(i == the_way.__len__()-1):
        modded_map[current_X][current_Y] = 'S'

    return modded_map


def print_map(map):
    """

    Parameters
    ----------
    map : maze_map

    Returns
    -------
    Void : Prints Map in Terminal

    """
    for row in map:
        for char in row:
            print(char, end = '')
    print()