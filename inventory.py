inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# ------------------------------Functions---------------------------------------

# 1
def display_inventory(inventory) :

    print("Inventory:")

    for key in inventory :
        print(str(inventory[key]) + ' ' + key)

    print("Total number of items: " + str(sum(inventory.values())) + '\n')

# 2
def add_to_inventory(inventory, added_items) :

    for key in added_items :
        if key in inventory :
            inventory[key] += 1
        else :
            inventory[key] = 1

# 3
def print_table(order = "") :

    if order == "count,asc" :
        ordered = sorted(inv.values())
    elif order == "count,desc" :
        ordered = reversed(sorted(inv.values()))
    else :
        ordered = inv.values()

    width_key = []
    for item in inv.keys():
        width_key.append(len(item))
    max_width_key = max(width_key)

    width_value = []
    for item in inv.values():
        width_value.append(len(str(item)))
    max_width_value = max(width_value)

    max_width = max_width_key + max_width_value + 9

    dict_to_destroy = dict(inv)

    print("Inventory:")
    print(((" ")*2) + "count" + (" ")*(max_width-(len("count")+len("item name")
    +2)) + "item name")
    print(("-")*max_width)

    for value in ordered:
        for key in dict_to_destroy : #rope #torch...
            if value == dict_to_destroy[key] :
                print((" ")*(7-len(str(value))) + (str(value) +
                (" ")*(max_width-7-len(str(key))) + str(key)))
                dict_to_destroy[key] = 0

    print(("-")*max_width)
    print("Total number of items: " + str((sum(inv.values()))) + '\n')

# 4
def import_inventory(filename) :

    opened_file = open(filename, 'r')
    read_items = opened_file.readlines()

    for item in read_items[1:] :

        slicing_point = item.index(',')
        key = item[:slicing_point]
        value = item[slicing_point + 1:]

        if key in inv :
            inv[key] += int(value)
        else :
            inv[key] = int(value)

    opened_file.close

# 5
def export_inventory(filename = "") :

        if filename != "" :
            opened_file = open(filename, 'w')
        else :
            opened_file = open('export_inventory.cvs', 'w')

        opened_file.write("item_name,count"+'\n')

        for key in inv :
            opened_file.write(str(key) + ',' + str(inv[key]) + '\n')

        opened_file.close

#-----------------------------main----------------------------------------------

def test_all_functions() :

    display_inventory(inv)

    add_to_inventory(inv, dragon_loot)

    display_inventory(inv)

    print_table("count,desc")

    print_table("count,asc")

    print_table()

    import_inventory('inventory.cvs')

    display_inventory(inv)

    print_table("count,desc")

    export_inventory('expinv.cvs')

    export_inventory()

#-------------------------test all fuctions-------------------------------------

test_all_functions()
