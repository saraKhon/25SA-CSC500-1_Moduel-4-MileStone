
# Sara Khon 04/13/2025 - Week 04 - MileStone

# Step 1 : create the ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name ="none"    #Sting
        self.item_price = 0.0     #float
        self.item_quantity = 0    #int


    def total_cost(self):
        return self.item_price * self.item_quantity


# This function makes the Online shopping cart invoice clear organize and easy to read
def print_Invoice(items):
    print("-" * 85)
    print("{:<10} {:<20} {:<10} {:>15} {:>15}".format("Item", "Description", "Item Quantity", "Cost Per Unit",
                                                          "Total"))
    print("-" * 85)
    grand_total = 0

    for i, item in enumerate(items):
        total = item.total_cost()
        print("{:<10}{:<30}{:<5} {:>12} {:>18}".format(
            f"Item {i + 1}", item.item_name, item.item_quantity,
            f"${item.item_price:,.2f}", f"${total:,.2f}"))

        grand_total += total

    tax = grand_total * 0.10
    final_total = grand_total + tax

    print("-" * 85)
    print("{:>70} ${:<10.2f}".format("Total Price test:", grand_total))
    print("{:>70} ${:<10.2f}".format("Junk Food Tax (10%): ", tax))
    print("{:>70} ${:<10.2f}".format("Total with Tax: ", final_total))




# PART II: Item 01
print("\n Purchase Item 01")
print("------------------------------------------------------------")
item01 = ItemToPurchase()
item01.item_name = input("Enter the name of the 1st item : \n")
item01.item_price = float(input("Enter the price: \n"))
item01.item_quantity = int(input("Enter the quantity:\n"))


#Part II: Item 02
print("------------------------------------------------------------")
print("\n Item 2 ")
item02 = ItemToPurchase()
item02.item_name = input("Enter the name of the 2nd item: \n")
item02.item_price = float(input("Enter the price: \n"))
item02.item_quantity = int(input("Enter the quantity: \n"))

# Put them in a list
items = [item01, item02]

#print
print_Invoice(items)







