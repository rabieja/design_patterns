# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:25:24 2024

@author: Agnieszka Rabiej
"""

class User():
    from singleton.logger import Logger
    
    logger = Logger()
    def __init__(self, name):
        self.name = name
        
    def send_message(self, message):
        self.logger.save_to_file(message, self.name)
