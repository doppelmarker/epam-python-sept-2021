def print_multiplication_table(a, b, c, d):
    print(f"{'':7}", end="")
    for i in range(c, d + 1):
        print(f"{i:7}", end="")
    print("\n")

    for row_idx, row_val in enumerate(range(a, b + 1)):
        for col_idx, col_val in enumerate(range(c, d + 1)):
            if col_idx == 0:
                print(f"{range(a, b + 1)[row_idx]:7}", end="")
            print(f"{row_val * col_val:7}", end="")
        print("\n")


print_multiplication_table(2, 4, 5, 7)
