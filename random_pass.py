import random

lengthOfPassword = input("How long do you want the password to be? ")
ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?[|]{}^~@_"
password = ""


def passwordGenerator(passLength):
    global password
    for i in range(passLength):
        randomNumber = random.randrange(0, len(ascii))
        randomCharacter = ascii[randomNumber]
        password = password + randomCharacter
    print(password)
passwordGenerator(lengthOfPassword)
del password
