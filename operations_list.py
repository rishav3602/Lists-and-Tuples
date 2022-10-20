A = [2,3,4,5]
B = [12,34,56,78]
c = A+B
print(c)
d = A*2
print(A*2) #double the list (not permanet)
print(A)
A = A*3 # reassigning to make it permanent
print(A)
print(B+B) #it is also allowed but not permanent
print(A*(-1)) #it will throw an empty list
e = A+B*2
print(e)
print(B*0) # it will also throw an empty list