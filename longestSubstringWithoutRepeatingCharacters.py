class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # left and right opinter, if char has not been previously seen within this window, increment counter, else: max(maxLength, currCount) reset currCount and increment left pointer
        left, right = 0, 0
        check = set()
        maxLength = 0
        while right < len(s):
            if s[right] not in check:
                check.add(s[right])
                maxLength = max(right - left + 1, maxLength)
            else:
                while s[right] in check:
                    check.remove(s[left])
                    left += 1
                check.add(s[right])
            right += 1

        return maxLength
