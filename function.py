def fun(n):
    print(n)
    if n==7:
        return 5
    fun(n+1)
fun(1)

def fun(n):
    if n==4:
        return 5
    print(fun(n+1))
fun(1)


def my_decorator(func):
    def wrapper():
        print("something is happening before the function calling")
        func()
        print("something is happening after the function calling")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()

def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
clouser=outer_function(10)
print(clouser(5))


def fun(a,b,c):
    print(a,b,c)
fun(a=20,b=10,c=30)


def fun(*a,b):
    print(a)
    print(b)
fun(10,20,30,40,b=25)


name=input("enter your name : ")
print(name[-1]+name[:-1])
name=input("enter your name : ")
print(name[1:]+name[0])


l=[]
l.append(5)
l.append(6)
l.extend({'name':'bhavani','name':'bhanu','age':20})
print(l,len(l))










