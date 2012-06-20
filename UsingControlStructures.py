#PART II
#5
theInput = raw_input("Enter an integer: ")
#Your code here
if int(theInput)%2 == 0:
    print 'even'
else:
    print 'odd'

print '---------'


#6
primarySchoolAge = 5
legalVotingAge = 18
presidentAge = 30
retireAge = 60
personAge = input("Enter an age: ")
print '---------'

if personAge < primarySchoolAge:
    print 'Too young.'
    print '---------'

if personAge >= legalVotingAge:
    print 'Remeber to vote'
    print '---------'

if personAge >= presidentAge:
    print 'Vote for me'
    print '---------'
elif personAge < presidentAge:
    print "You can't be president"
    print '---------'

if personAge > retireAge:
    print "Too old"

    print '---------'
    print '---------'




#7
print '\nMultiples of 3 from 40 to 0'
i=40
while i > 0:
    if i%3==0:
        print i
    i-=1


#8
print '\nNumbers between 6 and 30 that are not divisble by 2,3,5'
for j in range(7,30):
    if j%2==0:
        continue
    if j%3==0:
        continue
    if j%5==0:
        continue
    print j

#9
print '\nSmallest positive integer n such that 79*n has a remainder of 1 when divided by 97'
k=1
while k>0:
    if (79*k)%97==1:
        print '---------'
        print 'n =',k
        break
    k+=1


