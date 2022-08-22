
def user_details(username,year_of_birth, ):
    return 2022 - year_of_birth
username=input("what's your name?\n" ) 
year_of_birth=int(input("year of birth\n"))
print(username,"is born in the year",year_of_birth,"and your current age is",user_details(username, year_of_birth))

# name = input("enter a name:")
# year = int(input("enter a year:"))
# calc_age = 2022 - year
# print(f"my name is {name} and i am {calc_age} years old")
