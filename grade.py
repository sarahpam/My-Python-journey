

def gpa_calculator():
    name = input("enter name:")
    score =int(input("enter score:"))
     
    if score <= 100 and score >= 70:
        print(f" {name} has a score of {score} and is graded A .")
    elif score <= 69 and score >= 60:
        print(f" {name} has a score of {score} and is graded B .")
    elif score <= 59 and score >= 50:
        print(f" {name} has a score of {score} and is graded C .")
    elif score <= 49 and score >= 40:
        print(f" {name} has a score of {score} and is graded D .")
    elif score <= 39  and score >= 0:
        print(f" {name} has a score of {score} and is graded F .")
    elif score <= 0:
        print(f"{name} has a score of {score} which is a negative and cannot be graded.")
    elif score >=101:
        print(f"{name} has a score of {score} which is too big and cannot be graded .")
    
  
gpa_calculator()