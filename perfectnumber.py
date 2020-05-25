n=int(input("enter a number  to find whether a number is perfect number or not:"))
sum=0
for i in range(1,n):
	if (n % i==0):
		sum =sum+i
if sum==n:
	print("{0} is perfect number".format(n))
else:
	print("{0} is not perfect number".format(n))