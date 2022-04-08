import math
from art import logo

# Simple function
# def greet():
#     print("Hey")
#     print("Whats")
#     print("Up?")
#
# greet()

# Function that allows for input

# def greet_wth_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_wth_name(input("What is your name? "))
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with("Michal", "Lodz")

# Exercise 8.1 - Paint Area Calculator
#
# def paint_area_calc (height, width, coverage):
#     cans = math.ceil(height*width/coverage)
#     print(f"You need to buy {cans} cans of paint")
#
# height = int(input("Whats your wall height? "))
# width = int(input("Whats your wall width? "))
# coverage = 5
#
# paint_area_calc(height, width, coverage)

# Exercise 8.2 - Prime number checker

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime
#         print(f"{number} is not prime number")
#     else:
#         print(f"{number} is prime number")
#
#
# n = int(input("Check this number: "))
# prime_checker(n)

# Final project of a day - Caesar Cypher
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

# def encrypt (text, shift):
#     text_encrypted = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         text_encrypted += new_letter
#     print(f"The encoded text is {text_encrypted}")
#
#
# def decrypt(text, shift):
#     text_encrypted = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         text_encrypted += new_letter
#     print(f"The decoded text is {text_encrypted}")
#
#
# if direction == "e":
#     encrypt(text, shift)
# elif direction == "d":
#     decrypt(text, shift)
# else:
#     print("Choose right action!")

def ceasar(text, shift, direction):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "e":
            new_position = position + shift
            new_letter = alphabet[new_position]
            new_text += new_letter
        elif direction == "d":
            new_position = position - shift
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            print("Choose right action!")
    print(f"New text is: {new_text}")


ceasar(text, shift, direction)

