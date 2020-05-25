a=int(input("enter a number o find sum of digit"))
sum=0
sd=1
while(a>0):
	rem=a%10
	sum=sum+rem
	a=a//10
while(sum>9):
	rem=sum%10
	sd=sd+rem
	sum=sum//10
print("sum of digit is",sd)