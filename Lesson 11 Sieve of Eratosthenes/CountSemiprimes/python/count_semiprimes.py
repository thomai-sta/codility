import random
from math import sqrt


def solution(N, P, Q):

    # Find out all the primes with Sieve of Eratosthenes
    prime_table = [False] * 2 + [True] * (N - 1)
    prime = []
    prime_count = 0
    for element in range(2, int(sqrt(N)) + 1):
        if prime_table[element] is True:
            prime.append(element)
            prime_count += 1
            multiple = element * element
            while multiple <= N:
                prime_table[multiple] = False
                multiple += element

    for element in range(int(sqrt(N)) + 1, N + 1):
        if prime_table[element] is True:
            prime.append(element)
            prime_count += 1

    # Compute the semiprimes information
    semiprime = [0] * (N + 1)
    for index_former in range(prime_count - 1):
        for index_latter in range(index_former, prime_count):
            if prime[index_former] * prime[index_latter] > N:
                # So large that no need to record them
                break
            semiprime[prime[index_former] * prime[index_latter]] = 1
    # Compute the number of semiprimes until each position.
    # in the range (0,i] there are k semiprimes.
    for index in range(1, N + 1):
        semiprime[index] += semiprime[index - 1]

    # the number of semiprimes within the range [ P[K], Q[K] ]
    # should be semiprime[Q[K]] - semiprime[P[K]-1]
    question_len = len(P)
    result = [0] * question_len
    for index in range(question_len):
        result[index] = semiprime[Q[index]] - semiprime[P[index] - 1]

    return result


if (__name__ == '__main__'):
    assert solution(26, [1, 4, 16], [26, 10, 20]) == [10, 4, 0]
    N = 50000
    M = 100
    P = []
    Q = []
    for i in range(M):
        p = random.randint(1, N)
        q = random.randint(p, N)
        P += [p]
        Q += [q]
    print(solution(N, P, Q))

    N = 50000
    M = 30000
    P = []
    Q = []
    for i in range(M):
        p = random.randint(1, N)
        q = random.randint(p, N)
        P += [p]
        Q += [q]
    print(solution(N, P, Q))

    N = 5000
    M = 30000
    P = []
    Q = []
    for i in range(M):
        p = random.randint(1, N)
        q = random.randint(p, N)
        P += [p]
        Q += [q]
    print(solution(N, P, Q))
    N = 100
    M = 30000
    P = []
    Q = []
    for i in range(M):
        p = random.randint(1, N)
        q = random.randint(p, N)
        P += [p]
        Q += [q]
    print(solution(N, P, Q))
