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
    tree.append(f"{(high - 2) * ' '}I I")
    return tree


h, i = list(map(int, input().split(" ")))
print(*tree3(h, i), sep="\n")

