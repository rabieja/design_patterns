# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:42:40 2024

@author: Agnieszka Rabiej
"""

class DressAdapter:
    
    conversion_factor = 0.23
    def __init__(self, dress):
        self.dress_from_pl = dress
        
    def get_price_in_euro(self):
        return self.dress_from_pl.get_price_in_pln() * self.conversion_factor