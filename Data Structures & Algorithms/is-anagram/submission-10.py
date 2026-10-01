class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns =  sorted(list(s))
        nt = sorted(list(t))
        print("".join(ns))
        return True if (len(ns) == len(nt) and "".join(ns) == "".join(nt) ) else False