#method over loading not supported by python

class X:
    def m1(self):
        print("in m1 of x class-no param")
    def m1(self,a):
        print("in m1 of x class-one param")
    def m1(self,a,b):
        print("in mi of x class-two param")
x1 = X()
x1.m1(10,20)
x1.m1(10)
