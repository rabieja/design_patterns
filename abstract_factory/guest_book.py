# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:51:52 2024

@author: Agnieszka Rabiej
"""

from abc import ABC, abstractmethod

class GuestBook(ABC):
    
    @abstractmethod
    def get_guest_book_style(self):
        pass