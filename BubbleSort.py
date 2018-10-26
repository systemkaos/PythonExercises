""" 
Example of bubble sort

https://en.wikipedia.org/wiki/Bubble_sort
I had fun with this one, after reading the wiki page I got the logic down pretty well. I did have issues in the for statement, the range(n) or your list length -1 got me as I was getting index range problems 
"""
import random

#Creates a random list given a length paramater.
def generate_randomlist(len):
    listtosort = []
    i = 0
    while i <  len:
        listtosort.append(random.randrange(0, len))
        i = i + 1
    return listtosort

#The Sort algorithim 
def bubble_sort(list):
    n = len(list) - 1
    swapped = False
    while not swapped:
        swapped = True
        #Range that is modified is required because you get an index out of range problem otherwise
        for i in range(n):
            #Checks if left is greater than right, if so, swap.
            if list[i] > list[i + 1]:
                swapped = False
                j = list[i + 1]
                list[i + 1] = list[i]
                list[i] = j
    return list

x = generate_randomlist(4)
print(x)
y = bubble_sort(x)
print(y)