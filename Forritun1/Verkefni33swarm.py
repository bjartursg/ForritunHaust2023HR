# Here's something to get you going
# (you might need to add indentation or move it around):
answer="Y"
number=float(0)
while answer == "Y" or answer == "y":
    answer = input("You need something doubled? (Y)es? ")
    while answer == "Y" or answer == "y":
        print ("")
        number = float(input("All right, then. Give me a number, and I'll double it for ya:"))
        print ("")
        print (float(number*2))
        answer = input("You need something else doubled? (Y)es? ")