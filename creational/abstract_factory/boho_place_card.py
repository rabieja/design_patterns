# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:11:59 2024

@author: Agnieszka Rabiej
"""

from creational.abstract_factory.place_card import PlaceCard

class BohoPlaceCard(PlaceCard):
    
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        
    def print_guest_name(self):
        print(f'(Boho) {self.name} {self.last_name}')