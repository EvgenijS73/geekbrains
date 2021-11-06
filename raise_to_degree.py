# odd_nums = []
new_odd_nums = []
numerous = []
num = 1000

odd_nums = [i ** 3 for i in range(num + 1) if i % 2 != 0]
print(odd_nums)

# for i in range(num + 1):
#     if i % 2 != 0:
#         raise_num = i ** 3
#         odd_nums.append(raise_num)

for num in odd_nums:
    sum_of_odd_nums = 0
    if num > 0:
        n = num // 100000000
        u = num // 10000000 % 1000000 % 10
        m = num // 1000000 % 1000000 % 10
        b = num // 100000 % 100000 % 10
        e = num // 10000 % 10000 % 10
        r = num // 1000 % 1000 % 10
        o = num // 100 % 100 % 10
        f = num // 10 % 10
        s = num % 10
        sum_of_odd_nums = (n + u + m + b + e + r + o + f + s) % 7
    if sum_of_odd_nums == 0:
        new_odd_nums.append(num)

print(new_odd_nums)
print(sum(new_odd_nums))

for num in range(len(new_odd_nums)):
    new_odd_nums[num] += 17

print(new_odd_nums)
print(sum(new_odd_nums))

for num in new_odd_nums:
    sum_num_of_new_odd_numbers = 0
    if num > 0:
        n = num // 100000000
        u = num // 10000000 % 1000000 % 10
        m = num // 1000000 % 1000000 % 10
        b = num // 100000 % 100000 % 10
        e = num // 10000 % 10000 % 10
        r = num // 1000 % 1000 % 10
        o = num // 100 % 100 % 10
        f = num // 10 % 10
        s = num % 10
        sum_num_of_new_odd_numbers = (n + u + m + b + e + r + o + f + s) % 7
    if sum_num_of_new_odd_numbers == 0:
        numerous.append(num)
    else:
        print('there is no numbers satisfying the condition!')
        break

print(numerous)
