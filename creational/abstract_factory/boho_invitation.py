# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:10:28 2024

@author: Agnieszka Rabiej
"""

from creational.abstract_factory.invitation import Invitation

class BohoInvitation(Invitation):
    
    def print_invitation_content(self):
        print("Boho Invitation")