def solution(N):
    # Find number of divisors of N
    if N == 1:
        return 1

    divisors = 0
    i = 1
    while(i * i < N):
        if (N % i == 0):
            divisors += 2
        i += 1
    if (i * i == N):
        divisors += 1

    return divisors


if __name__ == '__main__':
    assert solution(24) == 8
    assert solution(2147483647) == 2
    assert solution(1) == 1
    assert solution(1000) == 16
    assert solution(1024) == 11
    assert solution(1125) == 12
    assert solution(125) == 4
    assert solution(48576) == 56
    assert solution(347) == 2
    assert solution(739) == 2
