import re
from .config import config

#search item code
def search(str, idata):
    str = str.replace(" ", "").lower()          # lowercase the query
    for item in list(idata.keys()):
        name = idata[item]["name"].replace(" ", "").lower()      # lowercase the name too
        colloq = idata[item]["colloq"].replace(" ", "").lower()  # lowercase colloq too
        if (str in name or str in colloq) and idata[item]["maps"]["11"]:
            return item
        
# get item data
def get_data(item_code, idata):
    return idata[item_code]['gold']['total'], idata[item_code]['stats'],idata[item_code]['tags'],idata[item_code]['description']

#find AH
def find_AH(description):
    # Try Korean format first, then English — works regardless of current lang
    match = re.search(r"스킬\s*가속\s*<attention>(\d+)</attention>", description)
    if match:
        return int(match.group(1))
    match = re.search(r"<attention>(\d+)</attention>\s*Ability\s*Haste", description)
    if match:
        return int(match.group(1))
    return 0