# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:24:34 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class Creator(ABC):
    
    @abstractmethod
    def create_element(self):
        pass 
        