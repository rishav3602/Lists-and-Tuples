l = ["Rishav",6,89,"box",True,76.34]
print(len(l)) #prints the length of the list.

# Creating an empty list.

my_list = list() #recommended
list = [] #not recommended
print(type(my_list))
print(type(list))
# print(max(l)) # will throw an error cause there is no comparison between int and string

for i in range (3):
    inp = int(input("Enter your items : "))
    list = list + [inp]
    print(f"item_number : {i} | current list : {list}")
    print(f"current_max : {max(list)}")
print(f"The maximum of the given list : {max(list)}")


for i in range (3):
    inp = (input("Enter your items : "))
    my_list = my_list + [inp]
    print(f"item_number : {i} | current list : {my_list}")
    print(f"current_max : {max(my_list)}")
print(f"The maximum of the given list : {max(my_list)}")