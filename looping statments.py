




# sum of given numbers
number=[1,3,5,7,9,10]
print(sum(number))

#another method
number=[1,2,3,4,5,6]
sum=0
for i in range (len(number)):
    sum=sum+number[i]
print(sum)

#sum of natural numbers:--
N=10
sum=(N*(N+1))/2
print(sum)
#another method:--
N=5
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)

#product of given numbers:--
n1=0
n2=0
for i in range(1,3):
    n1=sum+n1
    n2=sum*n2
print(n1)
print(n2)

#another method
n=3
p=1
for i in range(1,n+1):
    p=p*i
print(p)

# print solid right angled triangle
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print("\n")
# print solid square
for x in range(0,3):
    for y in range(0,4):
        print("*",end=" ")
    print()
print("\n")


# print solid rectangle
for p in range(0,2):
    for q in range(0,5):
        print("*",end=" ")
    print()
print(" ")

# Diagonal
for i in range(1,5):
    for j in range(1,5):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print(" ")

# mirror Diagonal
for i in range(1,5):
    for j in range(1,5):
        if(j-i>=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1,5):
    for j in range(1,5):
        if(i>=j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# diamond pattern
row=6
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

for i in range(row-1,0,-1):
    for j in range(1,row-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

#reversre diagonal
n=4
for i in range(1,5):
    for j in range(1,5):
        if(i+j==5):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()




























