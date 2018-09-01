class Bank:
    """SBI APPLICATION"""
    bname = 'SBI'
    
    def __init__(self,cname,cadd,cacc,cbal):
        self.cname = cname
        self.cadd  = cadd
        self.cacc  = cacc
        self.cbal  = cbal
    def deposit(self,dbal):
        self.cbal +=dbal
    def withdraw(self,wbal):
        self.cbal -=wbal
    def display(self):
        print(Bank.bname)
        print(self.cname)
        print(self.cadd)
        print(self.cacc)
        print(self.cbal)
        
d1=Bank("kamesh reddy","ameerpet",19010100113426,10000.00)
d1.deposit(1000.00)
d1.withdraw(2000.00)
d1.display()

d2=Bank("maniteja","ameerpet",32041392208,100000.00)
d2.deposit(10000.00)
d2.withdraw(20000.00)
d2.deposit(500000.00)
d2.display()

