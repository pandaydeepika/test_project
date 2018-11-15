# INTERVIEW QUESTIONS:-
#Print all list accept jessica 
 
 # student_name=["deepika","ram","shayam","govind","jessica"]
#  for i in student_name:
#  	if i!= "jessica":
#  		pass
#  		print(i)
# 		
# print and compare the list if it is match 
# 3-->[1,2,3,4,3]-True
# -1-->[1,5,3,4]-False

# def compare_list(a,b):
# 	Is_number_matched=False
# 	for i in b:
# 		if i==a:
# 			Is_number_matched=True
# 			break
# 	if Is_number_matched==True:
# 		print("Number Found")
# 	else:
# 		print("Number not Found")
# 		
		
# compare_list(3,[1,2,3,4,3])
# compare_list(-1,[1,2,3,4])
	
#take 2 list and compare each other of in list1 is one item matched with then print true.

# def single_match():
# 	l1=[1,2,3,4]
# 	l2=[4,5,6,7]
# 	count=0
# 	for i in l1:
# 		for j in l2:
# 			if i==j:
# 				count=count+1
# 				break
# 	if count==0:
# 		print("False")
# 	else:
# 		print("True")
# 		
# 		
# def multiple_match():
# 	l1=[1,2,3,4,5]
# 	l2=[1,6,7,8,5]
# 	count=0
# 	for i in l1:
# 		for j in l2:
# 			if i==j:
# 				count=count+1
# 				print(i)
# 	if count==0:
# 		print("Matched not found")
# 	else:
# 		print("Matched found")
# 		
# 					
		
		
		
		
# single_match()
# multiple_match()
		
#QUESTIONS:-		
		
# 1
# def divisible_number():
# 	num=[]
# 	for i in range(2000,3200):
# 		if (i%7==0) and (i%5!=0):
# 			num.append(i)
# 	print(num)
# 		
# 	
# # divisible_number()
# 
# # 2
# def factorial(n):
# 		if n>0:
# 			return n*factorial(n-1)	
# 		else:
# 			return 1
# 		 
# 		
# # print(factorial(8))
# 
# 
# # 2
# def fabbonnaci(n):
# 	if n==0 or n==1:
# 		return n
# 	else:
# 		return fabbonnaci(n-1) + fabbonnaci(n-2)
# 
# # for n in range(10):
# # 	print(fabbonnaci(n))
# # 	
# 
# # 3
# d=dict()
# def multiple(i):
# 	d[i]=i*i
# 	
# 	
# 
# # for i in range(1,9):
# # 	multiple(i)
# # print(d)
# 
# 
# # 4
# # x=input("Enter the values:").split(",")
# # y=[]
# # for i in x:
# # 	y.append(int(i))	
# # print(y)
# 	
# # print(eval(input("Enter the values:")), )
# 
# #5
# class Person:
# 	def __init__(self):
# 		self.name=""
# 		
# 	def getString(self):
# 		self.name=input("Enter some string:")
# 		
# 	def printString(self):
# 		print(self.name.upper())
# 		
# 	
# # p1 = Person()
# # p1.getString()
# # p1.printString()
# 		
# 
# 
# #6
# import math
# 
# class Equation:
# 	
# 	def __init__(self):
# 		self.n=""
# 	
# 	def formula(self):
# 		c=50
# 		h=30
# 		value=[]
# 		self.n=(input().split(','))
# 		items=[x for x in self.n]
# 		for d in items:
# 			value.append(int(round(math.sqrt(2*c*float(d)/h))))
# 		print(value)
# 
# 				
# p1 = Equation()
# p1.formula()
 
# #7 {Need to do}
# 
#8 
# class sentence:
# 	def __init__(self):
# 		self.name=""
# 	
# 	def getword(self):
# 		self.name=(input("Enter the list:").split(','))
# 		items=[x for x in self.name]
# 		items.sort()
# 		print(items)
# 		
# 		
# 		
# p1=sentence()
# p1.getword()
		

#9


# class sequence:
# 	def __init__(self):
# 		self.name=""
# 	
# 	def sentence_complete(self):
# 		lines=[]
# 		while True:
# 			self.name=input()
# 			if self.name:
# 				lines.append(self.name.upper())
# 			else:
# 				break
# 					
# 		return lines
# 
# 	
# p1 = sequence()
# print(p1.sentence_complete())
				


#10
# 
# class sequence:
# 	def __init_(self):
# 		self.name=""
# 		
# 	def sentence_complete(self):
# 		self.name=input("Enter the words:")
# 		words=[word for word in self.name.split(" ")]
# 		print(" ".join(sorted(list(set(words)))))
# 		
# 		
# p1=sequence()
# p1.sentence_complete()		
# 		
		
#11

# class sequence:
# 	def __init_(self):
# 		self.name=""
# 	
# 	def number_sequence(self):
# 		value=[]
# 		self.name=input("Enter the numbers:")
# 		items=[x for x in self.name.split(",")]
# 		for p in items:
# 			intp=int(p,2)
# 			if not intp%5:
# 				value.append(p)
# 				print(",".join(value))
# 			
# # 
# p1 = sequence()
# p1.number_sequence()
		
		
#12

# class number:
# 	def __init_(self):
# 		self.name=""	
# 		
# 	def even_number(self):
# 		values=[]
# 	# 	s = str(i)
# 		for i in range(1,30):
# 			if i % 2 == 0:
# 				values.append(i)
# 				print(values)
# 
# p1 = number()
# p1.even_number()


#13

# class sentence:
# 	def __init_(self):
# 		self.name=""
# 		
# 	def calculate(self):
# 		self.name=input("Enter the value:")
# 		d={"DIGITS":0, "LETTERS":0}
# 		for c in self.name:
# 			if c.isdigit():
# 				d["DIGITS"]+=1
# 			elif c.isalpha():
# 				d["LETTERS"]+=1
# 			else:
# 				pass
# 		print("LETTERS", d["LETTERS"])
# 		print("DIGITS", d["DIGITS"])
# 
# p1 = sentence()
# p1.calculate()

#14

# class sentence:
# 	def __init_(self):
# 		self.name=""
# 		
# 	def calculate(self):
# 		self.name=input("Enter the value:")
# 		d={"UPPERCASE":0, "LOWERCASE":0}
# 		for c in self.name:
# 			if c.isupper():
# 				d["UPPERCASE"]+=1
# 			elif c.islower():
# 				d["LOWERCASE"]+=1
# 			else:
# 				pass
# 		print("UPPERCASE", d["UPPERCASE"])
# 		print("LOWERCASE", d["LOWERCASE"])
# 		
# 		
# p1=sentence()
# p1.calculate()


#15

class sequence():
	def __init(self):
		self.name=""
		
	def calculate(self):
		self.name=input("Enter the number:")
		for a in self.name:
			n1 = int( "%s" % a )
			n2 = int( "%s%s" % (a,a) )
			n3 = int( "%s%s%s" % (a,a,a) )
			n4 = int( "%s%s%s%s" % (a,a,a,a))
			print (n1+n2+n3+n4)
			
p1=sequence()
p1.calculate()

#