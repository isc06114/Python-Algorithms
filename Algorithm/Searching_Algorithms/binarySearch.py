class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key, n):
        left, right=0,n-1
        while right >= left:
            mid=(left+right)//2
            if Dict.a[mid].key < search_key: left = mid+1
            elif Dict.a[mid].key > search_key: right = mid-1
            else: return mid
        return -1
            
    def insert(self, v):
        Dict.a.append(node(v))



N = 80000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(s_key)
d = Dict()
for i in range(N):
    d.insert(key[i])

for i in range(N):
    result = d.search(s_key[i], N)
    if result == -1 or key[result] != s_key[i]:
        print('Error!')
