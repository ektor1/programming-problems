# Find the letter that appears in both compartments in each rucksack
# Find its priority value and add it to a variable
import string
import numpy as np

my_file = open ("input3.txt", "r")

data = my_file.read()

items = data.split("\n")

alphabet = list(string.ascii_lowercase)
Alphabet = list(string.ascii_uppercase)

alphabet_arr = np.array(range(1,27)) # values for lowercase alphabet
Alphabet_arr = np.array(range(27,53)) # values for uppocase alphabet

# Assign values with appropriate alphabet
alph_values = dict(zip(alphabet, alphabet_arr))
Alph_values = dict(zip(Alphabet, Alphabet_arr))

def priorities(items):
    """split each string in half 
    select one split and check if the character is in the other split
    When character found - stop - link the letter to priority value and add to total"""
    total = 0
    
    for i in items:
        for j in i[:len(i)//2]:
            if j in i[len(i)//2:]:
                if j.islower():
                    total += alph_values[j]
                else:
                    total += Alph_values[j]
                break

    return total

print(priorities(items))
