import queue


class Node(object):
    def __init__(self, x, y, v=None):
        self.x = x
        self.y = y
        self.v = v

    def __lt__(self, other):
        return self.v < other.v


n = int(input())

matrix = [[0] * n for x in range(n)]

for i in range(n):
    l = input().split()
    for j in range(n):
        matrix[i][j] = Node(i, j, int(l[j]))

dotty = [[Node(i, j, '.') for i in range(n)] for j in range(n)]


def print_dotty(d):
    print()
    if type(d[0][0].v) == type(1):  # print <int> matrix
        for i in range(n):
            for j in range(n):
                print(d[i][j].v, end=' ')
            print()
    else:
        for i in range(n):          # print <other types> matrix
            for j in range(n):
                print(d[i][j].v, end='')
            print()


# determine new centers
def det_new_centers(c):
    N, E, W, S = None, None, None, None
    # North, South
    if c.x - 1 >= 0 and c.x + 1 < n:
        N = matrix[c.x-1][c.y]
        S = matrix[c.x+1][c.y]
    # East, West
    if c.y - 1 >= 0 and c.y + 1 < n:
        E = matrix[c.x][c.y+1]
        W = matrix[c.x][c.y-1]

    return [N, E, W, S]


def check_if_at_edge(c):
    at_edge = True
    if c.x == 0 or c.y == 0 or c.x == n-1 or c.y == n-1:
        return at_edge
    return not(at_edge)


def pour_water_W(c, dotty):
    dotty[c.x][c.y].v = 'W'


def overflow(c):
    q = queue.Queue()
    badq = queue.PriorityQueue()

    pour_water_W(c, dotty)

    q.put(c)

    while not q.empty() or not badq.empty():
        qn = None

        if not q.empty():
            qn = q.get()
        elif not badq.empty():
            qn = badq.get()
        else:
            return

        if check_if_at_edge(qn):
            return

        for adjn in det_new_centers(qn):
            if dotty[adjn.x][adjn.y].v == 'W':
                continue

            if qn.v >= adjn.v:
                adjn.v = qn.v
                pour_water_W(adjn, dotty)
                # extra two lines
                if check_if_at_edge(adjn):
                    return
                q.put(adjn)
            else:
                badq.put(adjn)


# print_dotty(dotty)
init_center = n // 2
# print_dotty(matrix)
overflow(matrix[init_center][init_center])

print_dotty(dotty)
