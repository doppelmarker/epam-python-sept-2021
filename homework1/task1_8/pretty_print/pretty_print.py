def print_multiplication_table(a, b, c, d):
    for row_idx, row_val in enumerate(range(a - 1, b + 1)):
        for col_idx, col_val in enumerate(range(c, d + 1)):
            if row_idx == col_idx == 0:
                print(f"{'':7}", end="")
            elif col_idx == 0:
                print(f"{range(a, b + 1)[row_idx - 1]:7}", end="")
            print(f"{row_val * col_val:7}", end="")
        print("\n")


print_multiplication_table(2, 4, 3, 7)
