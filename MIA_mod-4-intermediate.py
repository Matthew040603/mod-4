#def shift_letter(letter, shift):
#parameters
#letter : str
#shift : int
#code is purposefully not optimized to practice and demonstrate the use of functions: while, if, elif, else
#code is also adjusted to fit both uppercase and lowercase letters
def shift_letter():
    letter = str(input("Enter a letter: "))
    shift = int(input("Number of times the letter will be shifted (if 1, A->B): "))
    while shift>=26:
        shift -=26
    if (65<=ord(letter)<=90):
        shifted_letter_ini = int(ord(letter)) + shift
        if shifted_letter_ini>90:
            shifted_letter_fin = ord("A") + (shifted_letter_ini - ord("Z") - 1)
        else:
            shifted_letter_fin = shifted_letter_ini
    elif (97<=ord(letter)<=122):
        shifted_letter_ini = int(ord(letter)) + shift
        if shifted_letter_ini>122:
            shifted_letter_fin = ord("a") + (shifted_letter_ini - ord("z") - 1)
        else:
            shifted_letter_fin = shifted_letter_ini
    else:
        print("The character \"" + letter + "\" remains unchanged because it is not a letter")
        return
    print("Original letter: " + letter + "\nShifted letter: " + chr(shifted_letter_fin))

#def caesar_cipher(text, shift):
#parameters
#text : str
#shift : int
#code is adjusted to fit both uppercase and lowercase letters
def caesar_cipher():
    text = str(input("Enter a line of text: "))
    shift = int(input("Enter a key (amount of times the letters will be shifted): "))
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result
    print("Original text: " + text + "\nEncrypted text: " + result)

#def shift_by_letter(letter, letter_shift):
#parameters
#letter : str
#letter_shift : str
#code is adjusted to fit both upptercase and lowercase letters
def shift_by_letter():
    letter = str(input("Enter a letter: "))
    letter_shift = str(input("Enter another letter, which will correspond to the amount of times the original letter will be shifted (e.g. A:0, B:1, C:2:,...): "))
    if letter_shift.isalpha():
        if letter_shift.isupper():
            shift = ord(letter_shift) - ord("A")
        else:
            shift = ord(letter_shift) - ord("a")
    else:
        return "Invalid character"
    if letter.isalpha():
        if letter.isupper():
            result = chr(((ord(letter) - ord("A") + shift) % 26) + ord("A"))
        else:
            result = chr(((ord(letter) - ord("a") + shift) % 26) + ord("a"))
    else:
        print("Original letter: " + letter + "\nResult: " + letter)
        return
    print("Original letter: " + letter + "\nResult: " + result)
    
#def vigenere_cipher(message, key):
#parameters
#message : str
#key : str
#code is for uppercase letters only
def vigenere_cipher():
    message = str(input("Enter a message: ").upper())
    key = str(input("Enter a key: ").upper())
    if not key.isalpha():
        return "Invalid. Please do NOT use any spaces or unique characters in your key"
    encrypted_message = ""
    message = message.replace(" ", "")
    #Split up the message to the length of the key
    split_message = [message[i:i + len(key)] for i in range (0, len(message), len(key))]
    #Translate each letter from each split using the key
    for each_split in split_message:
        i = 0
        for letter in each_split:
            if letter.isalpha():
                shifted_letter = ((((ord(letter) - ord("A")) + (ord(key[i]) - ord("A"))) % 26) + ord("A"))
                encrypted_message += chr(shifted_letter)
            else:
                encrypted_message += letter
            i += 1
    print("Original message: " + message + "\nEncrypted message: " + encrypted_message)
    