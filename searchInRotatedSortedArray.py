class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # in: sorted nums with distinct ints; k >= 1 and k < len(nums);
        left = 0
        right = len(nums)-1


        while left <= right:

            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]: # if left side is 
                if nums[left] <= target and target < middle:
                # if target is smaller than middle
                    right = middle - 1
                else:


            else:
                return middle
        return -1
