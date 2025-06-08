class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        for n in nums:
            if n not in bucket:
                bucket[n] = 1
            else:
                bucket[n] += 1
        return [x[0] for x in sorted(bucket.items(), key=lambda kv: kv[1], reverse=True)[0:k]]
