x = int(input()) # Do not change this line
if x==1:
    print ("1")
print (x)
while x != 1:
    if x % 2 == 0:
        x=x/2
    else:
        x=x*3 + 1
    print (int(x))