def armstrong():
    num=int(input("enter a number:"))
    arms=str(num)
    result=0
    for i in arms:
        result=result+int(i)**len(arms)
    print(result)
    if result==num:print("armstrong")
    else:print("not armstrong")
armstrong()


def armstrong_by_lambda():
    num=int(input("enter a number:"))
    arms=str(num)
    result=list(map(lambda a:int(a)**len(arms),arms))
    final=0
    for i in result:final=final+i
    print(final)
armstrong_by_lambda()

with open('example.txt', 'w+') as file:
    file.write('hello')
    print(file.tell())
    print(file.read())

with open('example.txt', 'w+') as file:
    file.write('hello')
    print(file.seek(1))
    print(file.read())


l=[1,2,3,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])


l=[1,2,3,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k])