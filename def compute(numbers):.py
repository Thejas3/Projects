def compute(numbers):
    result = 1
    for num in numbers:
        result *= num - 2
    return result

values = [4, 7, 5]
computed_value = compute(values)
print(computed_value)