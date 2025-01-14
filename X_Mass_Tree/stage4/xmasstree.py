def tree3(high, interval):
    bomb = 0
    tree = list()
    for n in range(0, high):
        if n == 0:
            tree.append(f"{(high - n - 1) * ' '}X")
            tree.append(f"{(high - n - 1) * ' '}^")
        elif n == 1:
            tree.append(f"{(high - n - 1) * ' '}/{(2 * (n - 1) + 1) * '*'}\\")
        else:
            to_print = str()
            for i in range(0, 2 * (n - 1) + 1):
                if i % 2 == 0:
                    to_print += "*"
                else:
                    if bomb % interval != 0:
                        to_print += "*"
                    else:
                        to_print += "O"
                    bomb += 1
            tree.append(f"{(high - n - 1) * ' '}/{to_print}\\")
    tree.append(f"{(high - 2) * ' '}| |")
    return tree


def tree4(top_list):
    square_x = 30
    square_y = 50
    area_t = list()
    for _ in range(square_x):
        area_t_line = list()
        for _ in range(square_y):
            area_t_line.append(" ")
        area_t.append(area_t_line)
    for i in range(square_y):
        area_t[0][i] = "-"
        area_t[square_x - 1][i] = "-"

    for i in range(1, square_x - 1):
        area_t[i][0] = "|" #  str(i % 10)
        area_t[i][square_y - 1] = "|" #  str(i % 10)
    for top in top_list:
        tree = tree3(top[0], top[1])
        x = top[2]
        for line in tree:
            y = top[3] - int(((len(tree[-2]) - 1) / 2))
            for i in range(len(line)):
                if line[i] != " ":
                    area_t[x][y + i] = line[i]
            x += 1
    text = " " * int(((square_y - 1 - 11) / 2))
    text += "Merry Xmas"
    for t in range(len(text)):
        area_t[square_x - 3][t + 1] = text[t]

    area_t = ["".join(line) for line in area_t]
    print(*area_t, sep="\n")


trees = list(map(int, input().split(" ")))

if len(trees) == 2:
    print(*tree3(trees[0], trees[1]), sep="\n")
else:

    data = [trees[x: x + 4] for x in range(0, len(trees), 4)]
    tree4(data)
