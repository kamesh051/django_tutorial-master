import re
print("enter into python world")
regex = r"([a-zA-Z]+)"
x = open("hindu.txt")
data = x.read()
matches = re.findall(regex,data)
for i in matches:
    print ([i])
