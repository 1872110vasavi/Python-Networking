# write a program to remove duplicate numbers
set_a = set([1,2,2,3,4,4,5])
print(set(set_a))

#to remove list of numbers if present in the set
set_a=[1,2,3,4,"@","$","#"]
set_b=set_a.copy()
for i in range(len(set_a)):
    if not str(set_a[i]).isdigit():
        print(list[i],end="")
    else:
        set_b.remove(set_a[i])
print(set_b)

#given two lines of comma-seperated integers.
vas_a={1,2,3,4,5}
vas_b={4,1,2,3,8}
vas_c= vas_a & vas_b
print(vas_c)

#
vasu1={4,5,6,7,3}
vasu2={5,1,9,3,0}
vasu3={5,6,4,0}
intersection=vasu1 & vasu2 & vasu3
print(intersection)

#to check superset,subset,disjoint set
set_a={1,2,3,4,5,6,7}
set_b={1,2,3,4}
set_c={8,9,10}
superset=set_a.issuperset(set_b)
print(superset)
superset=set_a.issuperset(set_c)
print(superset)
subset=set_b.issubset(set_a)
print(subset)
disjoint=set_c.isdisjoint(set_a)
print(disjoint)

#7
k=[7,]
num_a=[1,2,3,4,5]
num_b=[1,2,3,4,5,6]
num_c=num_b.__add__(k)
print(num_c)

#write a program to rotates list D times to left
list_b=["python"]
list_a=list[list_b]
print(list_a)
for i in range(5):
    t=list_a[0]
    list_a.remove(t)
    list_a.append(t)
    print(list_a)

#max and min value
tuple1={1,2,3,4,5,6}
print(max(tuple1))
print(min(tuple1))

# 
















