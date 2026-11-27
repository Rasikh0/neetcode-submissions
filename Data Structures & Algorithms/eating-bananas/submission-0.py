class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Part 1: the range of speeds the answer could be
        lo, hi = 1, max(piles)

        # Part 2: keep halving until only one speed is left
        while lo < hi:
            mid = (lo + hi) // 2

            # Part 3: count the hours needed at speed mid
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid   # p / mid, rounded up

            # Part 4: keep the half that still holds the answer
            if hours <= h:
                hi = mid        # mid works, so the answer is mid or slower
            else:
                lo = mid + 1    # mid is too slow, so the answer is faster

        # Part 5: lo == hi, which is the slowest speed that works
        return lo