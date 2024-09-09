# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:18:56 2024

@author: Agnieszka Rabiej
"""

class Menu:
    
    def __init__(self):
        self.soup = None
        self.main_course = None
        self.dessert = None
        
    def __str__(self):
        menu_information = ''
        
        if self.soup:
            menu_information += f'Soup: {self.soup} \n'
        
        if self.main_course:
            menu_information += f'Main Course: {self.main_course} \n'
        
        if self.dessert:
            menu_information += f'Dessert: {self.dessert} \n'
        return menu_information