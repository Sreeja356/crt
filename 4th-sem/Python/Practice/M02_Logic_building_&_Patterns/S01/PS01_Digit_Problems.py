'''
1)write a python code to count the digits of number?
Ex: 15678-->output: 5

2) sum of the digits of a number?
Ex: 12345-->1+2+3+4+5 = 15'''
'''num = int(input("Enter a number:"))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //=10
print("Sum of digits:",sum_digits)'''

'''3)product of digits?
num =int(input("Enter a number"))
product = 1
while num > 0:
    product *= num %10
    num //= 10
print(product)'''
'''
4)Reverse the number?

num = int(input("Enter a number:"))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num//=10
print("Reversed number:",reverse)'''
'''
5) Count the even odd digits?

n = int(input("Enter n"))
even = 0
odd = 0
while n>0:
    d =n%10
    if d%2 == 0:
        even +=1
    else:
        odd+=1
    n//= 10
print(even)
print(odd)'''
'''
6) print the largest digit of a number?
'''