import random
min=1
max=6
roll_again="yes"
while roll_again =="yes":
    print("rolling the dice")
    print("the values...")
    print(random.randint(min,max))
    roll_again = input ("roles the dice again")