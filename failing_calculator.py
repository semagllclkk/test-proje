def average_ratios(numbers):
    total = 0
    count = 0
    for i in range(len(numbers)):
        # Skip zero values to avoid division by zero
        if numbers[i] != 0:
            total += 100 / numbers[i]
            count += 1
    return total / count if count > 0 else 0

print(average_ratios([10, 5, 0]))
