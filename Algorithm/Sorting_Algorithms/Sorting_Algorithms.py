import sys
sys.setrecursionlimit(10**9)

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("Sorted")
    else:
        print("Not sorted")
                

def checkReverseSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] < a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("Sorted")
    else:
        print("Not Sorted")


def selectionSort(a,n):
    for i in range(1,n):
        min=i
        for j in range(i,n+1):
            if a[min]>a[j]:
                min=j
            a[min],a[i]=a[i],a[min]

            

def bubbleSort(a, n):
    for i in range(n, 1,-1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

                

def insertionSort(a, n):
    for i in range(2,n+1):
        v=a[i]
        j=i-1
        while j>0 and a[j]>v :
            a[j+1]=a[j]
            j=j-1
        a[j]=v



def shellSort(a,n):
    h=1
    while h<n:
        h=3*h+1
    h=h//3
    while h>0:
        for i in range(h+1,n+1):
            v=a[i]
            j=i
            while j>h and a[j-h]>v:
                a[j]=a[j-h]
                j=j-h
            a[j]=v
        h=h//3



def quickSort(a,l,r):
    if r>l:
        i=partition(a,l,r)
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)

def partition(a,l,r):
    v=a[r]
    i=l
    j=r
    while True:
        while a[i]<v:
            i=i+1
        while a[j]>=v:
            j=j-1
        if i>=j:
            break
        a[i],a[j]=a[j],a[i]        
    a[i],a[r]=a[r],a[i]
    return i



def mergeSort(a, l, r):
    if(r >l):
        m=(r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

def merge(a,l,m,r):
    i,j,k=l,m+1,0
    b=[]
    for _ in range(l,r+1):
        b.append(None)

    while (i<m+1 and j<r+1):
        if(a[i]<a[j]):
            b[k]=a[i]
            i+=1
            k+=1
        else:
            b[k]=a[j]
            j+=1
            k+=1
    if(i>m):
        for p in range(j,r+1):
            b[k]=a[p]
            k+=1
    else:
        for p in range(i,m+1):
            b[k]=a[p]
            k+=1


    for p in range(l,r+1):
        a[p]=b[p-l]




def heapSort(a,n):
    for i in range(n//2,0,-1):
        heapify(a,i,n)
    for i in range(n-1,0,-1):
        a[1],a[i+1]=a[i+1],a[1]
        heapify(a,1,i)
        
def heapify(a, h, m):
    v=a[h]
    j=2*h
    while True:
        if j>m:
            break
        if j<m and a[j]<a[j+1]:
            j+=1
        if v>=a[j]:
            break
        else:
            a[j//2]=a[j]
        j=j*2
    a[j//2]=v




def cocktailShakerSort(a,n):
    d,i,k=True,1,n
    while(k>i):
        if (d==True):
            for p in range(i,k):
                if(a[p]>a[p+1]):
                   a[p],a[p+1]=a[p+1],a[p]
            k-=1
        else:
            for p in range(k,i,-1):
                if(a[p]<a[p-1]):
                   a[p],a[p-1]=a[p-1],a[p]
            i+=1
        d=not d


def exchangeSort(a,n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
                


def countingSort(a, n, m):
    b = [0]*(n+1)
    count=[0]*(m+1)
    for i in range(1,n+1):
        count[a[i]]=count[a[i]]+1
    for j in range(0,m):
        count[j+1]= count[j+1]+count[j]
    for i in range(n,0,-1):
        b[count[a[i]]]=a[i]
        count[a[i]]=count[a[i]]-1

    for i in range(1,n+1):
        a[i]=b[i]



def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('Queue is empty')
        return -1
    else:
        data = queue.pop(0)
        return data

import math
def digit(d, k):
    return int((d//math.pow(10,k-1))%10)

def radixSort(a, n, m, queue):
    for k in range(1, m+1):
        for i in range(1,n+1):
            kd=digit(a[i],k)
            enqueue(Q[kd],a[i])
        p=0
        for i in range(0,10):
            while Q[i]!=[]:
                p+=1
                a[p] = dequeue(Q[i])




def makeRun(a,n):
    i=1
    r=[]
    while i<=n:
        t=[]
        t.append(a[i])
        while i<n and a[i+1] >= a[i]:
            i+=1
            t.append(a[i])
        r.append(t)
        i+=1
    return r

def naturalMergeSort(r,m):
    k=1
    result=[]
    while k<m:
        array=[]
        a=len(r[k-1])
        b=len(r[k])
        i,j=0,0
        while i<a and j<b:
            if r[k-1][i]>r[k][j]:
               array.append(r[k][j])
               j+=1
            else:
                array.append(r[k-1][i])
                i+=1
        if i<a:
            for p in range(i,a):
                array.append(r[k-1][p])
        else:
            for p in range(j,b):
                array.append(r[k][p])
        result.append(array)
        k+=2
    k-=1
    
    if k<m:
        result.append(r[k])
    if len(result)!=1:
        result=naturalMergeSort(result,len(result))
    return result
