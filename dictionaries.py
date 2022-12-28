#dictionaries

dict_a={
    'name':'vasavi',
    'age':20

}
print(dict_a)
dict_a['age']=21
print(dict_a)

#remove key and value
del dict_a['age']
print(dict_a)

del dict_a['name']
print(dict_a)

#member check
dict_a={
    'name':'vasavi',
    'age':20
}
result='name'in dict_a
print(result)

#reffering same dictinary object

dict_a={
    'name':'vasu',
    'age':21
}
dict_b=dict_a
dict_b['age']=20
print(dict_a)
print(id(dict_a))
print(id(dict_b))

#problems
#update value of particular key
dict_a={
    'age':20
}
dict_a['age']=21
print(dict_a)

#remove a key__del
dict_a={
    'name':'vasavi',
    'age':21
}
dict_a.pop('name')
print(dict_a)

# Matrices
M=int(input)
N=int(input)
mat=[]
for i in range