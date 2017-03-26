def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


def solution(N, M):
    if (N == M):
        return 1

    # N chocolates with step M
    if (N % M == 0):
        return (N / M)

    GCD = gcd(N, M)
    LCM = M * N / GCD
    return LCM / M


if __name__ == '__main__':
    assert solution(10, 4) == 5
    assert solution(10, 3) == 10
    print(solution(1000000000, 1000000000))
    print(solution(1000000000, 1000))
