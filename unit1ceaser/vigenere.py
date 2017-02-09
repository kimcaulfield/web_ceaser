from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    '''rotate text by the numerical value of the letters in key'''
    message = ''
    textindex = 0
    keyindex = 0

    while textindex < len(text):
        numerical_key = alphabet_position(key[keyindex])
        rotate = rotate_character(text[textindex], numerical_key)
        message = message + rotate

        if text[textindex] == " ":
            keyindex = keyindex
        elif keyindex < len(key)-1:
            keyindex += 1
        else:
            keyindex = 0

        textindex += 1

    return message

def main():
    user_input = input("Type a message:")
    rotation = input("Encryption key:")
    print(encrypt(user_input, rotation))    
   
if __name__ == "__main__":
    main()     