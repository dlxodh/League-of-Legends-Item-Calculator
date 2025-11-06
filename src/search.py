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
    des_loc_s = description.find("스킬 가속 <attention>")+17
    des_loc_e = description[des_loc_s:].find("</attention>")
    vAH = description[des_loc_s:][:des_loc_e]
    return int(vAH)