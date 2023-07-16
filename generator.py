import random
import os


def random_():
    list_of_alpha = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"

    star_length = 1 # integer for "for loop" , Feel free to modify it
    end_length = 5  # integer for "for loop" , Feel free to modify it

    for _ in range(star_length, end_length):
        with open('password.txt', 'a') as f:
            f.writelines(random.choice(list_of_alpha))
        with open('password.txt','r') as file:
            p = file.read()
    sym = "#@$&"
    
    p = p.join(sym)

    return p
    
    
    

if __name__ == "__main__":
    print("Welcome to Password generaotr!".upper())
    
    print(f"\nHere is your generated password: {random_()}")
    os.remove("password.txt") 

    input("press Enter key to quite. ")

    
    

