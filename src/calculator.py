from .data_fetcher import fetch_items
from .search import search, find_AH, get_data

idata = fetch_items()

#Price Table
#Price of Health 1/Ruby Crystal
H = idata["1028"]['gold']['total']/idata["1028"]['stats']['FlatHPPoolMod']
#Price of Armor 1/Cloth Armor
AR = idata["1029"]['gold']['total']/idata["1029"]['stats']['FlatArmorMod']
#Price of Magic Resistance 1/Null-Magic Mantle
MR = idata["1033"]['gold']['total']/idata["1033"]['stats']['FlatSpellBlockMod']    
#Price of Attack 1/Long Sword
AD = idata["1036"]['gold']['total']/idata["1036"]['stats']['FlatPhysicalDamageMod']
#Price of Ability Power 1/Amplifying Tome
AP = idata["1052"]['gold']['total']/idata["1052"]['stats']['FlatMagicDamageMod']
#Price of Attack Speed 1%/Dagger
AS = idata["1042"]['gold']['total']/idata["1042"]['stats']['PercentAttackSpeedMod']
#Price of Ability Haste 1/Glowing Mote
AH = idata["2022"]['gold']['total']/find_AH(idata["2022"]['description'])
#Price of Mana 1/Sapphire Crystal
M = idata["1027"]['gold']['total']/idata["1027"]['stats']['FlatMPPoolMod'] 
#Price of Critical Chance 1%/Cloak of Agility
C = idata["1018"]['gold']['total']/idata["1018"]['stats']['FlatCritChanceMod']
#Price of Speed 1/Boots
S = idata["1001"]['gold']['total']/idata["1001"]['stats']['FlatMovementSpeedMod']

def calculate():
    pstat = {}
    stat_price = 0

    mapping = {
        'FlatHPPoolMod': ('Health', H),
        'FlatPhysicalDamageMod': ('Attack', AD),
        'PercentAttackSpeedMod': ('Attack Speed', AS),
        'FlatArmorMod': ('Armor', AR),
        'FlatSpellBlockMod': ('Magic Resistance', MR),
        'FlatMagicDamageMod': ('Ability Power', AP),
        'FlatMPPoolMod': ('Mana', M),
        'FlatCritChanceMod': ('Critical Chance', C),
        'AbilityHaste': ('Ability Haste', AH),
        'FlatMovementSpeedMod': ('Speed', S)
    }

    # calculate for stat
    for key, value in stat.items():
        if key in mapping:
            name, unit_price = mapping[key]
            total = value * unit_price
            pstat[name] = total
            stat_price += total

    option_price = price - stat_price
    pstat["Stat Price"] = stat_price
    pstat["Option Price"] = option_price

    pstat = {k: round(v, 1) for k, v in pstat.items()}

    return pstat

#get item info
def get_iinfo():
    global ifind
    global i_info
    global price
    global stat
    global tag
    try:
        ifind = search(input("Search: "), idata)
        i_info = get_data(ifind, idata)
        price = i_info[0]
        stat = i_info[1]
        tag = i_info[2]
    
        #find AH
        if 'AbilityHaste' in tag or 'CooldownReduction' in tag:
            stat["AbilityHaste"] = find_AH(i_info[3])

        print("Price: " + str(price))
        print(calculate())
        #print(tag)
    except KeyError:
        print("Item Do not Exists")