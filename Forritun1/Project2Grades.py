grade=1
eining=0
grade_sum=0
eining_sum=0
grade_eining=0
grade_eining_sum=0
highest_grade=-1

while True:
    grade = float(input(),)
    if grade < 0:
        break
    eining = int(input())
    if eining < 0:
        break
    if grade > highest_grade:
        highest_grade=grade
    grade_sum=grade_sum+grade
    eining_sum=eining_sum+eining
    grade_eining=grade * eining
    grade_eining_sum=grade_eining_sum+grade_eining
    
if eining_sum > 0:
    weighed_a_grades=grade_eining_sum / eining_sum
    rounded_weighed_a_grades= round(weighed_a_grades,2)
    print ("Weighted average grade:", rounded_weighed_a_grades)
if highest_grade >= 0:
    print("Highest grade: ", format(highest_grade, ".1f"))
