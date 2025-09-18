class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        returnArray = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while right > left:
                result = nums[i] + nums[left] + nums[right]
                if result > 0:
                    right -= 1
                elif result < 0:
                    left += 1
                else:
                    returnArray.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    # need to increment pointer without hitting a duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return returnArray
# by sorting the array we can use fix i using the for loop and use two pointers to adjust based on if the current calc is greater than or less thna 0. so move right if greater than 0 and move left if less than 0
