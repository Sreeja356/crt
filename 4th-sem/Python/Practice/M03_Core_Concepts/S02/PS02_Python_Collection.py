#2.creation of set:
a ={1,2,3,4,5,6}
print(a)
b=set([1,2,3,45,])
print(b)


#3.Adding element in set:
b =set([1,2,3,45,5])
b.remove(45)
print(b)

#4.Removing
b=set([1,2,3,45,5])
b.remove(45)
print(b)

#5.Set Operations
a={1,2,3,5,6}
b={10,2,3,5,60}
print(a.union(b))
print(a.intersection(b))
print(a.difference)

#6.Leetcode problems on sets(268,575)
#Tuples
t=(1,23,45,50)
print(t)
#Accessing of Tuples


#Concatenation:
t1={1,23,45,50}
t2={1,2,87,9,6}
print(t1+t2)

#Nesting of tuples
t1={1,23,45,50}
t2={1,2,87,9,6}
print(t1,t2)

#Repetation of tuples
t1=(1,23,45,50)
print(t1 *3)

#Slicing of tuples:
t1=(1,23,45,50)
print(t1[1:])
print(t1[0:3])
print(t1[:-1])

#Leetcode problems on Tuples(349,657)

#Dictionary
#Accessing dict items(key[],get()):
d ={'name':'sreeja','age':19}
d.key['name']
print(d)
d.get('name')
print(d)
#Adding & updating dict items
d ={'name':'sreeja','age':19}
del d['age']
d.pop('name')
print(d)
d.clear()
print(d)
#Leetcode problems on dict 1,
