def encipher(plain, n, p):
    cipher = ''
    i = 0
    while i < len(plain):
        m = ''
        for j in range(4):
            m += plain[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(p):
            b = t % n
            t = a * b
        if b < 10:
            cipher += '000' + str(b)
        elif b < 100:
            cipher += '00' + str(b)
        elif b < 1000:
            cipher += '0' + str(b)
        else:
            cipher += str(b)
    return cipher
def encode(plain):
    n = len(plain)
    m = ''
    for i in range(n):
        a = ord(plain[i])
        if a == 32: a = 64
        a -= 64
        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else:
            m += str(a)
    return m

def decipher(cipherText, n, s):
    plain = ''
    i = 0
    while i < len(cipherText):
        m = ''
        for j in range(4):
            m += cipherText[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(s):
            b = t % n
            t = a * b
        if b < 10:
            plain += '000' + str(b)
        elif b < 100:
            plain += '00' + str(b)
        elif b < 1000:
            plain += '0' + str(b)
        else:
            plain += str(b)
    return plain

def decode(decipherMessage):
    n = len(decipherMessage)
    m = ''
    plain = ''
    for i in range(n):
        a = ord(decipherMessage[i])
        m += chr(a)
    i = 0
    while i < len(m):
        dec = ''
        for j in range(2):
            dec += m[i+j]
        i += 2
        a = int(dec)
        a += 64
        if a == 64 : a = 32
        plain += chr(a)
    return plain
            

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97
P = 37
print('Plain text : ', plainText)
plainMessage = encode(plainText)
print('Encoding : ', plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print('encryption : ', cipherMessage)
decipherMessage = decipher(cipherMessage, N, S)
print('Encoding : ', decipherMessage)
plain = decode(decipherMessage)
print('decryption : ', plain)
