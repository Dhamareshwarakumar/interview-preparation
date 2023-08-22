"""
Find Missing Number in an Array

Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
"""

import time
import random

# Time Complexity: O(n^2)
# Space Complexity: O(1)


def bruteforce(arr, n):
    """loop from 1 to n and check if the element is present in the array or not."""
    for i in range(1, n+1):
        flag = 0
        for j in range(0, n-1):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i


# Time Complexity: O(nlogn) + O(n) = O(nlogn)
# Space Complexity: O(1)
def better_sort(arr, n):
    """sort the array and check if the element is present or not."""
    arr.sort()
    for i in range(1, n+1):
        if arr[i-1] != i:
            return i


# Time Complexity: O(n) + O(n) = O(n)
# Space Complexity: O(n)
def better_hash(arr, n):
    """create a hash array of size n+1 and mark all the elements of the array as 1."""
    hashArr = [0] * (n+1)
    for i in range(0, n-1):
        hashArr[arr[i]] = 1
    for i in range(1, n+1):
        if hashArr[i] == 0:
            return i


# Time Complexity: O(n)
# Space Complexity: O(1)
def best_math(arr, n):
    """calculate the sum of first n natural numbers and subtract it from the sum of the array."""
    NSum = int(n*(n+1)/2)
    arrSum = 0
    for i in range(0, n-1):
        arrSum += arr[i]
    return NSum - arrSum


# Time Complexity: O(n)
# Space Complexity: O(1)
def best_xor(arr, n):
    """calculate the xor of first n natural numbers and xor it with the xor of the array."""
    arrXor = 0
    NXor = n
    for i in range(0, n-1):
        arrXor ^= arr[i]
        NXor ^= i+1
    return arrXor ^ NXor


if __name__ == '__main__':
    N = 1000000
    randInt = random.randint(1, N)
    startArr = [i for i in range(1, randInt)]
    endArr = [i for i in range(randInt+1, N+1)]
    arr = startArr + endArr

    start = time.time()
    op = best_xor(arr, N)
    end = time.time()
    if randInt == op:
        print("1 of 1 test case passed.")
    else:
        print("1 of 1 test case failed.")
        print("Expected: ", randInt)
        print("Got: ", op)
    print("Time Taken: ", end-start)
