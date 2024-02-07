n = int(input())

matrix = []
for i in range(n):
    matrix += [(input().split())]

dotty = [['.' for i in range(n)] for j in range(n)]

print()
count = 0
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

center = n // 2
for i in range(n):
    for j in range(n):
        if ((i == center) and (j == center)):
            dotty[i][j] = 'W'

        print(dotty[i][j], end='')
    print()


# print_dotty(matrix)
# determine north, east, west, south coordinates
# n1, n2, e1, e2, w1, w2, s1, s2 = det_new_centers(a1, a2, n)
# # print(n1, n2, e1, e2, w1, w2, s1, s2)
# print(N, E, W, S)

# print('..................W................\n...............W.WWW...............\n..............WWWWWWW..............\n..............WWWWWW...............\n.............WWW..WWWW.............\n...........W.WWWWWWW.WWW...........\n..........WWWWW.WWWWWWWWW..........\n.........WWWWW.WWWWWWWWW.W.........\n.........WWWWW.WWWWWWWW.WWW........\n.......W..WWWWWWWWWWWWWWWWWW.......\n......WWW.WWWWWWW.WWW..WWWWWW......\n.....WWWW...WWWWWWW.WWW.WW.WWW.....\n........WWWWW.W.WWWWWWWW.WWWWWW....\n...W.WWWWWWWWWWWW.WWWWWWWWW.WW.....\n..WWWWWWWWW.WWW.WWWWW.WWWW.WWWW....\n.WWWWWWWWW.WW.WWWWWWWWW.WWWWW......\n...WWW..WWWWWW..WWWWW..W.W..WWW....\n..WWWWWWWWWWWWWWWWWWWW.WW..WWWWW...\n..WWW.WWWWW.WWW.WWWWWW.WWWWW.WW....\n.WWWW..WWWWWWWWWWWWWWWWWW.WWWWWW...\n..WWWW.WWWW.WWW.WWWWWW..W.W.WWW....\n...WWWWWWWWWWWWWWWWW.WWWWWWWWW.....\n....WWWW..WWWWW.W.WWW.WWWWWW.WW....\n.....WWWWWWWWWWW.WWWWWWWW.WWWW.....\n......WWWWWWWWWWWWWWWWWWWWWWW......\n.......WWWW.WW.WWW.WW..WWWWW.......\n........WWWWWW.WW...WWWW.WW........\n.........WW.WWWWWW.WW.WWW..........\n..........W..WWWWWWWWWWWW..........\n.............WWW.WWWWWWW...........\n............WW.WWWWWWWW............\n.............W.W.W.WWW.............\n....................W..............\n...................................\n...................................')

# print('.......\n.......\n.......\n...W...\n..WW...\n.WW....\n.W.....')
