"""
Finds the length of a collatz sequence 
that starts from a number the user inputs.

file: collatz.py
author: Maya Savino
date: 16 February 2021
assignment: Lab 3

"""

def collatz_len(n):
    """
    Finds the length of the collatz sequence of
    a given number."""
    count = 1

    while (n > 1):
        while (n % 2 != 0):
            n = int((3 * n) + 1)
            count += 1

        while (n % 2 == 0):
            n = int(n / 2)
            count += 1
        
    return count
    

if __name__ == "__main__":
    n = int(input("Enter a starting number: "))
    print("Length of Collatz sequence:", collatz_len(n))
