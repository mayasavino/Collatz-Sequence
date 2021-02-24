"""
Finds the longest collatz sequence under 1 million.


file: longest_collatz.py
author: Maya Savino
date: 17 February 2021
assignment: Lab 3

"""

from collatz import collatz_len

def main():
    """
    Finds the longest collatz sequence under 1 million using the equation
    collatz_len, defined in the collatz.py file."""   
    longest = 0
    n = 0
    l = 0
    for n in range (1, 1000000):
        count = collatz_len(n)
        if (longest < count):
            longest = count
            l = n
            
    print("Longest chain is produced by", l, "with a sequence of length", longest)


if __name__ == "__main__":
    main()