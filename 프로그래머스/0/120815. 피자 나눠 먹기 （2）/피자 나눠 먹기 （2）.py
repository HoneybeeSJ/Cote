def solution(n):
    a, b = 6, n
    while b:
        a, b = b, a % b
    lcm = 6 * n // a
    return lcm // 6