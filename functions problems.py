#divisible by 3 and divisible by 5
def div(num):
    if num%3==0 and num%5!=0 and num!=0:
        return "marco"
    elif num%5==0 and num%3!=0 and num!=0:
        return "polo"
    elif num%3==0 and num%5==0 and num!=0:
        return "marcopolo"
    else:
        return "no"
nu=int(input())
res=div(nu)
print(res)

#



