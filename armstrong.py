num=int(input("enter a number to check whether it is armstrong  number or not::"))
sum=0
temp=num
while temp > 0:
	rem=temp%10
	sum=sum+rem*rem*rem
	temp=temp//10
if num==sum:
	print("{0} is armstong number".format(num))
else:
	print("{0} is not armstrong".format(num))
