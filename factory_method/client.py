# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:39:33 2024

@author: Agnieszka Rabiej
"""
from factory_method.creator import Creator
from factory_method.node_creator import NodeCreator
from factory_method.edge_creator import EdgeCreator

class FactoryMethodClient:
    
    @staticmethod
    def show_works(creator : Creator):
        element = creator.create_element()
        element.print_type()
        
    @classmethod
    def run(cls):
        cls.show_works(NodeCreator())
        cls.show_works(EdgeCreator())
        

if __name__ == "__main__":
    FactoryMethodClient.run()