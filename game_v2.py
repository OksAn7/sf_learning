"""Guess a number game - with a computer"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): Our guessed number. Defaults to 1.

    Returns:
        int: Trails number
    """
    # number of trails
    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1,500)
        if predict_number == number:
            break
    
    return count

def score_game(random_predict) -> int:
    """Average trail number for 1000 trails if to guess the number from 1 to 100

    Args:
        random_predict (_type_): Guess function

    Returns:
        int: Average trails number
    """
    count_ls = []
    np.random.seed(1) #fix seed for reproducibility
    random_array = np.random.randint(1, 101, size =(1000)) #creating a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in average for {score} trails")
    return score

if __name__ == '__main__':
    score_game(random_predict)