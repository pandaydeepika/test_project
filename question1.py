# INTERVIEW QUESTIONS:-
#print all list accept jessica 

student_name=["deepika","ram","shayam","govind","jessica"]
for i in student_name:
	if i!= "jessica":
# 		pass
		print(i)
		
# print and compare the list if it is match 
# 3-->[1,2,3,4,3]-True
# -1-->[1,5,3,4]-False

def compare_list(a,b):
	Is_number_matched=False
	for i in b:
		if i==a:
			Is_number_matched=True
			break
	if Is_number_matched==True:
		print("Number Found")
	else:
		print("Number not Found")
		
		
compare_list(3,[1,2,3,4,3])
compare_list(-1,[1,2,3,4])
	
#take 2 list and compare each other of in list1 is one item matched with then print true.

def single_match():
	l1=[1,2,3,4]
	l2=[4,5,6,7]
	count=0
	for i in l1:
		for j in l2:
			if i==j:
				count=count+1
				break
	if count==0:
		print("False")
	else:
		print("True")
		
		
def multiple_match():
	l1=[1,2,3,4,5]
	l2=[1,6,7,8,5]
	count=0
	for i in l1:
		for j in l2:
			if i==j:
				count=count+1
				print(i)
	if count==0:
		print("Matched not found")
	else:
		print("Matched found")
		
					
		
		
		
		
single_match()
multiple_match()
		
#QUESTIONS:-		
		
# 1
def divisible_number():
	num=[]
	for i in range(2000,3200):
		if (i%7==0) and (i%5!=0):
			num.append(i)
	print(num)
		
	
# divisible_number()

# 2
def factorial(n):
		if n>0:
			return n*factorial(n-1)	
		else:
			return 1
		 
		
# print(factorial(8))


# 2
def fabbonnaci(n):
	if n==0 or n==1:
		return n
	else:
		return fabbonnaci(n-1) + fabbonnaci(n-2)

# for n in range(10):
# 	print(fabbonnaci(n))
# 	

# 3
d=dict()
def multiple(i):
	d[i]=i*i
	
	

# for i in range(1,9):
# 	multiple(i)
print(d)


# 4
# x=input("Enter the values:").split(",")
# y=[]
# for i in x:
# 	y.append(int(i))	
# print(y)
	
# print(eval(input("Enter the values:")), )

#5
s=str(input("Enter some string:"))
s1=s.upper()
print(s1)

#6
