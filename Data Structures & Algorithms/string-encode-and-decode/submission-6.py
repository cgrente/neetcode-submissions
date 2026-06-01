class Solution:

    def encode(self, strs: List[str]) -> str:
        parts: List[str] = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        decoded_str: List[str] = []
        len_str = ""
        len_int = 0
        i = 0
        while i < len(s):
            ch = s[i]
            
            if ch != "#":
                len_str += ch
                i += 1
            else:
                len_int = int(len_str)
                start = i + 1
                end = start + len_int
                decoded_str.append(s[start:end])
                len_str = ""
                i = end          # jump to next frame
                len_int = 0
                continue         # prevents i += 1

        return decoded_str
