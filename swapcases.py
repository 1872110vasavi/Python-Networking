#swapcase
v="pYtHoN"
print(v.swapcase())
swap="PrOgRaM"
print(swap.swapcase())
# covert dd-mm-yy format to dd/mm/yy
date="10-11-2022"
date_result=date.replace("-","/")
print(date_result)

#palindrome
palin1="MOM"
palin2="MOM"
palin3=palin2[::-1]
if (palin1==palin2):
    print("yes")
else:
    print("no")

palin_drome1="343"
palin_drome2="343"
palin_drome3=palin_drome2[::1]
if (palin_drome1==palin_drome2):
    print("yes")
else:
    print("no")

# valid password or not

import re
p="VaSu@123"
x=True
while x:
    if not re.search("[A-Z]",p):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[@]",p):
        break
    else:
        print("it is valid")
        x=False
        break
if x:
    print("it is not valid")




















