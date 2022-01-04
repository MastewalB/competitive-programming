class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = dict()
        pairs = 0

        for i in time:
            mod = ((i - (i % 60)) + 60) - i
            if count and count.get(60 - mod):
                pairs += count[60 - mod]

            if count and count.get(mod):
                if mod == 60:
                    pairs += count[mod]
                count[mod] += 1
            else:
                count[mod] = 1
        return pairs
