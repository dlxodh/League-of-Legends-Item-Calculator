from .data_fetcher import fetch_items
from .search import search, find_AH, get_data

# Price table baselines: stat_key -> (item_id, display_name)
# idata and prices are now computed inside get_iinfo() so that
# changing config.lang takes effect immediately on the next search.
BASELINE = {
    'FlatHPPoolMod':         ("1028", "Health"),
    'FlatPhysicalDamageMod': ("1036", "Attack"),
    'PercentAttackSpeedMod': ("1042", "Attack Speed"),
    'FlatArmorMod':          ("1029", "Armor"),
    'FlatSpellBlockMod':     ("1033", "Magic Resistance"),
    'FlatMagicDamageMod':    ("1052", "Ability Power"),
    'FlatMPPoolMod':         ("1027", "Mana"),
    'FlatCritChanceMod':     ("1018", "Critical Chance"),
    'FlatMovementSpeedMod':  ("1001", "Speed"),
}

def build_price_table(idata):
    table = {}
    for stat_key, (item_id, label) in BASELINE.items():
        cost = idata[item_id]['gold']['total']
        unit = idata[item_id]['stats'][stat_key]
        table[stat_key] = (label, cost / unit)

    # Ability Haste is not in the stats dict — parse from description
    ah_item = idata["2022"]
    ah_val = find_AH(ah_item['description'])
    table['AbilityHaste'] = ('Ability Haste', ah_item['gold']['total'] / ah_val)

    return table

def get_iinfo():
    # Fetch fresh data using whatever config.lang is set to RIGHT NOW
    idata = fetch_items()
    price_table = build_price_table(idata)

    try:
        item_id = search(input("Search: "), idata)
        price, stat, tag, desc = get_data(item_id, idata)

        stat = dict(stat)  # copy so we don't mutate the API data
        if 'AbilityHaste' in tag or 'CooldownReduction' in tag:
            stat["AbilityHaste"] = find_AH(desc)

        pstat = {}
        stat_price = 0
        for key, value in stat.items():
            if key in price_table:
                label, unit_price = price_table[key]
                gold = value * unit_price
                pstat[label] = round(gold, 1)
                stat_price += gold

        pstat["Stat Price"]   = round(stat_price, 1)
        pstat["Option Price"] = round(price - stat_price, 1)

        print("Price: " + str(price))
        print(pstat)

    except (KeyError, TypeError):
        print("Item does not exist")