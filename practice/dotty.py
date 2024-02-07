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
                print(dotty[i][j], end=' ')
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

    return {'n': N, 'e': E, 'w': W, 's': S}


def find_min_direction(dValues, fromDirn, water_level, nodes):
    v = [('n', dValues['n'], nodes[0]),
         ('e', dValues['e'], nodes[1]),
         ('w', dValues['w'], nodes[2]),
         ('s', dValues['s'], nodes[3])]

    v = [x for x in v if (x[0] != fromDirn and x[1] <=
                          water_level and x[2] not in prev_nodes)]

    vn = sorted(v, key=lambda x: x[1])

    if len(vn) > 0:
        return vn[-1][0]
    return None


def check_if_at_edge(a1, a2, n):
    at_edge = True
    if a1 == 0 or a2 == 0 or a1 == n-1 or a2 == n-1:
        return at_edge
    return not(at_edge)


def pour_water_W(i, j, dotty):
    dotty[i][j] = 'W'


prev_nodes = []

lobaldebug = []


def overflow(a1, a2, oDirn=None):
    while True:
        if len(lobaldebug) == 100:
            print(a1, a2, matrix[a1][a2])
            print_dotty(matrix)
            return True
        # print_dotty(matrix)
        if (a1, a2) not in prev_nodes:
            prev_nodes.append((a1, a2))

        # print(a1, a2, matrix[a1][a2])

        # water level
        water_level = matrix[a1][a2]

        # pour water in cell @ dotty[a1][a2]
        pour_water_W(a1, a2, dotty)

        if check_if_at_edge(a1, a2, n):
            print_dotty(dotty)
            # print_dotty(matrix)
            return True
        else:
            # determine north, east, west, south coordinates
            n1, n2, e1, e2, w1, w2, s1, s2 = det_new_centers(a1, a2, n)

            # determine north, east, west, south values
            vc = values_of_new_centers(n1, n2, e1, e2, w1, w2, s1, s2)

            # if N == "invalid" or S == "invalid" or W == "invalid" or E == "invalid":
            #     return

            dirn = find_min_direction(vc, oDirn, water_level, [
                                      (n1, n2), (e1, e2), (w1, w2), (s1, s2)])

            fromDirn = None

            x, y, v = 0, 0, None
            if dirn == 'n':
                x, y = n1, n2
                fromDirn = 's'
                v = vc[dirn]
            elif dirn == 'e':
                x, y = e1, e2
                fromDirn = 'w'
                v = vc[dirn]
            elif dirn == 'w':
                x, y = w1, w2
                fromDirn = 'e'
                v = vc[dirn]
            elif dirn == 's':
                x, y = s1, s2
                fromDirn = 'n'
                v = vc[dirn]

            flow = False
            if v != None and water_level >= v:
                if (x, y) in prev_nodes:
                    flow = False
                else:
                    flow = True
                    matrix[x][y] = water_level
                    r = overflow(x, y, oDirn=fromDirn)
                    if r:
                        return r

            if flow == False:
                print_dotty(dotty)
                exit()
                matrix[a1][a2] += 1
                lobaldebug.append(1)
                continue


# print_dotty(dotty)
init_center = n // 2
overflow(init_center, init_center)
print_dotty(dotty)
