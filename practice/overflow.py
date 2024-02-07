n = int(input())

matrix = []
for i in range(n):
    matrix += [list(map(int, (input().split())))]

dotty = [['.' for i in range(n)] for j in range(n)]


def print_dotty(dotty):
    print()
    if type(dotty[0][0]) == type(1):
        for i in range(n):
            for j in range(n):
                print(dotty[i][j], end=' ')
            print()
    else:
        for i in range(n):
            for j in range(n):
                print(dotty[i][j], end='')
            print()


# determine new centers
def det_new_centers(a1, a2, n):
    n1, n2, e1, e2, w1, w2, s1, s2 = -1, -1, -1, -1, -1, -1, -1, -1

    # North, South
    if a1 - 1 >= 0 and a1 + 1 < n:
        n1, n2 = a1 - 1, a2
        s1, s2 = a1 + 1, a2
    # East, West
    if a2 - 1 >= 0 and a2 + 1 < n:
        e1, e2 = a1, a2 + 1
        w1, w2 = a1, a2 - 1

    return n1, n2, e1, e2, w1, w2, s1, s2


def values_of_new_centers(n1, n2, e1, e2, w1, w2, s1, s2):
    if n1 == -1:
        N = "invalid"
    else:
        N = matrix[n1][n2]

    if e1 == -1:
        E = "invalid"
    else:
        E = matrix[e1][e2]

    if w1 == -1:
        W = "invalid"
    else:
        W = matrix[w1][w2]

    if s1 == -1:
        S = "invalid"
    else:
        S = matrix[s1][s2]

    return N, E, W, S


def check_if_at_edge(a1, a2, n):
    at_edge = True
    if a1 == 0 or a2 == 0 or a1 == n-1 or a2 == n-1:
        return at_edge
    return not(at_edge)


def pour_water_W(i, j, dotty):
    dotty[i][j] = 'W'


prev_nodes = []

solution = False


def overflow(a1, a2):
    global solution
    prev_nodes.append((a1, a2))

    # print(a1, a2, matrix[a1][a2])

    # water level
    water_level = matrix[a1][a2]

    # pour water in cell @ dotty[a1][a2]
    pour_water_W(a1, a2, dotty)

    if check_if_at_edge(a1, a2, n):
        print_dotty(dotty)
        solution = True
        return
    else:
        # determine north, east, west, south coordinates
        n1, n2, e1, e2, w1, w2, s1, s2 = det_new_centers(a1, a2, n)

        # determine north, east, west, south values
        N, E, W, S = values_of_new_centers(n1, n2, e1, e2, w1, w2, s1, s2)

        flow = False

        if water_level >= N:
            if (n1, n2) in prev_nodes:
                flow = False
            else:
                flow = True
                matrix[n1][n2] = water_level
                r = overflow(n1, n2)

        if water_level >= E:
            if (e1, e2) in prev_nodes:
                flow = False
            else:
                flow = True
                matrix[e1][e2] = water_level
                overflow(e1, e2)

        if water_level >= W:
            if (w1, w2) in prev_nodes:
                flow = False
            else:
                flow = True
                matrix[w1][w2] = water_level
                overflow(w1, w2)

        if water_level >= S:
            if (s1, s2) in prev_nodes:
                flow = False
            else:
                flow = True
                matrix[s1][s2] = water_level
                overflow(s1, s2)

        if solution == True:
            return
        if flow == False:
            water_level += 1
            matrix[a1][a2] += 1
            overflow(a1, a2)


# print_dotty(dotty)
init_center = n // 2
overflow(init_center, init_center)
print_dotty(dotty)
