# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:18:48 2024

@author: Agnieszka Rabiej
"""

from builder.chef_builder import ChefBuilder
from builder.menu import Menu

class ChefWithTwoStarsBuilder(ChefBuilder):

    price = 200
    
    def __init__(self):
        self.menu = Menu()

    def set_soup(self, soup):
        self.menu.soup = soup

    def set_main_course(self, main_course):
        self.menu.main_course = main_course

    def set_dessert(self, dessert):
        self.menu.dessert = dessert
    
    def get_price(self):
        full_price = self.price * 0.6 if self.menu.soup else 0
        full_price += self.price if self.menu.main_course else 0
        full_price += self.price * 0.7 if self.menu.dessert else 0
        return full_price
    
    def get_menu(self):
        return self.menu