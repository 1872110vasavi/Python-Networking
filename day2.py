M=int(input())
P=input()
C=input()
if M>=60 and P>=70 or C>=50:
    print("yes")
else:
    print("no")
if M+P+C>=180:
    print("Greater")
else:
    print("not greater")



