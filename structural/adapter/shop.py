# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:42:41 2024

@author: Agnieszka Rabiej
"""

class Shop:
    
    def show_price(self, item):
        print(f'{item.get_price_in_euro()} euro')