# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:35:53 2024

@author: Agnieszka Rabiej
"""

from abstract_factory.rustic_printing_house import RusticPrintingHouse
from abstract_factory.boho_printing_house import BohoPrintingHouse

class AbstractFactoryClient:
    
    @staticmethod
    def run():
        factory_type = input('Choose Rustic or Boho type: ')
        factory = AbstractFactoryClient.get_factory(factory_type)
    
        invitation = factory.create_invitations()
        place_card = factory.create_place_cards('Karolina', 'Krawiecka') 
        guest_book = factory.create_guest_book()
        
        invitation.print_invitation_content()
        place_card.print_guest_name()
        print(guest_book.get_guest_book_style())
            
    @staticmethod
    def get_factory(type):    
        if type == 'Rustic':
            return RusticPrintingHouse()
        elif type == 'Boho':
            return BohoPrintingHouse()
        else:
            raise ValueError('Unknown factory type.')
        

if __name__ == "__main__":
    AbstractFactoryClient.run()