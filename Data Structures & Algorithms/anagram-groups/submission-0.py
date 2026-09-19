class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for st in strs:
            if "".join(sorted(st)) in ana:
                ana["".join(sorted(st))].append(st)
            else:
                ana["".join(sorted(st))] = [st]
        return list(ana.values())