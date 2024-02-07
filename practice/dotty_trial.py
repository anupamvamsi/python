import queue


class Node:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

    def __lt__(self, other_node):
        return self.v < other_node.v


n = int(input())

matrix = [[0] * n for x in range(n)]
dotty = [[Node(i, j, '.') for j in range(n)] for i in range(n)]

for i in range(n):
    l = input().split()

    for j in range(n):
        matrix[i][j] = Node(i, j, int(l[j]))


def print_matrix(m):
    if type(m[0][0].v) == type(1):
        for i in range(n):
            print()
            for j in range(n):
                print(m[i][j].v, end=' ')
    else:
        for i in range(n):
            print()
            for j in range(n):
                print(m[i][j].v, end='')
    print()


def determine_new_centers(curr_center):
    N, E, W, S = None, None, None, None

    if curr_center.x - 1 >= 0 and curr_center.x + 1 < n:
        N = matrix[curr_center.x - 1][curr_center.y]
        S = matrix[curr_center.x + 1][curr_center.y]
    if curr_center.y - 1 >= 0 and curr_center.y + 1 < n:
        E = matrix[curr_center.x][curr_center.y + 1]
        W = matrix[curr_center.x][curr_center.y - 1]

    return [N, E, W, S]


def check_if_at_edge(curr_center):
    at_edge = True
    if curr_center.x == 0 or curr_center.y == 0 or curr_center.x == n-1 or curr_center.y == n-1:
        return at_edge

    return not(at_edge)


def pour_water_W(curr_center):
    dotty[curr_center.x][curr_center.y].v = 'W'


def overflow(curr_center):
    to_revisit = queue.Queue()
    to_revisit_if_stuck = queue.PriorityQueue()

    pour_water_W(curr_center)
    to_revisit.put(curr_center)

    while not to_revisit.empty() or not to_revisit_if_stuck.empty():
        to_revisit_node = None

        if not to_revisit.empty():
            to_revisit_node = to_revisit.get()
        elif not to_revisit_if_stuck.empty():
            to_revisit_node = to_revisit_if_stuck.get()
        else:
            return

        if check_if_at_edge(to_revisit_node):
            return

        for adjacent_node in determine_new_centers(to_revisit_node):
            if dotty[adjacent_node.x][adjacent_node.y].v == 'W':
                continue

            if to_revisit_node.v >= adjacent_node.v:
                adjacent_node.v = to_revisit_node.v
                pour_water_W(adjacent_node)

                if check_if_at_edge(adjacent_node):
                    return

                to_revisit.put(adjacent_node)

            else:
                to_revisit_if_stuck.put(adjacent_node)


init_center = n // 2
# determine_new_centers(matrix[init_center][init_center])

# pour_water_W(dotty[init_center][init_center])
overflow(matrix[init_center][init_center])
print_matrix(dotty)
