def alphabet_position(letter):
    '''return numerical value of letter'''
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    position = lowercase_alphabet.find(letter)
    if position < 0:
        position = uppercase_alphabet.find(letter)

    return position


def rotate_character(char, rot):
    '''rotate char by rot spaces'''
    import string
    def is_punct_char(char):
        '''check if char is punctuation'''
        if char in string.punctuation:
            return char
    original_position = alphabet_position(char)
    punctuation = is_punct_char(char)
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    encrypted = ''
    rotated_index = original_position + rot
    for character in char:
        if character == punctuation:
            return punctuation
        elif character == ' ':
            encrypted = encrypted + ' '
        elif character.islower():
#            rotated_index = original_position + rot
            if rotated_index < 26:
                encrypted = encrypted + lowercase_alphabet[rotated_index]
            else:
                encrypted = encrypted + lowercase_alphabet[rotated_index % 26]
#                if rotated_index == 0:
        else: 
            if rotated_index < 26:
                encrypted = encrypted + uppercase_alphabet[rotated_index]
            else:   
                encrypted = encrypted + uppercase_alphabet[rotated_index % 26]    

    return encrypted