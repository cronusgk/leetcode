class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        totalMatches = 0
        while (n > 1):
            if (n % 2 == 0):
                matches = int(n / 2)
                n = int(n / 2)
            else:
                matches = int((n - 1) / 2)
                n = (int((n-1) / 2)) + 1
            totalMatches += matches
        return totalMatches

