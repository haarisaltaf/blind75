# encode to include both the lengoth of the following string ALONGSIDE THE DELIMITER. so if the nim isnt there

class Solution:

    def encode(self, strs: List[str]) -> str:
        returnString = ""
        for string in strs:
            returnString += f"{len(string)}#{string}"
        print(returnString)
        return returnString

    def decode(self, s: str) -> List[str]:
        # in: string encoded, look for 'int#' then append the string AFTER the hashtag with alength of the integer to the final list. keep going until the end of the string?
        returnList = []
        stringCounter = 0

        while stringCounter < len(s):
            if s[stringCounter] == "#" and stringCounter > 1:
                try:
                    appendString = s[stringCounter +
                                     1:stringCounter + int(s[stringCounter-1])]
                    returnList.append(appendString)
                except TypeError:
                    stringCounter += 1
                stringCounter += 1
        return returnList


class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        return str("±§±±§±".join(strs))

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split("±§±±§±")
