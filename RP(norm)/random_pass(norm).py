import random

# makes sure user input is valid and that any ValueErrors are circumvented
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

ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&’()*+,-./:;<=>?[|]{}^~@_"
password = ""

def password_generator(pass_length):
    password = ''.join(random.choice(ascii) for i in range(pass_length))
    print("\nPassword: \n" + password)

password_generator(length_of_pass)
del password

