def longestSubarrayWithSumK(a: [int], k: int) -> int:
    maxLen = 0
    arrSum = 0
    j = 0
    for i in range(j, len(a)):
        arrSum += a[i]
        while (arrSum > k and j < i):
            arrSum -= a[j]
            j += 1
        if arrSum == k:
            subArrLen = i - j + 1
            if subArrLen > maxLen:
                maxLen = subArrLen
    return maxLen


if __name__ == "__main__":
    a = [1, 2, 3, 1, 1, 1, 1, 1]
    k = 3
    print(longestSubarrayWithSumK(a, k))
