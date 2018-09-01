class X(object):
    def m1(self):
        print("in m1 method")
class Y:
    def m2(self):
        print("in m2 method")
class Z:
    def m3(self):
        print("in m3 method")
class A(X,Y):
    def m4(self):
        print("in m4 method")
class B(Y,Z):
    def m5(self):
        print("in m5 method")
class M(A,B):
    def m6(self):
        print("in m6 method")
        
z1 =M()
k = z1.__hash__()
print k
z1.m1()
z1.m2()
z1.m3()
z1.m4()
z1.m5()
z1.m6()
