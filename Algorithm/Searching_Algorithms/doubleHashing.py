class Dict:
    def __init__(self):
        Dict.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while( Dict.a[x] != -1):
            x = x+u
            if x>=M:
                x=x%M
        Dict.a[x] = v

    def search(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while Dict.a[x] != -1:
            if(Dict.a[x] == v):
                return Dict.a[x]
            else:
                x+=u
                if x>=M:
                    x=x%M

    def hash(self, v):
        return v % M

    def hash2(self, v):
        return 64 - (v % 64)



N = 10000
M = 10391
key = []
s_key = []
for i in range(N):
    r = random.randint(1, 3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])

for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('Error!')

