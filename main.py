import os
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}


def convert(s):
    new_str = ""
    new_str = new_str.join(s)
    return new_str


def encrypt(message):
    result = []
    for char in message:
        try:
            result.extend([MORSE_CODE_DICT[char.upper()], ' '])
        except KeyError:
            os.system('clear')
            print('Invalid Key. Please refer to the Morse Guide for accepted characters. Thank you.')
            game_on()
    return convert(result)


def decrypt(message):
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    result = []
    sentence = message.split('   ')
    for word in sentence:
        signals = word.strip().split(' ')
        for s in signals:
            try:
                val_idx = val_list.index(s)
                result.append(key_list[val_idx])
            except ValueError:
                os.system('clear')
                print('Invalid Key. Please refer to the Morse Guide for accepted characters. Thank you.')
                game_on()
        result.append(' ')
    return convert(result)


def game_on():
    usr_choice = input('1. Encode\n2. Decode\n3. Exit\n\n')
    os.system('clear')
    if int(usr_choice) == 1:
        message = input('Message to encode:\n')
        os.system('clear')
        encrypted_message = encrypt(message)
        print(f'Result:\n{encrypted_message}\n\n')
        game_on()
    elif int(usr_choice) == 2:
        code = input('Message to decode:\n')
        os.system('clear')
        decrypted_message = decrypt(code)
        print(f'Result:\n{decrypted_message}\n\n')
        game_on()
    else:
        print("--. --- --- -..   -... -.-- . ")


game_on()
