def find_pairs_with_sum(numbers, target):
    """
    Finds all pairs in the list whose sum is equal to target.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    pairs = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


def binary_search(arr, key):
    """
    Performs binary search after sorting the array.
    Time Complexity: O(n log n)
    """
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low += 1
        else:
            high -= 1

    return -1


def calculate_average(values):
    """
    Calculates average of values.
    """
    total = 0
    for v in values:
        total += v
    return total / len(values)


def main():
    data = [10, 20, 30, 40, 50, 60]
    target_sum = 70
    key = 40

    pairs = find_pairs_with_sum(data, target_sum)
    index = binary_search(data, key)
    average = calculate_average(data)

    print("Pairs with sum:", pairs)
    print("Index of key:", index)
    print("Average:", average)


main()

