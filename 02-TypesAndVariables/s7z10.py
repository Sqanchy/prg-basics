import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("podaj liczbe 1-6: "))
win = you==computer
print(computer)
print(f'You won: {win}')