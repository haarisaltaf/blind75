def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    array = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                array.append(i)
                array.append(j)
    return array


# print(twoSum([2, 7, 11, 15], 9))


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    keyPair = {}
    for index, num in enumerate(nums):
        print(keyPair)
        if (target - num) not in keyPair:
            keyPair[num] = index
        else:
            return [index, keyPair[target - num]]


print(twoSum([2, 7, 11, 15], 9))
