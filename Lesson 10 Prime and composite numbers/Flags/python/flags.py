import random
import math


def solution(A):
    # Find peaks' positions
    peaks = []
    i = 1
    while(i < len(A) - 1):
        if (A[i] > A[i - 1] and A[i] > A[i + 1]):
            peaks.append(i)
            i += 2
        else:
            i += 1

    if (len(peaks) < 2):
        return sum(peaks)

    max_distance = peaks[-1] - peaks[0]
    max_K = int(math.sqrt(max_distance + 1))

    for K in range(max_K, 1, -1):
        curr_peak = peaks[0]
        num_peaks = 1
        for p in range(1, len(peaks)):
            if (peaks[p] - curr_peak >= K):
                num_peaks += 1
                curr_peak = peaks[p]
            if (num_peaks == K):
                return K


if __name__ == '__main__':
    assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    A = [random.randint(0, 1000000000) for i in range(100000)]
    print(solution(A))
