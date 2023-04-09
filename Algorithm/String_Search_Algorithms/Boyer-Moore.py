def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c)-64

def initSkip(p):
    M = len(p)
    for i in range(N):
        skip[i] = M
    for i in range(M):
        skip[index(p[i])] = M-i-1


def BM(p,t):
    M = len(p)
    N = len(t)
    initSkip(p)
    i, j = M-1, M-1
    while(j >= 0):
        while(t[i] != p[j]):
            s = skip[index(t[i])]
            if(M-j > s):
                i += M-j
            else:
                i +=s
            if i >= N:
                return N
            j = M-1
        i -= 1
        j -= 1
    return i+1


t = 'STRING STARTING CONSISTING'
p = 'STING'
M = len(p)
N = len(t)
skip=[-1]*N
print('Pattern location:',BM(p,t))
