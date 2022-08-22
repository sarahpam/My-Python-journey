a=int(input("enter a number"))
b=int(input("eneter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))

def all_same(a,b,c,d):
    if a ==b and a == c and a == d and b ==a and b == c and b == d and c == a and c == b and c == d and d == a and d == b and d == c:
        print(f"{a},{b},{c},{d} are same")
    else:
        print(f"{a},{b},{c},{d} are not same")

def maximum_num (a,b,c,d):
    if a > b and a > c and a > d:
        print(f"{a} greater than {b},{c},{d}")
    elif b > a and b > c and b > d:
        print(f"{b} greater than {a},{c},{d}")
    elif c > a and c > b and c > d:
        print(f"{c} greater than {a},{b},{d}")
    elif d > a and d > b and d > c:
        print(f"{d} greater than {a},{b},{c}")

def minimun_num (a,b,c,d):
    if a < b and a < c and a < d:
        print(f"{a} less than {b},{c},{d}")
    elif b < a and b < c and b < d:
        print(f"{b} less than {a},{c},{d}")
    elif c < a and c < b and c < d:
        print(f"{c} less than {a},{b},{d}")
    elif d < a and d < b and d < c:
        print(f"{d} less than {a},{b},{c}")

grp1=(a + b)
grp2= (c + d) 

def great(a,b,c,d):
    if grp1 > grp2:
        print(f"grp operation {grp1} greater than {grp2}")
    elif grp2 > grp1:
        print(f"grp operation {grp2} greater than {grp1}")

def small(a,b,c,d):
    if grp1 < grp2:
        print(f"grp operation {grp1} less than {grp2}")
    elif grp2 < grp1:
        print(f"grp operation {grp2} less than {grp1}")

def equal(a,b,c,d):
    if grp1 == grp2:
        print(f"grp operation {grp1} equals {grp2}")
    else:
        print(f"not equal")





# def example(n):
#     return n
# name = input("write a name:")
# print(f"name function {example(name)}")


print(f"same values funtion call:{all_same(a,b,c,d)}")   
print(f"max function: {maximum_num(a,b,c,d)}")
print(f"min function call : {minimun_num(a,b,c,d)}")
print(f"great funtion call:{great(a,b,c,d)}")
print(f"small function call:{small(a,b,c,d)}")
print(f"equal function:{equal(a,b,c,d)}")


 


# if a < b and a < c and a < d:
#      print(f"{a} less than {b},{c},{d}")
# elif b < a and b < c and b < d:
#      print(f"{b} less than {a},{c},{d}")
# elif c < a and c < b and c < d:
#      print(f"{c} less than {a},{b},{d}")
# elif d < a and d < b and d < c:
#      print(f"{d} less than {a},{b},{c}")  

# grp1=(a + b)
# grp2= (c + d) 

# if grp1 > grp2:
#     print(f"grp operation {grp1} greater than {grp2}")
# elif grp2 > grp1:
#     print(f"grp operation {grp2} greater than {grp1}")

# if grp1 < grp2:
#     print(f"grp operation {grp1} less than {grp2}")
# elif grp2 < grp1:
#     print(f"grp operation {grp2} less than {grp1}")

# if grp1 == grp2:
#     print(f"grp operation {grp1} equals {grp2}")

# val = 6+ 7
# an = 4+5


# def add(a,b):
#     return a+b 

# print(add(1,7))