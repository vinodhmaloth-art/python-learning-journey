# Day 6 - Strings
# Ask the user for their name, then print a greeting with the name in
# UPPERCASE, print how many letters the name has, and print the
# first and last letters of the name.

name = input("Enter your name: ")

print("Hello,", name.upper())
print("Your name has", len(name), "letters")
print("First letter:", name[0])
print("Last letter:", name[-1])
