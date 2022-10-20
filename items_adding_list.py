Grocery_list = list()
n = int(input("Enter the number of items you want to buy this diwali : "))
for i in range(n):
    enter_items = input("Enter the item : ")
    Grocery_list = Grocery_list + [enter_items]
    print(i,Grocery_list)

print(f" Your list has these items :{Grocery_list}")
 
new_items = input("Enter the new item : ")
if new_items in  Grocery_list:
    print("New items is already present in the list ")
else:
    Grocery_list = Grocery_list + [new_items]
print(f" New updated list is : {Grocery_list}")
