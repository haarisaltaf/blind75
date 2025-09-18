def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0

    left, right = 0, 1
    maxProfit = 0
      # check for the smallest and greatest value -- calculate greatest profit and store till bigger found
    while right < len(prices):
        if prices[right] > prices[left]:
            newProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, newProfit)
        else:
            left = right
        right += 1

    return maxProfit
