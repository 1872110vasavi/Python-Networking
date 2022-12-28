#Sets
#unordered collection of items.every set element is unique and immutable
a=2
set={5,"Six",a,8,2}
print(type(set))
print(set)

#set conversion
set={1,2,2,3,4,5}
print(set)
print(list(set))

#string to set
set_a="apple"
print(list(set_a))
print(tuple(set_a))

#as items are not ordered
set_a=((1,2,1))
print(set_a)

#add items
set_a={1,3,6,2,9}
set_a.discard(2)
print(set_a)

a=55
a+=1
print(a)

#string to tuple
color="red"
tuple_a=[1,2,3]
print(tuple_a)

#in and notin
tuple=(1,2,3,4)
value=5 in tuple
print(value)

#problems
#write a common elements in lists
vasu1={4,5,6,7,3}
vasu2={5,1,9,3,0}
vasu3={5,3,4,0}
intersection=vasu1 & vasu2 & vasu3
print(intersection)














