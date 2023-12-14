# What is the problem?
# The problem provides a calibration document where each line contains a sequence of characters
# I have to combine the first digit and last digit of each line to form a two digit number.
# Then I have to add up all these values (2 digits) and get the total sum to find the solution to this prblem.

# advent of code examples:
# 1abc2: first digit = 1, last digit = 2 -> number of two digits = 12
# pqr3stu8vwx: first digit = 3, last digit = 8 -> number of two digits = 38
# a1b2c3d4e5f: first digit = 1, last digit = 5 -> number of two digits = 15
# treb7uchet: first digit = 7, last digit = 7 -> number of two digits = 77 

# What to do?
# solve the problem with the example of advent of code, to see if the final result is 142, it's a way to understand if I'm doing the right steps;
# read the calibration document line by line. -> search how to read a text file in python;
# for each line, extract the first and last digit;
# combine the two digits to form a two-digit number;
# add up all these two-digit values;
# see total sum.

file = open("input.txt", "r")
content = file.read()
print(content)
file.close()



