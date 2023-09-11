size = int(input())
print ("* "*(size-1) + "*")
for number in range(size-2):
    print ("* "+("  "*(size-2))+"*")
if size > 1:
    print ("* "*(size-1) + "*")

