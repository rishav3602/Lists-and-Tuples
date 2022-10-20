A = [1,2,3,4,5]
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])

list_l = ["one","box","food",6,8,9.09,True]
print(list_l[1:])
print(list_l[:3])
print(list_l[2:6])
print(list_l[2:6:1])
print(list_l[2:6:2])
print(list_l[-1])
print(list_l[-1:4:-2])
print(list_l[-1:-5])
print(list_l[::-1])

for i in range(len(list_l)):
    print(i,list_l[i])

for items in A:
    print(items)

for j in range (len(A)):
    print(j,A[j])
