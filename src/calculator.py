from .data_fetcher import fetch_items
from .search import search, find_AH, get_data

idata = fetch_items()

#기준표 가장 싼 아이템의 가격/스탯
#체력 1의 가격/루비수정
H = idata["1028"]['gold']['total']/idata["1028"]['stats']['FlatHPPoolMod']
#방어력 1의 가격/천갑옷
AR = idata["1029"]['gold']['total']/idata["1029"]['stats']['FlatArmorMod']
#마저 1의 가격/마법무효화망토
MR = idata["1033"]['gold']['total']/idata["1033"]['stats']['FlatSpellBlockMod']    
#공격력 1의 가격/롱소드
AD = idata["1036"]['gold']['total']/idata["1036"]['stats']['FlatPhysicalDamageMod']
#주문력 1의 가격/증폭의 고서
AP = idata["1052"]['gold']['total']/idata["1052"]['stats']['FlatMagicDamageMod']
#공속 1%의 가격/단검
AS = idata["1042"]['gold']['total']/idata["1042"]['stats']['PercentAttackSpeedMod']
#가속 1의 가격/빛나는 티끌
AH = idata["2022"]['gold']['total']/find_AH(idata["2022"]['description'])
#마나 1의 가격/사파이어 수정
M = idata["1027"]['gold']['total']/idata["1027"]['stats']['FlatMPPoolMod'] 
#치확 1%의 가격/민첩성의 망토
C = idata["1018"]['gold']['total']/idata["1018"]['stats']['FlatCritChanceMod']
#이속 1의 가치
S = idata["1001"]['gold']['total']/idata["1001"]['stats']['FlatMovementSpeedMod']

#계산
def calculate():
    pstat = {} #아이템의 각 스탯 가격
    stat_price = 0
    option_price = 0
    for item in list(stat.keys()):
        if item == 'FlatHPPoolMod':
            pstat["체력"] = stat[item] * H
            stat_price += stat[item] * H
        elif item == 'FlatPhysicalDamageMod':
            pstat["공격력"] = stat[item] * AD
            stat_price += stat[item] * AD
        elif item == 'PercentAttackSpeedMod':
            pstat["공격속도"] = stat[item] * AS
            stat_price += stat[item] * AS
        elif item == 'FlatArmorMod':
            pstat["방어력"] = stat[item] * AR
            stat_price += stat[item] * AR
        elif item == 'FlatSpellBlockMod':
            pstat["마법저항력"] = stat[item] * MR
            stat_price += stat[item] * MR
        elif item == 'FlatMagicDamageMod':
            pstat["주문력"] = stat[item] * AP
            stat_price += stat[item] * AP
        elif item == 'FlatMPPoolMod':
            pstat["마나"] = stat[item] * M
            stat_price += stat[item] * M
        elif item == 'FlatCritChanceMod':
            pstat["치명타확률"] = stat[item] * C
            stat_price += stat[item] * C
        elif item == "AbilityHaste":
            pstat["스킬가속"] = stat[item] * AH
            stat_price += stat[item] * AH
        elif item == "FlatMovementSpeedMod":
            pstat["고정이속"] = stat[item] * S
            stat_price += stat[item] * S
    option_price = price - stat_price
    pstat["스탯가"] = stat_price
    pstat["옵션가"] = option_price
    for item in list(pstat.keys()):
        pstat[item] = round(pstat[item],1)
    return pstat

def get_iinfo():
    #계산할 아이템 정보 불러오기
    global ifind
    global i_info
    global price
    global stat
    global tag
    try:
        ifind = search(input("검색: "), idata)
        i_info = get_data(ifind, idata)
        price = i_info[0]
        stat = i_info[1]
        tag = i_info[2]
    
        #find AH
        if 'AbilityHaste' in tag or 'CooldownReduction' in tag:
            stat["AbilityHaste"] = find_AH(i_info[3])

        print("가격: " + str(price))
        print(calculate())
        #print(tag)
    except KeyError:
        print("존재하지 않는 아이템입니다")