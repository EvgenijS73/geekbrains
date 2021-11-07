from itertools import islice


def nums_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums = nums_gen(15)
print(*islice(nums, 5))
