a=int(input("Enter  first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third nunber:"))
if a>b and a>c:
	print("{0} js greater".format(a))
elif b>a and b>c:
	print("{0} is greater".format(b))
else:
	print("{0} is greater".format(c))