import random
lower_bound = int(input("Insert lower bound: "))
higher_bound = int(input("Insert higher bound: "))

try:
    print(random.randint(lower_bound, higher_bound))
except ValueError:
    print("Invalid input, try again!")
