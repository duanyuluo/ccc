DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, 1)]

def ccc2023j5():
    

    W = input()
    R = int(input())
    C = int(input())

    row = []

    for p in range(R):
        row.append(input().split(" "))

    DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, 1)]

    print(search(W, row, C, R))


def outrange(w, h, x, y):
    if (x < 0 or x > h - 1 or y < 0 or y > w - 1):
        return True
    return False


def search(word, grid, gridW, gridH):
    solcount = 0
    for y in range(0, gridW):
        for x in range(0, gridH):
            if (grid[x][y] == word[0]):
                i = 1
                for vx, vy in DIR:
                    # print(outrange(gridW, gridH, x + vx, y + vy))
                    if (outrange(gridW, gridH, x + vx, y + vy)):
                        continue
                    if (i > word.__len__() - 1):
                        continue
                    if (grid[x + vx][y + vy] == word[i]):
                        csrx = x + vx
                        csry = y + vy
                        while (word[i] == grid[csrx][csry]):
                            i += 1
                            csrx += vx
                            csry += vy
                            if (i > word.__len__() - 1):
                                solcount += 1
                                break
                            if (outrange(gridW, gridH, csrx, csry)):
                                break
    return solcount
 

#     y
# x > # # # # #
    

if (__name__ == "__main__"):
    ccc2023j5()