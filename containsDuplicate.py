def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashmap = {}
    for index, num in enumerate(nums):
        if (num in hashmap):
            return True
        else:
            hashmap[num] = index
    return False
