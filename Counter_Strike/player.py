# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:15:48 2020

@author: Dinesh.Choudhary
"""

class Player:
    def __init__(self):
        self.type=self.__class__.__name__


class Terrorist(Player):             
    def __init__(self):
        self.type=f'{Player.__name__}:{self.__class__.__name__}'
        
class Counter_Terrorist(Player):             
    def __init__(self):
        self.type=f'{Player.__name__}:{self.__class__.__name__}'


        
class T1(Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Terrorist.__name__}:{self.__class__.__name__}'
        
class T2(Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Terrorist.__name__}:{self.__class__.__name__}'
        
class CT1(Counter_Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Counter_Terrorist.__name__}:{self.__class__.__name__}'
        
class CT2(Counter_Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Counter_Terrorist.__name__}:{self.__class__.__name__}'
    

                                 