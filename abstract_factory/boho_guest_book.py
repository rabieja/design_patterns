# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:12:00 2024

@author: Agnieszka Rabiej
"""


from abstract_factory.guest_book import GuestBook

class BohoGuestBook(GuestBook):
    
    def get_guest_book_style(self):
        return 'Boho'