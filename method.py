# def my_method():
#     name = input("enter my name:")
#     length = len(name)
#     print(f"my name is {name} and my name has {length} letters")
#     return name
# my_method()







# def user_info():
#     username = input("enter name:")
#     email = input("enter email:")
#     password = input("enter password:")
#     length = len(password)
#     hide_password = "*" * length
    
#     print(f"my username is {username} , email address is {email} and my password is {hide_password}which has a length of {length} characters. ")
#     return username,email,password
# # user_info()

# # def game():
# #     num = 10
# #     yours = int(input("enter a number:"))

# #     if yours == num:
# #         print(f"you win")
# #     elif yours < num:
# #         print(f"the value {yours} is less than the secret number {num}")
# #     elif yours > num:
# #         print(f"the value {yours} is greater than the secret number {num}")
# #     else:
# #         print(f"the value inputted is not a number")

# # # game()

# secret_number = 10
# guess =int()
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_number and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = int(input("enter guess:"))
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print(f"Out of guesses, GAME OVER!")
# else:
    #print(f"YOU WIN! at {guess_count} attempt")
def cube(x):
    return x**3
    



