# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:34:16 2024

@author: Agnieszka Rabiej
"""
from creational.singleton.user import User
from creational.singleton.admin import Admin

class SingletonTest:

    @staticmethod
    def run():
        u1 = User('Agnieszka')
        u2 = User('Michal')
        u3 = User('Karol')
        a1 = Admin('Tomasz')
        
        u1.send_message('Hello')
        u2.send_message('Hi')
        u3.send_message('czesc')   
        a1.send_message('hej')


if __name__ == "__main__":
    SingletonTest.run()