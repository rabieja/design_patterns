# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:18:50 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class ChefBuilder(ABC):

    @abstractmethod
    def set_soup(self, soup):
        pass

    @abstractmethod
    def set_main_course(self, main_course):
        pass

    @abstractmethod
    def set_dessert(self, dessert):
        pass
    
    @abstractmethod
    def get_price(self):
        pass
    
    @abstractmethod
    def get_menu(self):
        pass