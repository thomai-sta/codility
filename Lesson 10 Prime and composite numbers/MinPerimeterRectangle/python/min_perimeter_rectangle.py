import sys


def solution(N):
    # Find number of divisors of N
    min_perimeter = sys.maxint
    i = 1
    while(i * i <= N):
        if (N % i == 0):
            a = i
            b = N / i
            min_perimeter = min(min_perimeter, (a + b))
        i += 1

    return 2 * min_perimeter


if __name__ == '__main__':
    assert solution(30) == 22
    print(solution(1000000000))
