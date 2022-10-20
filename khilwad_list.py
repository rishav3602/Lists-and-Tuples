suchi = [23,43,12,2,34,56,54,32]
suchi.sort() #permanently sort the list
print(suchi)
suchi.reverse() #this is also a permanent operation
print(suchi)

s2 = [67,87,45,2,34,78,54]
print(sorted(s2)) #this is not a permanent operation.
print(s2)
s2 = sorted(s2)
s2 = s2[::-1]
print(s2)

s3 = [98,67,109,56,12,34]
s3.sort(reverse=True) #descending order (permanent change)
print(s3)
print(s3[::-1]) #not a permanent operation (reassign to make it permanent)
print(s3)