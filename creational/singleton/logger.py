# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:59:42 2024

@author: Agnieszka Rabiej
"""

class Logger():
    
    _instance = None
    file_name = 'logs.txt'
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:    
            cls._instance = super().__new__(cls, *args, **kwargs)
            
        return cls._instance
    
    def save_to_file(self, log, name):
        with open(self.file_name, 'a') as file:
            file.write(f'{name}: {log} \n')

            