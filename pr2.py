for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            if j == 4:
                print(i + 2, end="")
            else:
                print(i + 1, end="")
        else:
            if j == 0:
                print(i + 2, end="")
            else:
                print(i + 1, end="")
    print()
