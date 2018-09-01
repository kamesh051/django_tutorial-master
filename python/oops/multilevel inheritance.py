class X(object):
    def m1(self):
        print("in m1 method")
class Y(X):
    def m2(self):
        print("in m2 method")
class Z(Y):
    def m3(self):
        print("in m3 method")
        
z1 =Z()
k = z1.__hash__()
print k
z1.m1()
z1.m2()
z1.m3()
