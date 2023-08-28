import math
a_str = input() # Do not change this line.
b_str = input() # Do not change this line.
c_str = input() # Do not change this line.
a_int=int(a_str)
b_int=int(b_str)
c_int=int(c_str)
s_int=(a_int+b_int+c_int)/2
area= math.sqrt(s_int*(s_int-a_int)*(s_int-b_int)*(s_int-c_int))
print(area) # Change this line at your own peril.
