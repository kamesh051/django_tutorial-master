n = int(input("enter number of elements:"))
a=list()
for i in range(0,n):
    elem = int(input('insert elemnt'))
    a.append(elem)
print(a)
avg = (sum(a)/n)
print(round(avg,5))
