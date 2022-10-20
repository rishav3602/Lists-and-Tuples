list = list()
n = int(input("Enter the number of items you want to add in the list : "))
for i in range(n):
    items = input("Enter the items you want to add to the list : ")
    list = list + [items]
    print(list)

print(list)

if "apple" in list :
    print("It is present in the list you made.")
else:
    print("It is not present in the list.")
    list = list + ["apple"]
print(list)

