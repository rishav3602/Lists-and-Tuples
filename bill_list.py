# total cost without using loops

flipkart = [["bracelet",200],["watch",600],["laptop",40000]]
total_cost = 0
total_cost = flipkart[0][1] + flipkart[1][1] + flipkart[2][1]
print(total_cost)


# total cost using a loop

#for loop

flipkart = [["bracelet",200],["watch",600],["laptop",40000]]
total_cost = 0
for i in range(len(flipkart)):
    print(flipkart[i][1])
    total_cost = total_cost + flipkart[i][1]

print(total_cost)



flipkart = [["bracelet",200],["watch",600],["laptop",40000]]
total_bill = 0
for items in flipkart:
    print(items[0])
    total_bill = total_bill + items[1]
    print(f"Flip cart after adding : {items[1]} | Cost of the item : {total_bill} ")

print(f"Total amount you have to pay : {total_bill}")


# while loop

flipkart = [["bracelet",200],["watch",600],["laptop",40000]]
total_amount = 0
i = 0
while i <= len(flipkart):
    print(i)
    total_amount = total_amount + flipkart[i][1]
    # print(f"Flip cart after adding : {flipkart[i][0]} | Cost of the item : {flipkart[i][1]} ")
    i = i + 1
    print(f"Total amount to be paid is : {total_amount}")

print(f"Total amount to be paid is : {total_amount}")