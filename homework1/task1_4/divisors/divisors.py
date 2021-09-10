def find_all_divisors(n):
    return {num for num in range(n // 2, 0, -1) if n % num == 0} | {n}
