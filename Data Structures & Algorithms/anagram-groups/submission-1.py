class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = tuple(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


# from collections import defaultdict
# d = defaultdict(list)

# d['fruits'].append('apple')
# d['vegetables'].append('carrot')
# print(d.values())

#ouput: dict_values([['apple'], ['carrot']])

# sortedS gives a list of sorted version of a word which we want to use as a key.
# But list is mutable and a key should be immutable, so we convert it into tuple().
# And mapped this key with each s, s-> act pots tops cat stop hat
# In this way, the dictionary is built and we accessed the values of keys and converted it to a list


