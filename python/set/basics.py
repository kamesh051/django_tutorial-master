x = {(10,20,30),(40,50,60),(70,80,90)}
print x
for p in x:
    print p,type(p)
    for q in p:
        print q,type(q)
y = {10,20,30}
print y
y.add(40)
print(y)
z = y.copy()
print z
z.discard(40)
print z
z.remove(10)
print z
z.pop()
z.pop()
print z

