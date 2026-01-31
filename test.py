def search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


data = [1, 2, 3, 4, 5]
print(search(data, 9))
