l = [1,2,3,4,5,6,7,8,9]
odd_list = list()
even_list = list()
for i in range(len(l)):
    num = l[i]
    if num % 2 == 0:
        even = num
        even_list = even_list + [even]
    else:
        odd = num
        odd_list  = odd_list + [odd]
print(f" The list of odd number is : {odd_list}")
print(f" The list of even number is : {even_list}")


