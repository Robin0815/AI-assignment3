#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time


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
    current_row = []

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
    tree
    node

    Returns
    -------

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

    """
    return maze_map

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
    
    def get_coord(self):
        return [self.i,self.j]
    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent
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

def iterative_search():


    return None

def assign_character_for_nodes(maze_map, current_node, prev_node):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map : [type]
        [description]
    current_node : [type]
        [description]
    prev_node : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """


    return char_map

'''def assign_character_for_nodes(editable_map, current_node_index, way):
    """ can also edid previus nodes

    Parameters
    ----------
    editable_map : [list of lists]
        [the 2dim index describs the position. The content is the unicode character at this position ]
    current_node_index : [int]
        [the index in "way" with the newest visited node]
    way : [list of list]
        [a list of lists with the visited nodes as 2d coords]

    Returns
    -------
    [list of lists]
        [same as editable_map paramater]
    """
    
    i = current_node_index #to visualize, the way the current, previus and pre previus node is necessary
    #x=row
    cur_x = way[i][0]
    cur_y = way[i][1]
    prev_x = way[i-1][0]
    prev_y = way[i-1][1]

    if prev_y < cur_y:  #comes from left
        editable_map[cur_x][cur_y] = '\u2500' # "-"
        if i < 2: return editable_map #prevent from overriding S
        if way[i-2][0] < way[i-1][0]: # if prevprev is over prev 
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2514' #change prev to "L"
        if way[i-2][0] > way[i-1][0]: # if prevprev is under prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u250c' #change prev to ",-"
    
    elif prev_y > cur_y:  #comes from right
        editable_map[cur_x][cur_y] = '\u2500' # "-"
        if i < 2: return editable_map
        if way[i-2][0] < way[i-1][0]: # if prevprev is over prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2518' #change prev to "_|"
        if way[i-2][0] > way[i-1][0]: # if prevprev is under prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2510' #change prev to "-,"

    elif prev_x > cur_x:  #comes from under
        editable_map[cur_x][cur_y] = '\u2502' # "|"
        if i < 2: return editable_map
        if way[i-2][1] > way[i-1][1]: # if prevprev is right from prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2514' #change prev to "L"
        if way[i-2][1] < way[i-1][1]: # if prevprev is left from prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2518' #change prev to "_|"

    elif prev_x < cur_x:  #comes from above
        editable_map[cur_x][cur_y] = '\u2502' # "|"
        if i < 2: return editable_map
        if way[i-2][1] > way[i-1][1]: # if prevprev is right from prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u250c' #change prev to ",-"
        if way[i-2][1] < way[i-1][1]: # if prevprev is left from prev
            editable_map[way[i-1][0]][way[i-1][1]] = '\u2510' #change prev to "-,"

    if i== (len(way)-1):
        editable_map[cur_x][cur_y] = "*"    #if the last iteration deleted the goal symbol
    #-----</visualize way>--------
    
    return editable_map'''

def show_way_in_maze_map(maze_map, way):
    """

    Parameters
    ----------
    maze_map
    way

    Returns
    -------

    """
    #----<convert tuple to list>---- # make it editable
    editable_map = list()
    row_list = list()
    for row in maze_map:
        for char in row:
            row_list.append(char)
        editable_map.append(row_list)
        row_list=list()
    #----</convert tuple to list>----
    #----<iterate thought the way>----
    
    for i in range(1,len(way)): #dont override start and goal symbol
        editable_map = assign_character_for_nodes(editable_map,i, way)
    #----</iterate thought the way>----    
    #----<convert list to tuple>----
    maze_map= tuple(editable_map)
    #----</convert list to tuple>----    
    return maze_map

def print_map(map):
    """

    Parameters
    ----------
    map

    Returns
    -------

    """
    for row in map:
        for char in row:
            print(char, end = '')
    print()