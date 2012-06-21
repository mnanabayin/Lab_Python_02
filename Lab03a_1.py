#1,2 Encrypted Number

import math
ans = 0
ans1 = 0
tel_num = input('Enter your telephone ')
length = math.ceil(math.log(tel_num,10))
bits = math.ceil(math.log(tel_num,10))-1
print 'length=',int(length)
length = int(length)
for i in range(length):
    rem = tel_num%10
    rem1 = tel_num%10
    tel_num = tel_num/10
    rem1 = (rem1 + 7)%10
    ans = ans + rem*(10**int(bits))
    ans1 = ans1 + rem1*(10**int(bits))
    bits-=1
print 'First Encryption =',ans,'Second Encryption =',ans1
    
    
