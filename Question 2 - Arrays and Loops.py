inventory = []
def addItem(itemName):
    if itemName in inventory:
        print(itemName + " is already in inventory.")
    else:
        inventory.append(itemName)
def listInventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Inventory:", inventory)
       
