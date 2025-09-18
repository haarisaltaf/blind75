class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        currMaxFreq = 0
        left = 0
        hashCount = {}  # counts the letters in the CURRENT WINDOW rather than entire string

        for right in range(len(s)):
            # adds the count for the current letter into hashmap or increments
            hashCount[s[right]] = hashCount.get(s[right], 0) + 1
            currMaxFreq = max(currMaxFreq, hashCount[s[right]])

            # while the window's replaceable letters are more than k we need to decrement via l
            while (right - left + 1) - currMaxFreq > k:
                hashCount[s[left]] -= 1
                left += 1
            # When the window has shifted the left pointer until we have the correct number of replacements we can check if thats the new longest length
            maxLength = max(maxLength, right - left + 1)

        return maxLength
