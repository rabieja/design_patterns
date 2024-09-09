# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:33:23 2024

@author: Agnieszka Rabiej
"""

from creational.factory_method.graph_element import GraphElement

class Edge(GraphElement):
    
    def print_type(self):
        print('Edge')