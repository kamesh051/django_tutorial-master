x = {"a":{1:2,3:4},
     "b":{5:6,7:8},
     "c":{9:10,11:12}}
print x
'''for p in x:
    print p
    k=x.get(p)
    print k
    for a,b in k.items():
        print a,b'''
for p in x:
    print p
    l = x.get(p)
    print l
    '''k = l.items()
    print k'''
    for a,b in l:
        print a,b

