# Functions
# Block of code

def greetings():
    print("hello")

def my_function():
    print("Hello")

#1
def my_fun():
    print("hello python")
my_fun()

#2
def conc(m1):
    print(m1+"HCL")
conc("WELCOME")

#area and perimeter of square
def peri(area,perim):
    print(area)
    print(perim)
l=3
b=4
area=l*b
perim=4*area
peri(area,perim)

#square of each number
def square(a):
    print(a*a)
square(1)
square(2)
square(3)
square(4)

#Divisible by 7
def divisible(a):
    print(a)
number=35
if number%7==0:
    print("true")
else:
    print("false")

#return second character
def second_character(msg):
    a1=msg
    res=list(a1)
    return(res[1])
word="vasu"
res=second_character(word)
print(res)




































