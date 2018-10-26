""" 
Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach 1 using the following process: 
"""

def collatz_conjecture(n):
    n = 500
    steps = 0
    while n > 1:
        if n % 2 == 0:
            #print("n before")
            #print(n)
            n = n / 2
            #print("n after")
            #print(n)
            steps = steps+1
        elif n % 2 != 0:
            #print("n before")
            #print(n)
            n = (n * 3) + 1
            #print("n after")
            #print(n)
            steps = steps+1
        steps
    return steps

collatz_conjecture(500)