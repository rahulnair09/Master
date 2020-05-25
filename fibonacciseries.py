n=int(input("enter a number for last end  range:"))
first=0
second=1
i=0
print(first)
print(second)
for i in range(2,n):
	third=first+second
	print(third)
	first=second
	second=third
	i+=1