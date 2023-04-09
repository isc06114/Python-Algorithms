class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self, key):
        self.key = key
        self.b = None
        self.left = None
        self.right = None

class Dict():
    itemMin = bitskey(0)
    head = node(itemMin)
    head.b = 5
    head.left = head.right = head

    def search(self, v):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1):
                x = x.right
            else:
                x = x.left
        if v.get() != x.key.get(): return self.itemMin
        return x.key

    def insert(self, v):
        v = bitskey(v)
        i = maxb
        p = self.head
        t = self.head.left
        while p.b > t.b:
            p = t
            if self.bits(v, t.b, 1):
                t = t.right
            else:
                t = t.left
        if v.get() == t.key.get(): return
        while self.bits(t.key, i, 1) == self.bits(v, i, 1):
            i -= 1  
        p = self.head
        x = self.head.left
        while p.b > x.b and x.b > i:
            p = x
            if self.bits(v, x.b, 1):
                x = x.right
            else:
                x = x.left
        t = node(self.itemMin)
        t.key = v
        t.b = i
        if self.bits(v, t.b, 1):
            t.left = x
            t.right = t
        else:
            t.left = t
            t.right = x

        if self.bits(v, p.b, 1):
            p.right = t
        else:
            p.left = t

    def bits(self, item, bit, cmp):
        if item.bits(bit, 1) == cmp:
            return 1
        else:
            return 0

    def check(self, v):
        v = bitskey(v)
        p = self.head
        x = g = self.head.left
        if x.key.get()==v.get():
            print('key : ',x.key.get(),', parents: ',g.key.get())
        else:
            while p.b > x.b:
                g = p
                p = x
                if self.bits(v, x.b, 1):
                    x = x.right
                else:
                    x = x.left
            if v.get() != x.key.get(): return self.itemMin
            print('key : ',x.key.get(),', parents: ',g.key.get())



N = 7
maxb = 5
key = [1, 19, 5, 18, 3, 26, 9]
s_key = [1, 19, 5, 18, 3, 26, 9]
s_key.sort()

d = Dict()
for i in range(N):
    d.insert(key[i])
print(key)
for i in range(N):
    d.check(s_key[i])
