import random

length_of_pass = int(input("How long do you want the password to be? "))
ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&’()*+,-./:;<=>?[|]{}^~@_"
password = ""


def password_generator(pass_length):
    global password
    for i in range(pass_length):
        random_num = random.randrange(0, len(ascii))
        random_character = ascii[random_num]
        password = password + random_character
    print(password)


password_generator(length_of_pass)
del password
