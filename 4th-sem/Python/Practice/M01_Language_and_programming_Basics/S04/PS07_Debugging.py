''' Debugging-->Finding and Fixing of Errors
bugss -->> Errors
    Types of errors:
1.Syntax Errors-->>Missing of colon, missing of Indentation
2.Runtime Errors-->>Division by zero
3.Logical Errors-->>Missing of Logics
Debugging Techniques:
    1.print()
    2.try-except
    3.using pdb
    pdb--> python debugger
    1)pause the execution code
    2)inspect the variable's value
     3)to run the code line by line
      pdb commands:
    1)n -->to execute the output in a next line
    2)p variable -->to get the value of a variable
    3)I -->List nearby code
    4)c -->continue the execution
    5)s -->to start a function
    6)r -->return from the function 
    7)h-->help
    8)q--> quit the execution'''
'''
try:
    a = int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by zero")
except ValueError:
        print("Invalid input")'''
import pdb 
def add(a,b):
    pdb.set_trace() #set the breakpoint
    return a+b
a = int(input("enter a 1st num:"))
b = int(input("enter a 2nd num:"))