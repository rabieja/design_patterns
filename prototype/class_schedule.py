# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:50:58 2024

@author: Agnieszka Rabiej
"""

from prototype.prototype import Prototype

class ClassSchedule(Prototype):
    
    def __init__(self, name, last_name, **subjects):
        self.name = name
        self.last_name = last_name
        
        for subject, term in subjects.items():
           setattr(self, subject, term)
    
    def __str__(self):
        description = f'{self.name} {self.last_name} \n'
        
        for i_subject in vars(self):
            if i_subject != 'name' and i_subject != 'last_name':
                description += f'{i_subject} {getattr(self, i_subject)} \n'
                
        return description