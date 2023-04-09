class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key, n):
        i=0
        while i<n and Dict.a[i].key != search_key:
            i+=1
        if i==n: return -1
        else: return i
        
    def insert(self, v):
        Dict.a.append(node(v))


N = 1000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.search(s_key[i], N)
    if result == -1 or key[result] != s_key[i]:
        print('Error!')

