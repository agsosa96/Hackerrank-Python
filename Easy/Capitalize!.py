# You are asked to ensure that the first and last names of people begin with a
# capital letter in their passports. For example, alison heck should be
# capitalised correctly as Alison Heck.

# alison heck --> Alison Heck

# Given a full name, your task is to capitalize the name appropriately.


def solve(s):
    
    ListFirstLetterCapitalized = [x.capitalize() for x in s.split(' ')]
    
    return ' '.join(ListFirstLetterCapitalized)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


