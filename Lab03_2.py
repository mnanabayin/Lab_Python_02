#Encrypted Number

import math
ans=0
tel_num = input('Enter your telephone ')
length = math.ceil(math.log(tel_num,10))
ct = int(math.ceil(math.log(tel_num,10)))-1
print 'length=',int(length)
length = int(length)
for i in range(length):
    rem = tel_num%10
    tel_num = tel_num/10
    ans = ans + rem * (10**ct)
    ct=ct-1
    
    
    print 
    
    
