class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


# from collections import defaultdict
# d = defaultdict(list)

# d['fruits'].append('apple')
# d['vegetables'].append('carrot')
# print(d.values())

#ouput: dict_values([['apple'], ['carrot']])

# sortedS gives the sorted version of a word which we used as a key.
# And mapped this key with each s, s-> act pots tops cat stop hat
# In this way, the dictionary is built and we accessed the values of keys and converted it to a list


#.join() : If we do not use .join then sortedS will store this:
# ['a', 'c', 't']
# ['o', 'p', 's', 't']
# ['o', 'p', 's', 't']
# ['a', 'c', 't']
# ['o', 'p', 's', 't']
# ['a', 'h', 't']

#by using .join():

# act
# opst
# opst
# act
# opst
# aht
