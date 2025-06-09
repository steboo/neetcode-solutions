class Solution:
    # Idea: We can count the number of characters in
    # each string and use those as indicies to find
    # the original strings in our decoded string.
    def encode(self, strs: List[str]) -> str:
        delimiter = ','
        count_string = ""
        for s in strs:
            count_string += str(len(s)) + delimiter
        if len(strs) == 0:
            count_string += delimiter
        count_string += delimiter
        encoded_string = count_string + "".join(strs)
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        if s == ',,':
            return []
        counts = []
        num = 0
        marker = False
        index = 0
        for ch in s:
            index += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
                marker = False
            elif ch == ',':
                if marker:
                    break
                marker = True
                counts.append(num)
                num = 0
            else:
                raise ValueError("Improperly encoded string: unexpected character " + ch)
        
        strs = []
        for count in counts:
            strs.append(s[index:index + count])
            index += count
        return strs
