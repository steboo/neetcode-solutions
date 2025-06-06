class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time and space
        if len(s) != len(t):
            return False
        seen = {} # ideally use a defaultdict
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        for letter in t:
            if letter in seen and seen[letter] > 0:
                seen[letter] -= 1
            else:
                return False

        return True
