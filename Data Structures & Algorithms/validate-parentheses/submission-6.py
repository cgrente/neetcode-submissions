class Solution:
    def isValid(self, s: str) -> bool:
        last_seen = []

        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                last_seen.append(')')
            elif ch == '{':
                last_seen.append('}')
            elif ch == '[':
                last_seen.append(']')
            elif ch == '}' or ch == ')' or ch == ']':
                if not last_seen or last_seen.pop() != ch:
                    return False

        return len(last_seen) == 0