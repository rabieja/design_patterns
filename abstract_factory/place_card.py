# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:51:51 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class PlaceCard(ABC):
    
    @abstractmethod
    def print_guest_name(self):
        pass