def count_pairs_naive(arr, L, R):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if L <= arr[i] + arr[j] <= R:
                count += 1
    return count

