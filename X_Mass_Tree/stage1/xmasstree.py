def tree_1(high):
    for n in range(0, high):
        print(f"{(high - n - 1) * ' '}{(n * 2 + 1) * '*'}")


tree_1(int(input()))
