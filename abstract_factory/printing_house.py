# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:36:39 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class PrintingHouse(ABC):
    
    @abstractmethod
    def create_invitations(self):
        pass
    
    @abstractmethod
    def create_place_cards(self, name, last_name):
        pass
    
    @abstractmethod
    def create_guest_book(self):
        pass
    