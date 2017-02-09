from sys import argv, exit
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    '''rotate a string of text by rot spaces'''
    message = ''
    for char in text:
        rotate = rotate_character(char, rot)
        message = message + rotate

    return message

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False
    elif cl_args[1].isdigit():
        return True
    else:
        return False

def main():
    if user_input_is_valid(argv):
        user_input = input("Type a message:")
        print(encrypt(user_input, (int(argv))))
    else:
        print("usage: python3 caesar.py n")
        exit()

if __name__ == "__main__":
    main()     

