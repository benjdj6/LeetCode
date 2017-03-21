class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        freq = {}
        out = []
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        for key, val in counts.iteritems():
            if val not in freq:
                freq[val] = [key]
            else:
                freq[val].append(key)
        values = freq.values()
        i = len(freq) - 1
        while i >= 0:
            if len(out) == k:
                break
            else:
                out.append(values[i].pop(0))
                if len(values[i]) == 0:
                    i -= 1
        return out
