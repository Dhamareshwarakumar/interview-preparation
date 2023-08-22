def singleNumber(arr):
    result = 0
    for i in range(len(arr)):
        result ^= arr[i]
    return result


if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]

    print(singleNumber(arr))
