nop=0
ask=0
everyone=0
while nop < 2:
    nop = int(input())
while ask < nop:
    ask=ask+1
    number=int(input())
    everyone=everyone + number

print (f"The sum of all contributions is {everyone}")
print (f"When {everyone} is divided by {nop}, the remainder is {everyone % nop}")
print (f"Player {everyone % nop} is the winner!")

