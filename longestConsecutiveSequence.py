class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if type(nums) is not list:
            return 0
        if nums == []:
            return 0
        # check for both the current count and the longest count
        count = 1
        longest = 0

        nums = list(set(nums))
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        print(nums)
        return max(longest, count)


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set to remove duplicates, if num +1 in set, ocunt hwile num+1 in set, count +1 -- for every n, if n+1 exists, check that consecutive numbers, then store as longest then reset count
        if nums == []:
            return 0
        longest = 0
        nums = set(nums)
        for num in nums:
            count = 1
            if num-1 not in nums:
                currentStartNum = num
                while currentStartNum+1 in nums:
                    count += 1
                    currentStartNum += 1
                longest = max(count, longest)
        return longest
