import random
import string

lengthOffPass = int(input("Enter password length: "))

char = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(lengthOffPass):
    password += random.choice(char)

print("Generated Password:", password)