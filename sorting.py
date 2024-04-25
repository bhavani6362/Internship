#bubble sort
l=[15,7,4,9,5,2]
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

#selection sort
l=[2,7,6,3,8,1]
n=len(l)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if l[min]>l[j]:
            min=j
    l[i],l[min]=l[min],l[i]
print(l)

#Insertion sort
l=[3,5,2,8,9,1]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)
