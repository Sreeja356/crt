

'''Display Arithmetic Progression values upto 10
a = int(input())
d = int(input())
for i in range(10):
    print(a + (i*d),end=" ")'''
'''fibonacci series
'''
a = 0
b = 1
n = int(input())
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b
li = [0,1]
for i in range(2,n):
    li.append(li[i-2] + li[i-1])
print(li)

