
print("Hello World")

print("12*3")
print(12*5)

import math
print(math.pow(2,6))

number=4
print(bool(number))
val1 = 7
val2 = 3
print(val1 < val2)

val1 = 5
val2 = 7
print(val1 < val2)

# print addition of multiple numbers

sum=2+3+4+5
print(sum)

# print length of the string
s="vasavi"
print(len(s))

# print "python is amazing", use tab space and new line characters
print("python     is      amazing")
print("python\nis\namazing")

#read two strings in two different variables,concat them and print length of concated string
v1="vasavi"
v2="konka"
c=v1+v2
print(c)
print(len(c))

#print remainder,quotient of the division.print both integer and flot results
a=15
b=5
c=a//b
print(c)
c=a%b
print(c)
#Type of variables:--
"int"
var1=2
print(type(var1))

"float"
s=2.0
print(type(s))

alpha = 'vasavikonka'
print(list(alpha))
print(tuple(alpha))
print(set(alpha))

print(id("hello"))

# reffering the same object
list_a=[1,3,5,7]
list_b=list_a
print(id(list_a))
print(id(list_b))

list_b[2]=4
print(list_b)
print(list_a)

# compound assignment example
s1=[1,2,3]
s2=s1
s1=s1+[4,5]
print(str(s1))
print(str(s2))
s1=[1,2,3]
s2=[3,s1]
print(s2)
s2[1]=5
print(s2)

# splitting a string
numbers="1,2,3   4"
num_list=numbers.split(',')
print(num_list)

numbers="1   2 3 4"
num_list=numbers.split(" ")
print(num_list)

string_a="python is astonishing"
list_a=string_a.split('a')
print(list_a)

# negative indexing
# using negative index returns the nth term from the end of the list
# last item in the list can be accessed with index-1

l1=[1,2,3,4,5]
print(l1[3])
print(l1[-1])

# slicing

l1=[1,2,3,4,5]
l2=l1[-5:-1]
print(l2)
l2=l1[-4:-1]
print(l2)

# negative stepsize
l1=[1,2,3,4,5]
l2=l1[4:0:-2]
print(l2)
l2=l1[4:1:-1]
print(l2)
l2=l1[3:1:-1]
print(l2)
l2=l1[4:0:-2]
print(l2)
l2=l1[::-1]
print(l2)
l2=l1[4::-1]
print(l2)
# slicing and indexing  strings

l1="program"
l2=l1[5:0:-1]
print(l2)
# take two numbers M and n.write a program to create a list with element M repeated by N times
m=5
n="4"
print(m*n)

m=5
n="hi"
print(m*n)

#

a="APPLE"
b="ApPLICATION"
if a[0:3]==b[0:3]:
    print("yes")
else:
    print("no")
# write a program that reads two 3 digit numbers and check if the first digit of A is less than last digit of B
A=input()
B=input()
if A[2:3] == B[0:1]:
    print("yes")
else:
    print("no")























