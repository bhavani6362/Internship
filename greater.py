a=int(input())
b=int(input())
c=int(input())
if a>b:
    print("the 1st greater num")
elif b>c:
    print("the 2nd greater num")
elif c>a:
    print("the 3rd greater num")
else:
    print("no one")
a=10


b=10
if a>b:
    print("a is a greater")
elif a==b:
    print("equal")
else:
    print("b is a greater")
    a=10
    b=10
    if a>b and a>5:
        print("a is a greater")
    else:a==b

a=int(input("a 1"))
b=int(input("b 1"))
c=int(input("c 1"))
if a>b and a>c:
    print("a 1")
    if b>c:print("b 2\n c 3")
    else: print("c 2\n b 3")
elif b>c and b>a:
    print("b 1")
    if a>c: print("a 2\n c 3")
    else: print("c 2\n c 3")
else: print("c 1")
if b>a:print("b 2\n a 3")
else:print("a 2\n b 3")
for i in range(1,11):
        print(i ,end="")
print(list(range(1,10,2)))
for a in ("bhavani"):
    print(a)