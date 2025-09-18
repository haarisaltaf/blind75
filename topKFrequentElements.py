import heapq


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # in: array[nums], int k
    # out: array[ints] -- most frequent k elements
    hash = {}  # {number: occurances}
    heap = []

    for num in nums:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] += 1
    # fills hash with number to number of occurances

    for key, value in hash.items():
        heapq.heappush(heap, (-value, key))
# heap filled in order with -ve values

    returnArray = []
    for i in range(k):
        returnArray.append(heapq.heappop(heap)[1])
    return returnArray

# heap is a binary tree (in python is a min heap) so the root is the smallest value with the leaves being the bigggest. --> for this question we need a max heap as we want in order of being the most common numbers so hasve key:value pair where key is the num of occurances and push onto heap as a negative so it simulates a max heap by inverting the values in a way.
