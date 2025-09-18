class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
# sorted then rotated. find minimum. if midpoint is smaller then leftmost item then inflection is on the left else right. then binary search on the correct half and repeat till.

        while left < right:
            middle = (right + left) // 2

            if nums[right] >= nums[middle]:
                right = middle
            else:
                left = middle + 1

        return nums[left]
