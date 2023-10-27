#class inventory
#Attributes: item_id, item_name, stock_count, item_price using dictionary inventory
# methods: add_item, update_item, minus_item, check_item_details

class Inventory_System():
    def __init__(self):
        self.xyz_inventory = {}


#add item method and check for duplicate
    def add_item(self, Item_ID, Item_Name, Stock_Count, Item_Price):
        if Item_ID not in self.xyz_inventory:
            self.xyz_inventory[Item_ID] = {
                "Item_Name" : Item_Name,
                "Stock_Count" : Stock_Count,
                "Item_Price" : Item_Price
            }

        else:
            print(f"Item with ID: {Item_ID} already exist in the inventory, modify with update_item.")

#update item method and check for unavailability in inventory
    def update_item(self, Item_ID, Stock_Count, Item_Price):
        if Item_ID in self.xyz_inventory:
            self.xyz_inventory[Item_ID]['Stock_Count'] += Stock_Count
            self.xyz_inventory[Item_ID]['Item_Price'] = Item_Price

        else:
            print("Item not found in the inventory.")

#check item details method and check non-availability in inventory
    def check_item_details(self, Item_ID):
        if Item_ID in self.xyz_inventory:
            item = self.xyz_inventory[Item_ID]
            print(f"Item Name: {item['Item_Name']}")
            print(f"Stock Count: {item['Stock_Count']}")
            print(f"Price: ${item['Item_Price']:.2f}")

        else:
            print("Item not found in inventory.")

#minus item details method and check insufficient item in stock and inventory
    def minus_item(self, Item_ID, quantity):
        if Item_ID in self.xyz_inventory:
            if self.xyz_inventory[Item_ID]['Stock_Count'] >= quantity:
                self.xyz_inventory[Item_ID]['Stock_Count'] -= quantity

            else:
                print("Insufficient item in stock")

        else:
            print("Item not found in inventory")



#USAGE
xyz_inventory = Inventory_System()


xyz_inventory.add_item("001", "Note Book", 100, 2.99)
xyz_inventory.add_item("002", "MacBook", 10, 554.99)
xyz_inventory.add_item("003", "iPhone 15", 50, 1446.99)
xyz_inventory.add_item("004", "HP Laptop", 70, 409.95)
xyz_inventory.add_item("005", "Sneaker", 20, 150.99)

xyz_inventory.update_item("003", 20, 1239.99)
xyz_inventory.update_item("001", 55, 2.50)
xyz_inventory.update_item("007", 9, 100.99) #prints "Item not found in inventory"

xyz_inventory.check_item_details("002")
xyz_inventory.check_item_details("004")
xyz_inventory.check_item_details("006") #prints "Item not found in inventory"


xyz_inventory.minus_item("005", 5)
xyz_inventory.minus_item("004", 20)
xyz_inventory.minus_item("002", 15) # prints insufficient item in stock