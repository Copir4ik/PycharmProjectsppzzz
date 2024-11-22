def count_subsegments_with_max_fraction(n, arr):
    max_ratio = 0
    count = 0

    for i in range(n):
        current_min = arr[i]
        current_max = arr[i]

        for j in range(i, n):
            current_min = min(current_min, arr[j])
            current_max = max(current_max, arr[j])
            ratio = current_max / current_min

            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

    return count


# Входные данные
n = int(input())
arr = list(map(int, input().split()))

# Вывод результата
print(count_subsegments_with_max_fraction(n, arr))
