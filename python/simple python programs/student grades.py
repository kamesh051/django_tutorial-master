x1 = int(input('enter telugu marks'))
x2 = int(input('enter hindi marks'))
x3 = int(input('enter english marks'))
x4 = int(input('enter maths marks'))
x5 = int(input('enter science marks'))
x6 = int(input('enter social marks'))

avg = (x1+x2+x3+x4+x5+x6)/6
print(avg)

if (avg >= 90):
    print("Grade A")
elif (avg < 90 and avg >= 80):
    print("Grade B")
elif (avg < 80 and avg >= 70):
    print("Grade C")
elif (avg < 70 and avg >= 60):
    print("Grade D")
else:
    print("Grade E")
