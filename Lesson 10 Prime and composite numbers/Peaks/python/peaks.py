import math
import random


def solution(A):
    N = len(A)
    peaks = [0] * N
    i = 1
    while(i < len(A) - 1):
        if (A[i] > A[i - 1] and A[i] > A[i + 1]):
            peaks[i] = 1
            i += 2
        else:
            i += 1

    # start from min divisor, we check the symmetric
    i = 1
    while (i <= int(math.sqrt(N))):
        if (N % i == 0):
            # Check if the i blocks contain at least one peak
            block_len = i
            block_num = N / i
            start = 0
            end = block_len - 1
            curr_blocks = 0
            for b in range(block_num):
                if (sum(peaks[start:end + 1]) != 0):
                    curr_blocks += 1
                start += block_len
                end += block_len
            if (curr_blocks == block_num):
                return block_num
        i += 1

    # start from max divisor
    i = int(math.sqrt(N))
    while (i > 0):
        if (N % i == 0):
            # Check if the i blocks contain at least one peak
            block_len = N / i
            block_num = i
            start = 0
            end = block_len - 1
            curr_blocks = 0
            for b in range(block_num):
                if (sum(peaks[start:end + 1]) != 0):
                    curr_blocks += 1
                start += block_len
                end += block_len
            if (curr_blocks == block_num):
                return block_num
        i -= 1

    return i


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    A = [random.randint(0, 1000000000) for i in range(100000)]
    print(solution(A))
