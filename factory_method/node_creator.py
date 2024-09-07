# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:33:26 2024

@author: Agnieszka Rabiej
"""

from factory_method.creator import Creator
from factory_method.node import Node

class NodeCreator(Creator):
    
    def create_element(self) -> Node:
        return Node()