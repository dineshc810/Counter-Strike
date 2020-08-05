# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:16:54 2020

@author: Dinesh.Choudhary
"""

import gun
import player

gun_dict={}

player_dict={player.Terrorist:[player.T1,player.T2],
             player.CounterTerrorist:[player.CT1,player.CT2]
             }

def search_player_in_dict(player_dict,input_):
    for k in player_dict.keys():
        if input_==k.__name__.lower():
            return k
        elif isinstance(player_dict[k],list):
            for i in player_dict[k]:
                if input_==i.__name__.lower():
                    return i

def input_player_type():
    input_=input().lower()
    return search_player_in_dict(player_dict,input_)
    

    
def get_player():
    print("Enter the player type: " )
    for pt in player_dict:
        print(pt.__name__)
    player_type = input_player_type()
    if player_type=='terrorist':
        return get_terrorist() 
    elif player_type=='CounterTerrorist':
        return get_counterterrorist()
    

    
def get_terrorist():
    print("Enter the sub-player type: " )
    for spt in player_dict[player.Terrorist]:
        print(spt.__name__)
    player_sub_type = input_player_type() 
    return player_sub_type
        
        
def get_counterterrorist():                                                                 
    print("Enter the sub-player type: " )
    for spt in player_dict[player.CounterTerrorist]:
        print(spt.__name__)
    player_sub_type = input_player_type() 
    return player_sub_type

def print_user_details():
    pass    
    


    
#main
    
get_player()


    