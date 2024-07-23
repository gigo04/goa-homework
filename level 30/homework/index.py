def odd_index_sum(numbers):
    sum_odd_indices = 0

    for i in range(1, len(numbers), 2):
        sum_odd_indices += numbers[i]
    
    return sum_odd_indices

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = odd_index_sum(numbers_list)
print("Sum of numbers at odd indices:", result)
