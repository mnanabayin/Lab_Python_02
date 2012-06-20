#Encrypted Number

import math
tel_num = input('Enter your telephone ')
length = math.ceil(math.log(tel_num,10))
print 'length=',int(length)
length = int(length)
for i in range(length):
    rem = tel_num%10
    tel_num = tel_num/10
    print rem
    
    
