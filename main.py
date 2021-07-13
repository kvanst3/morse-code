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
        result.extend([MORSE_CODE_DICT[char.upper()], ' '])
    return convert(result)


def decrypt(message):
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    result = []
    sentence = message.split('   ')
    for word in sentence:
        signals = word.strip().split(' ')
        for s in signals:
            val_idx = val_list.index(s)
            result.append(key_list[val_idx])
        result.append(' ')
    return convert(result)


game_on = True

while game_on:
    usr_choice = input('1. Encode\n2. Decode\n3. Exit\n\n')
    if int(usr_choice) == 1:
        message = input('Message to encode:\n')
        encrypted_message = encrypt(message)
        print(f'Result:\n{encrypted_message}')
    elif int(usr_choice) == 2:
        code = input('Message to decode:\n')
        decrypted_message = decrypt(code)
        print(f'Result:\n{decrypted_message}')
    else:
        game_on = False
