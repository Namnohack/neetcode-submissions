class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        mapping = { ")" : "(", "]" :"[", "}":"{"}
        
        for b in s:
            if b in mapping.values():
                a.append(b)
            elif b in mapping.keys():
                if not a or mapping[b] != a.pop():
                    return False

        return not a
