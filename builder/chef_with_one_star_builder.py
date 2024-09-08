# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:18:49 2024

@author: Agnieszka Rabiej
"""

from builder.chef_builder import ChefBuilder
from builder.menu import Menu

class ChefWithOneStarBuilder(ChefBuilder):

    price = 100
    
    def __init__(self):
        self.menu = Menu()

    def set_soup(self, soup):
        self.menu.soup = soup

    def set_main_course(self, main_course):
        self.menu.main_course = main_course

    def set_dessert(self, dessert):
        self.menu.dessert = dessert
    
    def get_price(self):
        full_price = 0
        for i_dish in (self.menu.soup, self.menu.main_course, self.menu.dessert):
            full_price += self.price if i_dish else 0
        return full_price
    
    def get_menu(self):
        return self.menu