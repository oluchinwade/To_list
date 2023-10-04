from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_count = {}

        for num in nums:
            if num in num_count:
                count += num_count[num]
                num_count[num] += 1
            else:
                num_count[num] = 1

        return count

solution = Solution()
nums = [1, 2, 3, 1, 1, 3]
print(solution.numIdenticalPairs(nums))