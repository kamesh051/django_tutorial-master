class X(object):
    def m1(self):
        print("in m1 method")
class Y(X):
    def m2(self):
        print("in m2 method")

y1 = Y()
k = y1.__hash__()
print k
y1.m1()
y1.m2()
