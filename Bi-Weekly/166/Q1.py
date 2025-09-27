class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        tab = {}
        for ch in s:
            k = str(s.count(ch))
            if k not in list(tab.keys()):
                tab[k] = set()
            tab[k].add(ch)
        l = 0
        ke = list(tab.keys())[0]
        for key in tab.keys():
            c = len(tab[key])
            if c > l or (c == l and int(key) > int(ke)):
                l = c
                ke = key
        group = ""
        for ch in tab[ke]:
            group += ch
        return group