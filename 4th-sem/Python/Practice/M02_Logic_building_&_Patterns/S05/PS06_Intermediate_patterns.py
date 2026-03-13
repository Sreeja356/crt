'''li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i ** 2)
print(res)

li = [1,2,3,4,5]
res = []
for i in li:
    if i%2 == 0:
        res.append(i)
print(res)

print([i for i in li if i%2 == 0])

li = ['a','b','c']
res = ""
for ch in li:
    res = res + ch +" "
print(res)
print(" ".join(li))'''
#1.pyramid
'''n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)'''
#Diamond
''' int(input())
# upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)'''
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
