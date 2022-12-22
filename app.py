import random
import string


def generate_password(length):
    chars = string.printable

    chars = chars.replace("'", '')
    chars = chars.replace('"', '')
    chars = chars.replace('\\', '')

    chars = list(chars)
    random.shuffle(chars)

    passoword = ''.join(random.sample(chars, length))
    return passoword

password = generate_password(10)
print(password)