# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:22:03 2024

@author: Agnieszka Rabiej
"""

from abstract_factory.printing_house import PrintingHouse
from abstract_factory.rustic_invitation import RusticInvitation
from abstract_factory.rustic_place_card import RusticPlaceCard
from abstract_factory.rustic_guest_book import RusticGuestBook

class RusticPrintingHouse(PrintingHouse):
    
    def create_invitations(self):
        return RusticInvitation()
        
    def create_place_cards(self, name, last_name):
        return RusticPlaceCard(name, last_name)
        
    def create_guest_book(self):
        return RusticGuestBook()

        