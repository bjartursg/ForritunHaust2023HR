k = int(input())
n = int(input())
summa=0

for number in range(n):
    x=int(input())
    newk=k**x
    summa+=newk
print (summa)
