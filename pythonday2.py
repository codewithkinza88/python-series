# ==========================================
# File: day2_basics.py
# Author: Kinza Kareem
# Date: June 25, 2026
# Description: Introduction to Variables, Inputs, and Math
# Concepts: Variables, input() function, string concatenation, and math operators.
# ==========================================

# ------------------------------------------
# 1. WHAT IS A VARIABLE?
# ------------------------------------------
# Think of a variable as a labeled storage box. 
# We put data inside the box, and we can access or change it using its label.

character_name = "Alex"  # Storing text (a string)
character_age = 21       # Storing a whole number (an integer)

print("--- 1. Variable Demonstration ---")
print("Once upon a time, there was a developer named " + character_name + ".")
print("They were " + str(character_age) + " years old.")
print("They loved the name " + character_name + ", but didn't like being " + str(character_age) + ".\n")


# ------------------------------------------
# 2. TAKING USER INPUT
# ------------------------------------------
# The input() function pauses the program and waits for the user to type something.
# Whatever the user types is always saved as a string (text).

print("--- 2. Interactive Input ---")
user_name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")

# We can combine (concatenate) strings using the '+' symbol
print("\nNice to meet you, " + user_name + "!")
print("Your favorite color, " + favorite_color + ", is an excellent choice!\n")


# ------------------------------------------
# 3. BASIC MATH IN PYTHON
# ------------------------------------------
# Python can perform calculations easily:
# Addition (+), Subtraction (-), Multiplication (*), Division (/)

print("--- 3. Let's Do Some Math ---")
birth_year_str = input("What year were you born? ")

# CRITICAL CONCEPT: Because input() always returns text,
# we must convert (cast) it to an integer using int() to do math!
birth_year = int(birth_year_str)
current_year = 2026

age = current_year - birth_year

print("Since the current year is " + str(current_year) + ":")
print("\tYou are (or will turn) " + str(age) + " years old this year!\n")

# Extra Math Tricks:
print("Double your age is:\t" + str(age * 2))
print("Your age in 5 years:\t" + str(age + 5))
print("==========================================")