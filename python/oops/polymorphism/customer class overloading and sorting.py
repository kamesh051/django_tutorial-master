class Customer:
    """Bank Application"""
    cbank = "CANARA BANK"
    def __init__(self,cname,cadd,caccno,cbal):
        self.cname = cname
        self.cadd = cadd
        self.caccno = caccno
        self.cbal = cbal
    def __str__(self):
        return self.cname+" "+self.cadd+" "+str(self.caccno)+" "+str(self.cbal)
    def deposit(self,damt):
        self.cbal += damt
        return self.cbal
    def withdrawl(self,wamt):
        self.cbal -= wamt
        return self.cbal 
c1 = Customer("yamini","anakapalle",1001,5000)
c2 = Customer("chukkas","vizag",1002,3000)
c3 = Customer("rock","duggirala",1003,2000)
print "before sorting"
x = [c1,c2,c3]
for p in x:
    print p
c1.deposit(7000)
c2.withdrawl(1000)
c3.deposit(10000)
print "After sorting"
y = sorted(x ,key = lambda c:c.cbal,reverse = True)
for q in y:
    print q
