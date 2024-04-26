class A:
    def duster(self):
        print("duster")
class B(A):
    def chalk(self):
        print("chalk")

bhavani=A()
pacchu=B()
#bhavani.chalk()
pacchu.duster()
bhavani.duster()
pacchu.chalk()