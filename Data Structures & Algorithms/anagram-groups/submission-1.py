class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group = defaultdict(list)
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     group[key].append(word)
        # return list(group.values())
        group = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] +=1
            key = tuple(count)
            group[key].append(word)
        return list(group.values())