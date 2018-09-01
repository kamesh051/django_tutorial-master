import random
import sys
import string

def input(help_text="Do you want me to help you with a password? \n"):
	return (str(raw_input(help_text)))

def main():
	a = []
	while True:
		x = input()
		if x == "yes":
			while True:
				z = input("How many characters, between 3 and 50, do you want it to have? \n")
				if not z.isdigit() or int(z)<3 or int(z)>50:
					print "please use a number between 3 and 50!"
				else: 			
					while True:
						y = input("Do you want it to be a weak, medium, strong or insane password? \n")
						if y!="weak" and y!="medium" and y!="strong" and y!="insane":
							print "please use weak/medium/strong/insane "
						elif y == "weak":
							for i in xrange(int(z)):
								b = [random.choice(string.ascii_lowercase)]
								a.append(random.choice(b))	
							print "how about: \n", "".join(a)
							sys.exit()
						elif y == "medium":
							for i in xrange(int(z)):
								b = [random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase)]
								a.append(random.choice(b))	
							print "how about: \n", "".join(a)
							sys.exit()
						elif y == "strong":
							for i in xrange(int(z)):
								b = [random.choice(string.ascii_lowercase),random.choice(string.digits),random.choice(string.ascii_uppercase)]
								a.append(random.choice(b))	
							print "how about: \n", "".join(a)
							sys.exit()
						elif y == "insane":
							for i in xrange(int(z)):
								b = [random.choice(string.digits), random.choice(string.ascii_lowercase), random.choice("-_?!/.,';][)(~`@#$%^&*+|"),random.choice(string.ascii_uppercase)]
								a.append(random.choice(b))	
							print "how about: \n", "".join(a)
							sys.exit()		
		elif x == "no":
			print "Ok, goodbye!"
			sys.exit()
		else:
			print " please use yes or no!"

main()
