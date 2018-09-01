x = [range(10000)]
for p in x:
    p
while True:
    i = input("enter element to found")
    if i in p:
        print "number found"
        break
    else:
        print "not found"
