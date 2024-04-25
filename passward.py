for i in {5,4,2,3,"hi","aa",1.0,"aabc",2,0}:
    print(i,end=" ")

for q in range(1,10):
    print(q,end="")
print (list(range(1,10,-1)))


l=[1,2,3,4,5,6,7,8,9]
for a in {'one':1,'two':2,'three':3,"four":4}:
    print(a,end=" ")


l=[1,2,3,4,5,6,7,8,9]
for a,b in enumerate(l):
    print(a,b)

username=['krishna','bhavani']
password=['123','1234']
name=input('Enter your name:')
for a,b in enumerate(username):
    print(a,b)
    if b==name:
        password=input('Enter your password:')
        print('welcome')


rows=int(input("Enter downward Triangle pattern rows ="))
print("downward Triangle star pattern")
for i in range(rows,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print()

