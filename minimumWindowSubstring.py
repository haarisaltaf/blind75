class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # TODO: doesnt work, only gets the first min substring

        needHash = {}

        # needHash populated with the counts of each char in t
        for char in t:
            if char not in needHash:
                needHash[char] = 1
            else:
                needHash[char] += 1

        haveCount, haveHash = 0, {}
        needCount = len(needHash)

        if t == "":
            return ""

        minResult = float('inf')
        resultString = ""
        left = 0
        check = False
        for right in range(len(s)):
            # if dont have the correct num of distinct elements in have
            print(s[right], haveHash.get(s[right], 0))
            haveHash[s[right]] = 1 + haveHash.get(s[right], 0)
            haveCount = len(haveHash)

            if haveCount >= needCount:
                # same or more of distinct elements
                for key in needHash.keys():
                    if haveHash.get(key, 0) < needHash[key]:
                        check = False
                        break
                    check = True
                if check:
                    # if we have the correct keys in the substring
                    currentResultLength = right - left + 1
                    if currentResultLength < minResult:
                        minResult = min(currentResultLength, minResult)
                        resultString = s[left:right]
                        check = False
                        left + 1
                    while needHash.get(s[left], 0) == 0:
                        left += 1
        return resultString


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # taking a substring and checking if every letter of t is in there the correct num of times
        # else return ""
        if len(t) > len(s):
            return ""

        countT = {}
        for i in range(len(t)):
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1

        def dictContainedCheck(dict1, dict2):
            for dictPair in dict1:
                if dict2.get(dictPair, 0) < dict1[dictPair]:
                    return False
            return True

        answerExists = False
        left = 0
        # need to count the occurances of the needed chars in the current window
        currentCount = {}
        currentMinSubstring = ""
        minSubstring = s

        for right in range(len(s)):
            currentCount[str(s[right])] = currentCount.get(
                str(s[right]), 0) + 1

            # HACK: change substring to change based on length
            while dictContainedCheck(countT, currentCount):
                # if countT is a subset of currentCount
                currentMinSubstring = s[left:right+1]
                currentCount[str(s[left])] = currentCount[str(s[left])] - 1
                if len(minSubstring) >= len(currentMinSubstring):
                    minSubstring = currentMinSubstring
                left += 1
                answerExists = True

        if answerExists:
            return minSubstring
        return ""
