#Armstrong number 
'''
n = int(input())
l = len(str(n))
res = 0
for i in str(n):
    res +=int(i) ** l

print("Armstrong" if n == res else "not Armstrong")
'''
#Perfect number
n = int(input())
s = 0
for i in range(1,n//2 + 1):
    if n % i == 0:
        s += i
print("perfect" if n == s else "not perfect")