stop_range=int(input())
num_divisor=int(input())

for i in range(stop_range):
    stop_range2=i%10 
    stop_range3=(i-(i%10))/10
    stop_range4=(stop_range2+stop_range3)**2
    if stop_range4 == i:
        if i >= 10 and i < 100:
            print (i)

range_counter=0                   
for x in range(1,100):
    range_counter=0
    if x >= 0:
        if x <= stop_range:
            for y in range(1,x//2 + 1):
                if x % y == 0:
                    range_counter+=1
    if range_counter+1 == num_divisor:
        if x < stop_range:
            print (x)