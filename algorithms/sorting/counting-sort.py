def countingSort(nums):
    count = [0] * (max(nums) + 1)
    for num in nums:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1
    return output

nums = [1, 2, 3, 0, 6, 0, 1, 1, 3]
nums = countingSort(nums)
print('after', nums)