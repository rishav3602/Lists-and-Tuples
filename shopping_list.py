# Creating a shopping list


#for loop

list_of_items_to_purchase = list()
N = int(input("Enter the number of items you need to purshase : "))
for i in range(N):
    user_input = input('Enter the items that you want to purchase : ')
    list_of_items_to_purchase = list_of_items_to_purchase + [user_input]

print(list_of_items_to_purchase)


#while loop

items_list = list()
n = int(input("Enter the number of items you want to buy : "))
i = 1
while i <= n:
    items_input = input("Enter the list of items you need to buy : ")
    items_list = items_list + [items_input]
    i = i + 1
    
print(items_list)


