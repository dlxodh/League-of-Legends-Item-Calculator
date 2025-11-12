import re

#아이템 코드검색
#search item code
def search(str, idata):
    str = str.replace(" ","")
    for item in list(idata.keys()):
        name = idata[item]["name"].replace(" ","")
        colloq = idata[item]["colloq"].replace(" ","")
        if (str in name or str in colloq) and idata[item]["maps"]["11"]:
            return item
        
#아이템 정보 가져오기 
# get item data
def get_data(item_code, idata):
    return idata[item_code]['gold']['total'], idata[item_code]['stats'],idata[item_code]['tags'],idata[item_code]['description']

#스킬가속값 찾기
#find AH
def find_AH(description):
    # 한글 버전: "스킬 가속 <attention>15</attention>"
    match_kr = re.search(r"스킬\s*가속\s*<attention>(\d+)</attention>", description)
    if match_kr:
        return int(match_kr.group(1))

    # 영어 버전: "<attention>15</attention> Ability Haste"
    match_en = re.search(r"<attention>(\d+)</attention>\s*Ability\s*Haste", description)
    if match_en:
        return int(match_en.group(1))

    return 0