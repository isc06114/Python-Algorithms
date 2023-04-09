def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32: a = 64
        t = a + k
        if t > 90: t -= 27
        if t == 64: t = 32
        cipher += chr(t)
    return cipher
    
def decipher(cipherText, k):
    n = len(cipherText)
    plain = ''
    for i in range(n):
        a = ord(cipherText[i])
        if a == 32: a = 64
        t = a - k
        if t < 64: t += 27
        if t == 64: t = 32
        plain += chr(t)
    return plain

plainText = 'SAVE PRIVATE RYAN'
K = 1
print('plain text : ', plainText)
cipherText = encipher(plainText, K)
print('encryption : ', cipherText)
decodeText=decipher(cipherText,K)
print('decryption : ', decodeText)
