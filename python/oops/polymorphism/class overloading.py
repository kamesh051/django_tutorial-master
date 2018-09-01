class X:
    def m1(self):
        print("in m1 of x class-no param")
class Y(X):
    def m1(self,a):
        print("in m1 of y class-one param")
class Z(Y):
    def m1(self,a,b):
        print("in mi of z class-two param")
z1 = Z()
z1.m1(10,10)
