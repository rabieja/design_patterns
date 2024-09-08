# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:59:30 2024

@author: Agnieszka Rabiej
"""

from prototype.class_schedule import ClassSchedule

class PrototypeTest:
    
    @staticmethod
    def run():
        class_schedule = ClassSchedule('Agnieszka', 'Rabiej', math= ['Monday', '18.00'], history=['Friday', '19.00'])
        new_class_schedule = class_schedule.clone()
        new_class_schedule.name = 'Monika'
        new_class_schedule.last_name = 'Krawczyk'
        setattr(new_class_schedule, 'geography', ['Wednesday', '17.00'])
        print(class_schedule)
        print(new_class_schedule)
        

if __name__ == "__main__":
    PrototypeTest.run()
        
    
        
        