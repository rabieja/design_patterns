# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:06:13 2024

@author: Agnieszka Rabiej
"""

from creational.abstract_factory.invitation import Invitation

class RusticInvitation(Invitation):
    
    def print_invitation_content(self):
        print("Rustic Invitation")