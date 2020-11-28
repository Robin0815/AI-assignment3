#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes, get_start, get_goal, get_tree_node, this_is_the_way, show_way, show_way_in_maze_map, print_map


def depth_first_search(maze_map, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [type]
        [description]
    start_pos : [type]
        [description]
    goal_pos : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    queue = deque()
    queue.append(start_pos)

    # Fill in your BFS algorithm here
    tree = maze_map_to_tree(maze_map)
    start_node = get_tree_node(tree, start_pos)
    goal_node = get_tree_node(tree, goal_pos)
    #print(goal_node.get_coord)
    #print(goal_pos)
    while queue.__len__() > 0:
        current_node = queue.pop()
        current_node_node = get_tree_node(tree, current_node)
        #print(current_node_node.get_coord())
        #print(current_node)
        if current_node_node.get_coord() == goal_node.get_coord():
            the_way = this_is_the_way(start_node, goal_node)
            new_maze_map = show_way_in_maze_map(maze_map, the_way)
            print('worked with Result: \n')
            #print(the_way)
            return new_maze_map
            '''the_way = []
            node = goal_node
            #print(type(node))
            while node.get_coord() != start_node.get_coord():
                the_way.append(node.get_coord())
                #print(type(node.get_parent().get_parent()))
                node= node.get_parent()#get_tree_node(tree,node.get_parent)
            the_way.append(start_node.get_coord())
            the_way.reverse
            return the_way'''
        neighbour = current_node_node.get_neighbour(maze_map)
        #print(neighbour)
        for neigh in neighbour:
            neigh_node = get_tree_node(tree, neigh)
            if neigh_node.is_visited() == False:
                queue.append(neigh)
                neigh_node.set_parent(current_node_node)

    print('worked')
    return maze_map


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    # CALL THESE FUNCTIONS after filling in the necessary implementations
    start_pos_map1 = get_start(maze_map_map1)
    goal_pos_map1 =get_goal(maze_map_map1)
    for goal_pos in goal_pos_map1:

        path_map1 = depth_first_search(maze_map_map1, start_pos_map1, goal_pos)
        print('\nSolution: ')
        print_map(path_map1)

        # write_to_file("dfs_map3", path_map3)
    # write_to_file("bfs_map1", path_map1)

    start_pos_map2 = get_start(maze_map_map2)
    goal_pos_map2 =get_goal(maze_map_map2)
    for goal_pos in goal_pos_map2:

        path_map2 = depth_first_search(maze_map_map2, start_pos_map2, goal_pos)
        print('\nSolution: ')
        print_map(path_map2)
        
        # write_to_file("dfs_map3", path_map3)
    # path_map2 = breadth_first_search(maze_map_map2, start_pos_map2, goal_pos_map2)
    # write_to_file("dfs_map2", path_map2)


    start_pos_map3 = get_start(maze_map_map3)
    goal_pos_map3 =get_goal(maze_map_map3)
    for goal_pos in goal_pos_map3:

        path_map3 = depth_first_search(maze_map_map3, start_pos_map3, goal_pos)
        print('\nSolution: ')
        print_map(path_map3)

        # write_to_file("dfs_map3", path_map3)
    # path_map3 = breadth_first_search(maze_map_map3, start_pos_map3, goal_pos_map3)
    # write_to_file("bfs_map3", path_map3)
