import re
import random
import string

# makes sure that user input is valid and that any ValueErrors are circumvented
while True:
    try:
        length_of_pass = int(input("How long do you want the password to be? "))
    except ValueError:
        print("**Please make sure you only use numbers.**\n")
        continue

    if length_of_pass < 0:
        print("**You've used an invalid number. Please use a number that is not negative.**\n")
    else:
        break

# the four variables below are the components/characters to make up ascii _____
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = "0123456789"
special = "!#$%&’()*+,-./:;<=>?[|]{}^~@_"
emoji = "😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍😘😗😙"
# variable that any of the chosen components (variables) above will be added to
ascii_text = ""

# will determine which components/character groups of ascii will be in the password
def components():
    def lower_def():
        global ascii_text
        lower_answer = input("\nLower case letters? ").upper()
        if lower_answer == "YES" or lower_answer == "Y":
            ascii_text += lowercase
        elif lower_answer == "NO" or lower_answer == "N":
            None
        else: # if yes or no is not given, re-ask the question
            lower_def()
    lower_def()

    def upper_def():
        global ascii_text
        upper_answer = input("\nUpper case letters? ").upper()
        if upper_answer == "YES" or upper_answer == "Y":
            ascii_text += uppercase
        elif upper_answer == "NO" or upper_answer == "N":
            None
        else:
            upper_def()
    upper_def()
    
    def special_def():
        global ascii_text
        special_answer = input("\nSpecial characters? ").upper()    
        if special_answer == "YES" or special_answer == "Y":
            ascii_text += special
        elif special_answer == "NO" or special_answer == "N":
            None
        else:
            special_def()
    special_def()
    
    def number_def():
        global ascii_text
        numbers_answer = input("\nNumbers? ").upper()
        if numbers_answer == "YES" or numbers_answer == "Y":
            ascii_text += numbers
        elif numbers_answer == "NO" or numbers_answer == "N":
            None
        else:
            number_def()
    number_def()
    
    def emoji_def():
        global ascii_text
        emoji_answer = input("\nEmojis? ").upper()
        if emoji_answer == "YES" or emoji_answer == "Y":
            ascii_text += emoji
        elif emoji_answer == "NO" or emoji_answer == "N":
            None
        else:
            emoji_def()
    emoji_def()

components()

def password_generator(pass_length):
    password = ''.join(random.choice(ascii_text) for i in range(pass_length))
    # make something to make sure characters wanted are in password
    #for i in true:
        #if i p
    print("\nPassword: \n" + password)
    del password
    diff_pass = input("\nNew password?\n").upper()
    if diff_pass == "YES" or diff_pass == "Y":
        print("\n")
        password_generator(length_of_pass)

password_generator(length_of_pass)

