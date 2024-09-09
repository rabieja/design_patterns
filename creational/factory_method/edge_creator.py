# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:33:28 2024

@author: Agnieszka Rabiej
"""

from creational.factory_method.creator import Creator
from creational.factory_method.edge import Edge

class EdgeCreator(Creator):
    
    def create_element(self) -> Edge:
        return Edge()