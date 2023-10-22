def groupAnagrams( strs):
    dic = {}
    for eachStr in strs:

        # print(eachStr)
        # print(sorted(eachStr))
        lexoSort = "".join(sorted(eachStr))
        # print(lexoSort)
        if lexoSort not in dic:
            dic[lexoSort] = []
            dic[lexoSort].append(eachStr)
        else:
            dic[lexoSort].append(eachStr)

    return list(dic.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
