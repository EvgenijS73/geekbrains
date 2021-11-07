src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
numbers = []
for el in src:
    if src.count(el) == 1:
        numbers.append(el)
print(numbers)

nums = [el for el in src if src.count(el) == 1]
print(nums)
