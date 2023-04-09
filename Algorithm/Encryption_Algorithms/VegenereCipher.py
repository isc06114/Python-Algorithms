def encipher(plain, k):
    n = len(k)
    cipher = ''
    for i in range(len(plain)):
        a = ord(plain[i])
        if a == 32: a = 64
        b = ord(k[i % n]) - 64
        t = a + b
        if t > 90: t -= 27
        if t == 64: t = 32
        cipher += chr(t)
    return cipher

def decipher(cipherText, k):
    n = len(k)
    plain = ''
    for i in range(len(cipherText)):
        a = ord(cipherText[i])
        if a == 32: a = 64
        b = ord(k[i%n]) -64
        t = a-b
        if t < 64: t += 27
        if t == 64: t = 32
        plain += chr(t)
    return plain

plainText = 'SAVE PRIVATE RYAN'
K = 'ABC'
print('plain text : ', plainText)
cipherText = encipher(plainText, K)
print('encryption : ', cipherText)
decodeText=decipher(cipherText,K)
print('decryption : ', decodeText)

