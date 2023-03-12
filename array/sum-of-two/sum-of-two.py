def sumOfTwoNumbers(nums, target):
    dic = {}
    i = 0
    for x in nums:
        c = target - x
        if c in dic:
            return [dic.get(c), i]
        dic[x] = i
        i += 1


example = [0, 3, 5, 8, 1, 3, 9]
target = 11

print(sumOfTwoNumbers(example, target=target))
