# import random library
import random 
import sys

# Variables
result = sys.argv[1]
number = int(result)

# read in the words file
with open('Code/words.txt') as file:
    data = file.readlines()
    random_words = random.sample(data, len(data))
    for i in range(0, number):
            print(random_words[i].strip(), end = " ")
