class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node

    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    def check(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.right.key== search_key or x.left.key == search_key:
                return x.key
            else:  
                if x.key > search_key: x=x.left
                elif x.key < search_key: x=x.right
                else: return x.key
        return -1
    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key > search_key: x=x.left
            elif x.key < search_key: x=x.right
            else: return x.key
        return -1

    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

N = 4000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])


for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('Error!')

