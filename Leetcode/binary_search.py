if __name__ == "__main__":

    arr = [0,1,2,3,4,5,6,7]
    target = 2.5

    start = 0
    end = len(arr) - 1

    output = -1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            output = arr[mid]
            break
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            output = arr[mid]
            start = mid + 1
    print("Output: ", output)