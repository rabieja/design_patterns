# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:17:42 2024

@author: Agnieszka Rabiej
"""

from creational.builder.chef_with_one_star_builder import ChefWithOneStarBuilder
from creational.builder.chef_with_two_stars_builder import ChefWithTwoStarsBuilder
from creational.builder.director import Director

class BuilderTest:
    
    @staticmethod
    def run():
        
        builder_one_star = ChefWithOneStarBuilder()
        first_director = Director(builder_one_star)
        first_director.create_menu_without_deser('pomidorowa', 'schabowy')
        print(first_director.builder.get_menu())
        print(first_director.builder.get_price())
        
        builder_two_stars = ChefWithTwoStarsBuilder()
        second_director = Director(builder_two_stars)
        
        second_director.create_menu('pomidorowa', 'schabowy', 'tiramisu')
        print(second_director.builder.get_menu())
        print(second_director.builder.get_price())
        
        
if __name__ == "__main__":
    BuilderTest.run()