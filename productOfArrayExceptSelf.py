class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Prefix and suffix addition

        # prefix = [:i]
        # suffix = [i:]
        # 2 pointer, one from right, one from left to add each side

        # ins: nums array
        # calc: prefix and suffix. prefix caches/ stores everytihng the left index's cumult. mult. to then be multiplied by the suffix.

        # outs`: array of nums multiplyed by everything to the left and right of it
        returnArray = [1] * len(nums)

        prefix, suffix = 1,1
        for i in range(len(nums)):
            returnArray[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            returnArray[i] *= suffix
            suffix *= nums[i]

        return returnArray
