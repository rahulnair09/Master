a=int(input("enter a number o find sum of digit"))
sum=0
while(a>0):
	rem=a%10
	sum=sum+rem
	a=a//10
print("sum of digit",sum)