m = int(input())
n = int(input())
new2= 0
new3= 0 
for months in range (n):
    new = int(input())
    new2 = m - new
    new3 += new2
print (new3 + m)