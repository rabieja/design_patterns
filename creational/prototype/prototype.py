# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:52:56 2024

@author: Agnieszka Rabiej
"""

import copy

class Prototype:
    
    def clone(self):
        return copy.deepcopy(self)