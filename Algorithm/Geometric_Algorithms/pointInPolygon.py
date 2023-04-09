import geo as g
import sys


def ccw(p0, p1, p2):
    dx1 = p1.x - p0.x
    dy1 = p1.y - p0.y
    dx2 = p2.x - p0.x
    dy2 = p2.y - p0.y
    if dx1 * dy2 > dx2 * dy1 : return 1
    if dx1 * dy2 < dx2 * dy1 : return -1
    if dx1 == 0 and dy1 == 0 : return 0
    if dx1 * dy2 < 0 or dx2 * dy1 < 0 : return -1
    if dx1^2 + dy1^2 < dx2^2 + dy2^2 : return 1
    return 0

def intersect(l1, l2):
    t1 = ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)
    t2 = ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)
    return t1 <= 0 and t2 <= 0

def theta(p1, p2):
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)
    if ax + ay == 0 : t = 0
    else: t = dx / (ax + ay)
    if dx < 0 : t = 2 - t
    elif dy < 0 : t = 4 + t
    return t * 90

def selectionSort(p, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1):
            if theta(p[1], p[j]) < theta(p[1], p[minIndex]):
                minIndex = j
        p[minIndex], p[i] = p[i], p[minIndex]

def inside(t, p, n):
    count, j = 0, 0
    lt, lp  = g.line(), g.line()
    p[0], p[n+1] = p[n], p[1]
    lt.p1 = t
    lt.p2.x = sys.maxsize
    lt.p2.y = t.y
    for i in range(1, n+1):
        lp.p1, lp.p2 = p[i], p[i]
        if intersect(lp, lt) == False:
            lp.p1 = p[i]
            lp.p2 = p[i]
            if intersect(lp, lt): count += 1
    if count % 2 == 1: return True
    else: return False

def printInside(t, res):
    print('Point (%s, %s) :'%(t.x, t.y), end=' ')
    if res:
        print('IN')
    else:
        print('OUT')

N = 16
p = []
p.append(g.point(None, None, None))
for i in range(N):
    p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))
p.append(g.point(None, None, None))
minIndex = 1
for i in range(2, N+1):
    if p[i].y < p[minIndex].y:
        minIndex = i
p[minIndex], p[1] = p[1], p[minIndex]
selectionSort(p, N)
tlist = []

#일련의 point 선
tlist.append(g.point(13,4,1))
tlist.append(g.point(7,9,2))
tlist.append(g.point(5,8,3))
tlist.append(g.point(8,13,4))

for i in tlist:
    printInside(i, inside(i, p, N))

