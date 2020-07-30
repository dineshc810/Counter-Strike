# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:21:07 2020

@author: Dinesh.Choudhary
"""
import player
import gun



def get_player():
    
    print("Enter the player: (Terrorist)(Counter Terrorist)")
    player_input=input()

    if player_input=='Terrorist':
        print("Enter the player type: (T1)(T2)")
        player_type_input=input()
        if player_type_input=='T1':
                return player.T1().type
        elif player_type_input=='T2':
                return player.T2().type
            
    elif player_input=='Counter Terrorist':
        print("Enter the player type: (CT1)(CT2)")    
        player_type_input=input()
        if player_type_input=='CT1':
                return player.CT1().type
        elif player_type_input=='CT2':
                return player.CT2().type
            
    
def get_gun():
    
    print("Enter the gun: (Pistol)(Rifle)")
    gun_input=input()
    if gun_input=='Pistol':
        print("Enter the gun type: (Flare gun)(Deagle)(Skorpion)")
        gun_type_input=input()
        if gun_type_input=='Flare gun':
            return gun.Flare_Gun().type
        elif gun_type_input=='Deagle':
            return gun.Deagle().type
        elif gun_type_input=='Skorpion':
            return gun.Skorpion().type
        
        
    elif gun_input=='Rifle':
        print("Enter the gun type: (Assault Rifle)(Sniper)(Shotgun)(Machine gun)")
        gun_type_input=input()
        if gun_type_input=='Assault Rifle':
            print("Enter the gun sub type: (Groza)(AK47)")
            gun_subtype_input=input()
            if gun_subtype_input=='Groza':    
                return gun.Groza().type   
            elif gun_subtype_input=='AK47':
                return gun.AK47().type  
        elif gun_type_input=='Sniper':
            print("Enter the gun sub type: (M24)(AWM)")
            gun_subtype_input=input()
            if gun_subtype_input=='M24':    
                return gun.M24().type   
            elif gun_subtype_input=='AWM':
                return gun.AWM().type  
        elif gun_type_input=='Shotgun':
            print("Enter the gun sub type: (DBS)(S686)")
            gun_subtype_input=input()
            if gun_subtype_input=='DBS':    
                return gun.DBS().type   
            elif gun_subtype_input=='S686':
                return gun.S686().type  
        elif gun_type_input=='Machinegun':
            print("Enter the gun sub type: (MG42)(Thompson MG)")
            gun_subtype_input=input()
            if gun_subtype_input=='MG42':    
                return gun.MG42().type   
            elif gun_subtype_input=='Thompson MG':
                return gun.ThompsonMG().type  
        
        
def printresult():
    x=get_player()
    y=get_gun()
    print (f'{x}---{y}')
    

printresult()




      
