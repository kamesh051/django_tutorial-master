x = input("no of terms to print in series")
a = 0
b = 1
count = 2
print "0,1,",
while count<x:
    c = a+b
    a=b
    b=c
    print c,",",
    count +=1
