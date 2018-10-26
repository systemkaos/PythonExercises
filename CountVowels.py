""" 
Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
Im sure there is a lot of checking you can do to determine if, in fact, Y is a vowel for the string. I wont do this.
"""

#Does a simple count and just outputs the total amount of vowels.
def count_vowels(inputstring):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        for letter in inputstring:
            if letter == vowel:
                count += 1
    return count

inputstring = 'colonization'
count_vowels(inputstring)

#Counts the vowels and total count in a dictionary.
def count_vowels_report(inputstring):
    vowels = {'totalcount': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for vowel in vowels:
        for letter in inputstring:
            if letter == vowel:
                vowels[letter] += 1
                vowels['totalcount'] += 1
    return vowels

count_vowels_report(inputstring)