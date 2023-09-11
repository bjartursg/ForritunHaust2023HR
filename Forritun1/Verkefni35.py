number = int(input())
while number >=0:
    if number == 0:
        print ("The number does not contain 7.")
        break
    if number % 10 == 7:
        print("The number contains 7.")
        break
    number=number//10




