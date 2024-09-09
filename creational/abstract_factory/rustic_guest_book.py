# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:11:59 2024

@author: Agnieszka Rabiej
"""

from creational.abstract_factory.guest_book import GuestBook

class RusticGuestBook(GuestBook):
    
    def get_guest_book_style(self):
        return 'Rustic'