# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:16:54 2020

@author: Dinesh.Choudhary
"""

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
       
def get_player_type():
    print("Enter the player type: " )
    for pt in player_dict:
        print(pt.__name__)
    player_type = input_player_type()
    return get_player_sub_type(player_type.__name__,player_type)
        
def get_player_sub_type(a,b):
    print(f'Enter the {a} type: ')
    for spt in player_dict[b]:
        print(spt.__name__)
    player_sub_type = input_player_type() 
    return a,player_sub_type.__name__
         
def print_user_details(x,y):
    print(f'The player type is: {x} and player sub-type is : {y}')
    
  
#main
x,y=get_player_type()
print_user_details(x,y)

    