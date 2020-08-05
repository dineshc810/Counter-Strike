import gun
import player

#player
    
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



#gun

gun_dict = {gun.Pistol: [gun.FlareGun, gun.Deagle, gun.Skorpion],
            gun.Rifle: {gun.AssaultRifle: [gun.AK47, gun.Groza],
                        gun.Sniper: [gun.AWM, gun.M24], 
                        gun.Shotgun:[gun.DBS, gun.S686],
                        gun.Machinegun:[gun.MG42, gun.ThompsonMG] }
           }

def search_gun_in_dict(d, input_):
    for k in d.keys():
        if input_ == k.__name__.lower():
            return k
        if isinstance(d[k], list):
            for i in d[k]:
                if input_ == i.__name__.lower():
                    return i.__name__
        elif isinstance(d[k], dict):
            return search_gun_in_dict(d[k], input_)
        else:
            raise RuntimeError('input_gun_type: expected list or dict.')
    raise RuntimeError('input_gun_type: execution shouldn\'t reach here')

def input_gun_type():
    input_ = input().lower()
    return search_gun_in_dict(gun_dict, input_)

def get_gun_type():
    return get_pistol(), get_rifle()

def get_pistol():
    print('Enter pistol type -')
    for pst in gun_dict[gun.Pistol]:
        print(pst.__name__)
    pistol_sub_type = input_gun_type()
    return pistol_sub_type

def get_rifle():
    print('enter rifle type -')
    for rt in gun_dict[gun.Rifle].keys():
        print(rt.__name__)
    rifle_type = input_gun_type()
    print('enter rifle sub type - ')
    for rst in gun_dict[gun.Rifle][rifle_type]:
        print(rst.__name__)
    rifle_sub_type = input_gun_type()
    return rifle_sub_type

def print_users_details(pistol, rifle):
    print(f'Pistol chosen by user is - {p}')
    print(f'Rifle chosen by user is - {r}')





# main

x,y=get_player_type() 
p, r = get_gun_type()
print_user_details(x,y)  
print_users_details(p, r)

