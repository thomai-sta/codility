def solution(A):
    N = len(A)

    if (N == 1):
        return [0]

    # count elements' occurrences
    counters = [0] * (2 * N + 1)
    for a in A:
        counters[a] += 1

    non_divisors = [N] * (2 * N + 1)

    for a in range(1, 2 * N + 1):
        if (counters[a] != 0):
            multiple = a
            while(multiple <= 2 * N):
                non_divisors[multiple] -= counters[a]
                multiple += a

    result = []
    for a in A:
        result.append(non_divisors[a])

    return result


if __name__ == '__main__':
    assert solution([3, 1, 2, 3, 6]) == [2, 4, 3, 2, 0]
    print(solution([3, 4]))
