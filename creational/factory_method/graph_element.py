# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:22:45 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class GraphElement(ABC):
    
    @abstractmethod
    def print_type(self):
        pass
    