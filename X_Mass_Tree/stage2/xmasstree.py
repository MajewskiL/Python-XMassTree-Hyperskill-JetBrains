def tree_2(high):
    for n in range(0, high):
        if n == 0:
            print(f"{(high - n - 1) * ' '}X")
            print(f"{(high - n - 1) * ' '}^")
        elif n == 1:
            print(f"{(high - n - 1) * ' '}/{(2 * (n - 1) + 1) * '*'}\\")
        else:
            print(f"{(high - n - 1) * ' '}/{(2 * (n - 1) + 1) * '*'}\\")
    print(f"{(high - 2) * ' '}| |")


tree_2(int(input()))
