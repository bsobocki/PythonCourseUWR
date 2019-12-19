print(bin(7^80))

def encrypt(word, key):
    result = ''
    for letter in word:
        result += chr(ord(letter)^key)
    return result

def decrypt(encrypted, key):
    result = ''
    for letter in encrypted:
        result += chr(ord(letter)^key)
    return result

enc = encrypt('Python',7)
print(enc)
print(decrypt(enc, 7))