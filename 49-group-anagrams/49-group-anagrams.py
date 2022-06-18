class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for s in strs:
            set_s = ''.join(sorted(s))
            if set_s not in ana_dict:
                ana_dict[set_s] = [s]
            else:
                ana_dict[set_s].append(s)
        return list(ana_dict.values())
        