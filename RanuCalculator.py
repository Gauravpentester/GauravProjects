import math
print("Hello I am a smart calculator Ranu\n")
print("How can i help you\n")
class calculator:
 def UserInput():
  data=input("Enter some text:")
  data=data.lower()
  if data=='whatisyourname' or data=='what is your name':
   print("My name is Ranu")
  else:
   operand=calculator.checkInput(data)
   if len(operand)==0:
    print("Please enter a valid input")
   else:
    op=calculator.CheckOperation(data)
    calculator.PerformOperation(op,operand)
 
 def PerformOperation(op,operand):
   if op=='+':
    calculator.add(operand)
   elif op=='-':
    calculator.sub(operand)
   elif op=='/':
    calculator.div(operand)
   elif op=='*':
    calculator.mult(operand)
   elif op=='hcf':
    calculator.hcf(operand)
   elif op=='lcm':
    calculator.lcm(operand)
   elif op=='square':
    calculator.square(operand)  
   elif op=='factorial':
    calculator.fact(operand)
   
  
 
 def checkInput(data):
   integers=[int(x) for x in data if x.isdigit()]
   return integers
  
 def add(operand):
  if len(operand)==2:
   print("Addition is:",operand[0]+operand[1])
  else:
   print("Please enter a valid input")
   
 def sub(operand):
  if len(operand)==2:
   print("Subtraction is:",operand[0]-operand[1])
  else:
   print("Please enter a valid input")
   
 def mult(operand):
  if len(operand)==2:
   print("Multiplication is:",operand[0]*operand[1])
  else:
   
   print("Please enter a valid input")
   
 def div(operand):
  if len(operand) == 2:
   try:
    result = operand[0] / operand[1]
    print("Division is:", result)
   except ZeroDivisionError:
    print("Cannot divide by zero!")
 def lcm(operand):
  if len(operand)==2:
   a=operand[0]
   b=operand[1]
   m=min(a,b)
   i=1
   while True:
    if m*i%a==0 and m*i%b==0:
     break
     i+=1 
   print("LCM is:",m*i)
  else:
   print("Please neter a valid input") 
   
 def hcf(operand):
  if len(operand)==2:
   print("HCF is:",math.gcd(operand[0],operand[1]))
  else:
   print("Please enter a valid input") 
 
 def square(operand):
  if len(operand)==1:
   print("Square is:",operand[0]**2)
  else:
   print("Please enter a valid input") 
 
 def fact(operand):
  if len(operand)==1:
   print("Factorial is:",math.factorial(operand[0]))
  else:
   print("Please enter a valid input") 
 

 def CheckOperation(data):
  ops_dict={ 
    'plus':'+',
    'add' :'+',
    'sum' :'+',
    'addition':'+',
    'minus':'-',
    'subtraction':'-',
    'multiply':'*',
    'multiplication':'*',
    'divison':'/',
    'divide':'/',
    'lcm':'lcm',
    'hcf':'hcf',
    '+':'+',
    '-':'-',
    '*':'*',
    '/':'/',
    'factorial':'factorial', 
    'square':'square'
    } 
  for i in ops_dict:
   if i in data:
    return ops_dict.get(i)
  else:
   print("Enter Valid Input")
    
calculator.UserInput()
 
 
''' 

how programs catches error while execution
how order of function is imp
'''
