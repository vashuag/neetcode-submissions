
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        strsg = ""
        for word in strs:
            strsg += str(len(word)) + "#" + word
        return strsg

    def decode(self, s: str) -> List[str]:
        strsl = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter
            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Extract the word
            start = j + 1
            end = start + length
            strsl.append(s[start:end])

            i = end

        return strsl
