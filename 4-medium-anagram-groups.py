class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea 1: sort all strings alphabetically O(m*nlgn)
        #         where m=number of strings, n=number of charcters
        # idea 1a: special sort to reach O(n)
        # idea 2: calculate/hash each string
        #   f(n) => deterministic value
        # This implements idea 1...
        sorted_strs = []
        for s in strs:
            sorted_strs.append((s, ''.join(sorted(s))))
        sorted_strs.sort(key=lambda x: x[1])

        group = []
        current_group = []
        last_str = None
        for orig_s, hash_s in sorted_strs:
            if last_str is None or last_str == hash_s:
                current_group.append(orig_s)
            else:
                group.append(current_group)
                current_group = [orig_s]
            last_str = hash_s
        group.append(current_group)
        return group
