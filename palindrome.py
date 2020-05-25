n=int(input("Enter a number to check whether a given number is palindrome or not:"))
temp=n
sum=0
while(temp>0):
	rem=temp%10
	sum=sum*10 +rem
	temp=temp//10
if sum==n:
	print("{0} is palindrome number".format(n))
else:
	print("{0} is not a palindrome number".format(n))