# HIT 137 Assignment 2 Q1
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037

RAW_FILE_PATH = "raw_text.txt"
ENCRYPTED_FILE_PATH = "encrypted_text.txt"

# Takes a single char and two integer values and outputs the encrypted char
def encrypt_char(char, n, m):
    ord_value = ord(char)
    # lowercase between 'a' to 'm' - forward by n * m
    if ord_value >= ord('a') and ord_value <= ord('m'):
        return chr(ord_value + (n * m))
    
    # lowercase between 'n' to 'z' - backward by n + m
    if ord_value >= ord('n') and ord_value <= ord('z'):
        return chr(ord_value - (n + m))
    
    # uppercase between 'A' to 'M' - backward by n
    if ord_value >= ord('A') and ord_value <= ord('M'):
        return chr(ord_value - n)

    # uppercase between 'N' to 'Z' - forward by m^2
    if ord_value >= ord('N') and ord_value <= ord('Z'):
        return chr(ord_value + (m ** 2))

    return char

# Takes a single char and two integer values and outputs the decrypted char
def decrypt_char(char, n, m):
    ord_value = ord(char)

    # lowercase between 'a' to 'm' - backward by n * m
    if ord_value - (n * m) >= ord('a') and ord_value - (n * m) <= ord('m'):
        return chr(ord_value - (n * m))
    
    # lowercase between 'n' to 'z' - forward by n + m
    if (ord_value + n + m) >= ord('n') and (ord_value + n + m) <= ord('z'):
        return chr(ord_value + (n + m))

    # uppercase between 'A' to 'M' - forward by n
    if ord_value + n >= ord('A') and ord_value + n <= ord('M'):
        return chr(ord_value + n)

    # uppercase between 'N' to 'Z' - backward by m^2
    if ord_value - (m ** 2) >= ord('N') and ord_value - (m ** 2) <= ord('Z'):
        return chr(ord_value - (m ** 2))
    
    return char

# takes n and m values as integers and encrypts the raw
# data from file. Saves encrypted text to file
def encrypt(n, m):
    encrypted_text = ''
    with open(RAW_FILE_PATH, 'r') as input_file:
        input_text = input_file.read()
        for char in input_text:
            encrypted_text += encrypt_char(char, n, m)
    
    with open(ENCRYPTED_FILE_PATH, 'w') as output_file:
        output_file.write(encrypted_text)

# takes n and m values as integers and decrypts the already
# encrypted text from file. Returns decrypted text as string
def decrypt(n, m):
    with open(ENCRYPTED_FILE_PATH, 'r') as file:
        encrypted_text = file.read()
        decrypted_text = ''
        for char in encrypted_text:
            decrypted_text += decrypt_char(char, n, m)

        return decrypted_text

# takes input of a decrypted text string and compares
# it to raw input string, returns True if the strings
# are an exact match, else returns False
def decrypted_text_valid(decrypted_text):
    raw_text = ''
    with open(RAW_FILE_PATH, 'r') as file:
        raw_text = file.read()

    # print(raw_text)
    # print()
    # print(decrypted_text)

    return raw_text == decrypted_text

# main entry point
n = int(input("Enter n value: "))
m = int(input("Enter m value: "))

encrypt(n, m)
decrypted_text = decrypt(n, m)
print('The decrypted text is the same as the original.' if decrypted_text_valid(decrypted_text) else 'The decrypted text is NOT the same as the original')