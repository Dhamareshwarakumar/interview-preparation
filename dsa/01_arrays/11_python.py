def maxOnes(arr):
    count = 0
    result = 0
    for i in range(len(arr)):
        if (arr[i] == 1):
            count += 1
        else:
            count = 0
        if (count > result):
            result = count
    return result


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(maxOnes(arr))
