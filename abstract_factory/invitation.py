# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:51:47 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class Invitation(ABC):
    
    @abstractmethod
    def print_invitation_content(self):
        pass