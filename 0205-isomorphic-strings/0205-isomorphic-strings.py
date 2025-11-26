class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}

        l_s = list(dict.fromkeys(s))
        l_t = list(dict.fromkeys(t))

        if len(l_t)!=len(l_s):
            return False
        else:
            for i in range(len(l_t)):
                dict[l_t[i]] = l_s[i]
            out = ""

            for i in t:
                if i in dict.keys():
                    out += dict[i]
            if out == s:
                return True
            else:
                return False