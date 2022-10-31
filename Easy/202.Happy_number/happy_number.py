class Solution:
    def isHappy(self, n: int) -> bool:
        alreadySeen = defaultdict(int)
        while n != 1:
            current = 0
            while n != 0:
                rem = n % 10
                n = n // 10
                current += rem ** 2
            if alreadySeen.get(current, -1) == current:
                return False
            n = current
            alreadySeen[current] = current
        return True