# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:27:58 2024

@author: Agnieszka Rabiej
"""

from creational.abstract_factory.printing_house import PrintingHouse
from creational.abstract_factory.boho_invitation import BohoInvitation
from creational.abstract_factory.boho_place_card import BohoPlaceCard
from creational.abstract_factory.boho_guest_book import BohoGuestBook

class BohoPrintingHouse(PrintingHouse):
    
    def create_invitations(self):
        return BohoInvitation()
        
    def create_place_cards(self, name, last_name):
        return BohoPlaceCard(name, last_name)
        
    def create_guest_book(self):
        return BohoGuestBook()

        