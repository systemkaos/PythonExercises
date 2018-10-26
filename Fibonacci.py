""" 
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
https://en.wikipedia.org/wiki/Fibonacci_number 
"""

def Fibonacci_Sequence():
    
    x = 1
    y = x + x
    calc = []

    calc.append(x)
    calc.append(x)

    def run_seq(n):
        result = 0
        while n > 0:
            result = calc[0] + calc[1]
            calc.pop(1)
            calc.append(result)
            return result
            n - 1

    return run_seq(50)
