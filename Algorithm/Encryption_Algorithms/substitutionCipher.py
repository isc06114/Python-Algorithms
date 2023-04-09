def encipher(plain, k):
    n = len(plain)
    cipher = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32:
            a = 0
        else:
            a -= 64
        cipher += k[a]
    return cipher

def decipher(cipherText, k):
    n = len(cipherText)
    plain = ''
    for i in range(n):
        j=0
        while(cipherText[i] != k[j]):
            j+=1
        if j == 0:
            j=32
        else:
            j+=64
        plain += chr(j)
    return plain

plainText = 'SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('plain text : ', plainText)
cipherText = encipher(plainText, K)
print('encryption : ', cipherText)
decodeText=decipher(cipherText,K)
print('decryption : ', decodeText)

