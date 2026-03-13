'''
Read a number from user 

n = int(input())
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count+= 1
print(count)
'''
'''
Given a signed 32-bit integer x, return x with its digits reversed.If reversing x causes the value to
 go outside the signed 32-bit integer range [-2^31,2^31,-1],then return 0.
 
n = int(input())
print(int(str(n)[: : -1]))
'''
'''
n = int(input())
if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1 * int(str(n)[::-1]))'''
#check whether a given number is prime or not
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

