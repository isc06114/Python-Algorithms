def bruteForce(p,t,c):
    i, j = c, 0
    while(i < N-M and j < M):
        if t[i+j] != p[j]:
            i+=1;
            j=0;
        else:
            j+=1

        
    if (j == M):
        return i
    else:
        return -1
    



t='ababacabcbababcacacbcaababca\0'
p='ababca'
c=0
M=len(p)
N=len(t)
while(True):
    c=bruteForce(p,t,c)
    if(c==-1):
        print('end')
        break
    print('Pattern location:',c)
    c+=1
    


