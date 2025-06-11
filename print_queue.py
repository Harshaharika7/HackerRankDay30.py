from itertools import product

def summingPieces(arr):
    n = len(arr)
    total = 0

    # Try all possible ways to cut the array into contiguous segments
    for mask in product([0, 1], repeat=n-1):  # 2^(n-1) cuts
        current_segment = []
        result = 0
        for i in range(n):
            current_segment.append(arr[i])
            if i == n-1 or mask[i] == 1:
                result += len(current_segment) * sum(current_segment)
                current_segment = []
        total += result

    return total


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(summingPieces(arr))
