# for even in range(50,100,2):
#     print(even)
# kin = 50
# while kin <= 100:
#     print(kin)
#     kin += 2

# for odd in range(50,100,3):
#     print(odd)
# sin = 50
# while sin <= 100:
#     print(sin)
#     sin += 3

# for great in range(200,1000,50):
#     print(great)
# pin = 200
# while pin <= 1000:
#     print(pin)
#     pin += 50

def even_odd():
    ant =int(input("enter a number:"))
    
    if ant%2 == 0 and ant != 0:
        print(f"this number is even")
    elif ant%2 == 1 and ant != 0:
        print(f"this number is odd")
    else:
        print(f"invalid number to search")

    

# even_odd()

def square():
    num =int(input("enter a number:"))
    square = num**2

    print(f"the squared value is:{square}")   
    return square
square()