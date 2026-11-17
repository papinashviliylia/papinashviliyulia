def cumulative_sum(lst):
    result = []
    current_sum = 0

    for num in lst:
        current_sum += num
        result.append(current_sum)

    return result

print(cumulative_sum([1, 2, 3]))
print(cumulative_sum([]))
print(cumulative_sum([-1, 1, -1]))
print(cumulative_sum([1.5, 2.5]))
