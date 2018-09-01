class demo:
    """non static variables"""
    def __init__(k):
        print("constructor defined")
        k.a = 100
        k.b = 200
    def m2(k):
        print(k.a)
        print(k.b)
    def m3(k):
        k.a = k.a+10
        k.b = k.b-10
d1 = demo()
print(d1)
d1.m2()
d1.m3()
d1.m2()

d2 = demo()
d3 = demo()
