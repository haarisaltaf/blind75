from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # hashmap of key being the sorted string ie the anagram matches and the value being the original string

    returnList = defaultdict(list)

    for string in strs:
        sortedString = "".join(sorted(string))
        returnList[sortedString].append(string)
    print(returnList)
    return list(returnList.values())
