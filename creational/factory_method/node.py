# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:33:21 2024

@author: Agnieszka Rabiej
"""

from creational.factory_method.graph_element import GraphElement

class Node(GraphElement):
    
    def print_type(self):
        print('Node')
    