class ECE:
    def __init__(self,marks):
       self.marks=marks
    def scored(self):
        print(self.marks)
bhavani=ECE(100)
bhavani.scored()


class ECE:
    def __init__(self,marks):
        self.marks=marks
    def total(self,other):
        print(self.marks,other.marks,self.marks+other.marks)
nawaz=ECE(100)
bindu=ECE(1000)
ECE.total(nawaz,bindu)



class ECE:
    def __init__(self,*marks):
        self.m1=marks[0]
        self.m2=marks[1]
        self.m3=marks[2]
        self.m4=marks[3]
        self.m5=marks[4]
    def total(self):
        self.total=self.m1+self.m2+self.m3+self.m4+self.m5
    def rank(self,other):
        if self.total>other.total:
            print("bhavani")
        else:print("bhavana")
bhavani=ECE(100,100,100,100,100)
bhavana=ECE(80,80,80,80,80)
bhavani.total()
bhavana.total()
ECE.rank(bhavani,bhavana)



class ECE:
    def __init__(self,*marks):
        self.m1=marks[0]
        self.m2=marks[1]
        self.m3=marks[2]
        self.m4=marks[3]
        self.m5=marks[4]

class A:
    def __init__(self):
        self.b=self.B()
        self.c=self.b.C()
        self.c.fan()
    class B:
        def __init__(self):
            pass
        class C:
            def __init__(self):
                print("c")
            def fan(self):
                print("fan run")
A()


list=[1,3,4,6,8,9]
key=8
l=0
r=len(list)-1
while l<=r:
    mid=(l+r)//2
    if list[mid]==key:
        print(f"key found at the index of {mid}")
        break
    elif list[mid]>key:
        r=mid-1
    else:
        l=mid+1
if key not in list:
    print("value not found")


