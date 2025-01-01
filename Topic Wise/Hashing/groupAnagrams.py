# Group Anagrams LC 49

strs=["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    res={}
    for s in strs:
        # print(s)
        key=''.join(sorted(s))
        # print(key)
        # print(list(res))
        if key in res:
            res[key].append(s)
            # print(res)
        else:
            res[key]=[s]
            # print(res)

    return list(res.values())

print(groupAnagrams(strs))    