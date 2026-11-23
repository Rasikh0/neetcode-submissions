class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1

        # Part 1: one box per amount, all starting as "impossible"
        fewest = [impossible] * (amount + 1)
        fewest[0] = 0

        # Part 2: fill in every amount from 1 up to the target
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    fewest[a] = min(fewest[a], fewest[a - coin] + 1)

        # Part 3: still impossible? Then it can't be done
        if fewest[amount] == impossible:
            return -1
        return fewest[amount]