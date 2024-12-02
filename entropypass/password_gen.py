import math
import random

LEET_SUBSTITUTIONS = {
    'a': ['@', '4'],
    'b': ['8', '13', '|3'],
    'c': ['<', '(', '{', '['],
    'd': ['|)', '[)', '])'],
    'e': ['3', '€'],
    'f': ['|='],
    'g': ['9', '&'],
    'h': ['|-|', '#'],
    'i': ['1', '!', '|'],
    'j': ['_|', '</'],
    'k': ['|<', '|{'],
    'l': ['|', '7', '1'],
    'm': ['(V)', '/\\ /\\', '|V|', '^^'],
    'n': ['/\\/', '||', '^/'],
    'o': ['0', '()'],
    'p': ['|D', '|o', '|>'],
    'q': ['0_', '9', '(,)'],
    'r': ['|2', '12', '|?'],
    's': ['$', '5', '§'],
    't': ['7', '+', '-|-'],
    'u': ['|_|', 'µ', '()_'],
    'v': ['/', '||'],
    'w': ['//', '^/', '(n)', 'X/', 'V V'],
    'x': ['><', '%'],
    'y': ['`/', '¥', '|/'],
    'z': ['2', '7_']
}

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special_chars = """~!@#$%^&*()`_-+={}[]|\:;"'<>,.?/"""
random_set = letters + numbers + special_chars

def return_entropy(char):
    return len(char) * math.log2(len(set(char)))

def random_index(n):
    return random.sample([i for i in range(n)], n//2)

#Function for strong entropy
def return_strong_password(linuxword_ele: str, entropy: int) -> str:
    linuxword=[i for i in linuxword_ele]

    indexes = random_index(len(linuxword))

    for i in indexes:
        if linuxword[i].lower() in LEET_SUBSTITUTIONS:
            linuxword[i]=random.choice(LEET_SUBSTITUTIONS[linuxword[i].lower()])

    desired_password="".join(linuxword)
    while int(return_entropy(desired_password)) <= entropy:
        random_char = random.choice(random_set)
        desired_password += random_char

    print(f"Original Linuxword: {linuxword_ele} | Password: {desired_password} | Entropy: {return_entropy(desired_password)}")   
     
    return desired_password

def process_file(input_path: str, output_path: str, entropy: int):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            password = line.strip()
            new_password = return_strong_password(password, entropy)
            outfile.write(new_password + '\n')


