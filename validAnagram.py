def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    sHash = {}
    tHash = {}

    for i in range(len(s)):
        if s[i] not in sHash:
            sHash[s[i]] = s.count(s[i])

        if t[i] not in tHash:
            tHash[t[i]] = t.count(t[i])

    if sHash == tHash:
        return True

    return False

print(isAnagram("aacc", "ccac"))
