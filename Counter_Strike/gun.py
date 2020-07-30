# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:16:41 2020

@author: Dinesh.Choudhary
"""

class Gun:
    def __init__(self):
        self.type=self.__class__.__name__
     
        
class Pistol(Gun):
    def __init__(self):
        self.type=f'{Gun.__name__}:{self.__class__.__name__}'

class Rifle(Gun):
    def __init__(self):
       self.type=f'{Gun.__name__}:{self.__class__.__name__}'



class Flare_Gun(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'
    
class Deagle(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'      

class Skorpion(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'      

class Assault_Rifle(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'
 
class Sniper(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'
        
class Shotgun(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'

class Machinegun(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'        
        
class Groza(Assault_Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Assault_Rifle.__name__}:{self.__class__.__name__}'
        
class AK47(Assault_Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Assault_Rifle.__name__}:{self.__class__.__name__}'
        
class AWM(Sniper):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Sniper.__name__}:{self.__class__.__name__}'

class M24(Sniper):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Sniper.__name__}:{self.__class__.__name__}'   
        
class DBS(Shotgun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Shotgun.__name__}:{self.__class__.__name__}'
  
class S686(Shotgun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Shotgun.__name__}:{self.__class__.__name__}'  
        
class MG42(Machinegun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Machinegun.__name__}:{self.__class__.__name__}' 
  
class ThompsonMG(Machinegun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Machinegun.__name__}:{self.__class__.__name__}'   
        
