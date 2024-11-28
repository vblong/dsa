# https://leetcode.com/problems/split-array-largest-sum/

nums = [7, 2, 5, 10, 8]
k = 2
left = max(nums)
right = sum(nums)
result = right

def canSplit(limit, numOfGroups):
    currentNumOfGroups = 0
    currentSum = 0
    for n in nums:
        currentSum += n
        if currentSum > limit:
            currentSum = n
            currentNumOfGroups += 1
    return currentNumOfGroups + 1 <= numOfGroups


while left <= right:    
    mid = (left + right) // 2
    if canSplit(mid, k):
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)
