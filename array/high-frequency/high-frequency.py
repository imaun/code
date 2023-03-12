def highFrequency(nums):
    dic = {}
    max_count = 0
    for x in nums:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] = dic[x] + 1
        max_count = max(max_count, dic[x])
    return max_count


example = [1, 2, 4, 5, 6, 7, 5, 5]
print(highFrequency(example))  # prints 3
