class Kamesh():
    a = 1000
    b = 2000
    def __init__(self):
        self.a = 10
        self.b = 20
        print(self.a+self.b)
    def sum1(self):
        sum1 = self.a+self.b
        print(sum1)
c1 = Kamesh()
print(c1)
c1.sum1()
print(Kamesh.a)
del c1
print(c1)
