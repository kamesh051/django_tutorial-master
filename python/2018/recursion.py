i=1
count=0
def func():
	print("hi")
	global i,count
	while i<9:
		
		i+=1
		count+=1
		print(i)
		func()
x=func()
print(x)
print(count)
print("i=",i)