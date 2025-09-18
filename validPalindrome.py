def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    cleaned = ''.join(char for char in s if char.isalnum()).lower()

    left, right = 0, len(cleaned)-1
    if len(s) == 1 or len(cleaned) == 0:
        return True

    while left <= right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True
