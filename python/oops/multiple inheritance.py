class X(object):
    def m1(self):
        print("in m1 method x")
class Y:
    def m1(self):
        print("in m1 method y")
class Z(Y,X): #problem in multiple inheritance
    def m3(self):
        print("in m3 method")


z1 =Z()
k = z1.__hash__()
print k
z1.m1()
z1.m1()

