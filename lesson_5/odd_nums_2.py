from itertools import islice


def odd_nums(max_num):
    odd_num = (num for num in range(1, max_num + 1, 2))
    return odd_num


new_odd_nums = odd_nums(17)
print(*islice(new_odd_nums, 3))
