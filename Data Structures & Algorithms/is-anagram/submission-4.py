class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # count length

# count the letter amount and if the letter amounts are the same the they are anagrams

        x = {} #dict
        for char in s:
            if char in x:
                x[char] += 1
            else:
                x[char] = 1

        for char in t:
            if char in x:
                x[char] -= 1
            else:
                return False
        
        for count in x.values():
            if count != 0:
                return False

        return True

