from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        
        frequencies = Counter(s)
        used = set()
        deletions = 0

        for freq in frequencies.values():
            while freq > 0 and freq in used:
                freq -= 1
                deletions += 1
            
            if freq > 0:
                used.add(freq)
        
        return deletions