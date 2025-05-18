"""Guess a number game"""
import numpy as np

number = np.random.randint(1,101)

# number of trails
count = 0

while True:
    count+=1
    predict_number = int(input("Guess a number from 1 to 100: "))
    
    if predict_number > number:
        print("The number should be less!")
        
    elif predict_number < number:
        print("The number should bigger!")
        
    else:
        print(f"You guessed correctly! The number is {number}, your trail is {count}")
        break