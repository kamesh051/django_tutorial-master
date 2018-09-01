'''n = input("enter a number")
p = n[::-1]
print(p)'''

n = int(input("enter a number"))
rev = 0
while n>0:
    num = n%10
    print("num =",num)
    rev = rev*10 + num
    n = n//10
    print('rev',rev)
print(rev)
