def calculate_sum_v1(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total


def calculate_sum_v2(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total


def calculate_average_v1(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)


def calculate_average_v2(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total / len(numbers)


def search_pairs(numbers, target):
    result = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] == target:
                    result.append((numbers[i], numbers[j]))

    return result


def process_data(data):
    if data is not None:
        if len(data) > 0:
            if type(data) == list:
                sum1 = calculate_sum_v1(data)
                sum2 = calculate_sum_v2(data)
                avg1 = calculate_average_v1(data)
                avg2 = calculate_average_v2(data)

                print("Sum1:", sum1)
                print("Sum2:", sum2)
                print("Avg1:", avg1)
                print("Avg2:", avg2)

                pairs = search_pairs(data, 50)
                print("Pairs:", pairs)
            else:
                print("Invalid type")
        else:
            print("Empty list")
    else:
        print("No data")


def main():
    data = [10, 20, 30, 40, 10, 20]
    process_data(data)


main()
