class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encode as: <len>#<string><len>#<string>...
        Using a list builder avoids quadratic string concatenation.
        """
        parts: List[str] = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        decoded_str: List[str] = []

        i = 0
        while i < len(s):
            # Read the length (can be multiple digits)
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # Read the payload of that length
            start = j + 1
            end = start + length
            decoded_str.append(s[start:end])

            # Move to the next frame
            i = end

        return decoded_str
