def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


def solution(A, B):
    i = 0
    for a, b in zip(A, B):
        # Find GCD(a, b)
        gcd_val = gcd(a, b)  # gcd_val contains all common prime divisors

        while (a != 1):
            a_gcd = gcd(a, gcd_val)
            if a_gcd == 1:
                break
            a /= a_gcd

        if a != 1:
            continue

        while (b != 1):
            b_gcd = gcd(b, gcd_val)
            if b_gcd == 1:
                break
            b /= b_gcd

        if b == 1:
            i += 1

    return i


if __name__ == '__main__':
    assert solution([2, 1, 2], [1, 2, 2]) == 1
