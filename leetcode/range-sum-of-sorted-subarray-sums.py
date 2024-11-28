class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        # Brute force
        # stack = []
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         stack.append(sum)
        # stack.sort()
        # print(stack)
        # # O(N)
        # res = 0
        # for i in range(left -1, right):
        #     res += stack[i]
        # return res % 1000_000_007

        def count_and_sum_subarrays(array, threshold: int):
            count, total_sum, current_window_sum, running_sum = 0, 0, 0, 0
            start = 0

            for end, num in enumerate(array):
                running_sum += num * (end - start + 1)
                current_window_sum += num
                while current_window_sum > threshold:
                    running_sum -= current_window_sum
                    current_window_sum -= array[start]
                    start += 1
                count += end - start + 1
                total_sum += running_sum

            return count, total_sum
        
        def calculate_sum_of_first_k_subarrays(array, k: int) -> int:
            low, high = min(array), sum(array)
            while low < high:
                mid = (low + high) // 2
                if count_and_sum_subarrays(array, mid)[0] < k:
                    low = mid + 1
                else:
                    high = mid
            count, sum_value = count_and_sum_subarrays(array, low)
            return sum_value - low * (count - k)
        
        def findSubArrays(nums, threshold):
            print('finding arrays with sum <=', threshold)
            left, right = 0, 0
            currentSum = 0 # sum of current window
            totalSum = 0 # sum of all valid subarrays
            count = 0 # num of valid subarrays
                # if currentSum <= threshold:
                #     print(f'Found {nums[left:right + 1]}, sum = {currentSum}, totalSum = {totalSum}')
            while left < n and right < n:
                currentSum += nums[right]
                while currentSum > threshold and left < right:
                    currentSum -= nums[left]
                    totalSum -= nums[left]
                    left += 1

                if left != right and nums[right] <= threshold:
                    count += 1
                    totalSum += nums[right]
                    print(nums[right:right+1], 'sum = ', nums[right])

                if currentSum <= threshold:
                    totalSum += currentSum
                    count += 1
                    print(nums[left:right + 1], 'sum = ', currentSum, 'total sum = ', totalSum)
                
                right += 1

            print('Total found:', count)
            print('Total sum: ', totalSum)
            return count, totalSum
        
        def findFirstKSmallestSubarrays(nums, k):
            print('--- Find k = ', k)
            left = min(nums)
            right = sum(nums)
            while left <= right:
                print('--- left, right = ', left, right)
                mid = (left + right) // 2
                count, totalSum = count_and_sum_subarrays(nums, mid)
                if count == k:
                    print('++++++ Final size = ', count)
                    print('++++++ Sum = ', totalSum)
                    return count, totalSum
                elif count < k:
                    left = mid + 1
                else:
                    right = mid - 1
                print('updated left right', left, right)
                        
            print('++++++>>> Final size = ', count)
            print('++++++>>> Sum = ', totalSum)
            if count > k:
                totalSum -= mid * (count - k)
                count -= count - k
                print('&&&&& adjusting', count, totalSum)
            return count, totalSum
        # findSubArrays(nums, 5)
        # findSubArrays(nums, 2)
        lSum = calculate_sum_of_first_k_subarrays(nums, left - 1)
        # print("###############################")
        rSum = calculate_sum_of_first_k_subarrays(nums, right)
        
        # print(f'There are {lCount}/{left - 1} smallest arrays found, there sum is {lSum}')
        # print(f'There are {rCount}/{right} smallest arrays found, there sum is {rSum}')
        # print("DEBUG DEBUG DEBUG")
        # print(find_subarrays_with_sum_less_than_k(nums, 8))
        return (int)((rSum - lSum) % (1e9 + 7))
    
nums, n, left, right = [1,2,3,4], 4, 1, 5 # 13
nums, n, left, right = [1,2,3,4], 4, 3, 4 # 6
nums, n, left, right = [1,2,3,4], 4, 1, 10 # 50

print(Solution().rangeSum(nums, n, left, right))