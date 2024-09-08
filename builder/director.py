# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:18:45 2024

@author: Agnieszka Rabiej
"""

class Director:
    def __init__(self, builder):
        self.builder = builder
        
    def create_menu_without_deser(self, soup_name, main_course):
        self.builder.set_soup(soup_name)
        self.builder.set_main_course(main_course)
        
    def create_menu(self, soup_name, main_course, dessert_name):
        self.builder.set_soup(soup_name)
        self.builder.set_main_course(main_course)
        self.builder.set_dessert(dessert_name)
        
        
        