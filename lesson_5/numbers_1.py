from itertools import islice

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 167, 15, 16, 39, 2, 3, 3, 5, 5, 5, 89]

# for i, j in enumerate(src):
#     if src[i] < src[i + 1]:
#         print(src[i + 1])
# for i in range(len(src) - 1):
#     if src[i] < src[i + 1]:
#         print(src[i + 1])

nums = (src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1])
print(*islice(nums, len(src)))
