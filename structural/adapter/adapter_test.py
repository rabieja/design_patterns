# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:43:41 2024

@author: Agnieszka Rabiej
"""

from structural.adapter.dress_from_italy import DressFromItaly
from structural.adapter.dress_from_poland import DressFromPoland
from structural.adapter.dress_adapter import DressAdapter
from structural.adapter.shop import Shop

class AdapterTest:
    
    @staticmethod
    def run():
        first_dress = DressFromItaly(100)
        second_dress = DressFromPoland(350)
        dress_adapter = DressAdapter(second_dress)
        
        shop = Shop()
        
        shop.show_price(first_dress)
        shop.show_price(dress_adapter)
        

if __name__ == "__main__":
    AdapterTest.run()
        
        