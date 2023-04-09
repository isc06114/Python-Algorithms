def initNext(p):
    i, j = 0,-1
    while(i < M):
        if (p[i] == p[j]):
            Next[i] = Next[j]
        else:
            Next[i]=j
        while(p[i] != p[j] and j>-1):
            j=Next[j]
        i+=1
        j+=1

def KMP(p,t,c):
    initNext(p);
    i, j, = c, 0
    while(i<N and j< M):
        while(t[i] != p[j] and j>-1):
            j=Next[j]
        i+=1
        j+=1
    if(j==M):
        return i-M
    else:
        return i
            


t='ababacabcbababcacacaababca'
p='ababca'
M=len(p)
N=len(t)
Next=[]
c=0
for i in range(M):
    Next.append(-1)

while(c<26):
    c=KMP(p,t,c)
    print('Pattern location:',c,'\n')
    c+=1




