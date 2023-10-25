# Group all string in a list such that all strings in a group are shifted versions of each other i.e the difference
# between consecutive characters for all character of the string are equal. As in the above example take acd, dfg and mop
# a c d -> 2 1
# d f g -> 2 1
# m o p -> 2 1

from collections import defaultdict


def groupStrings(strings):
    mp = defaultdict(list)
    for s in strings:
        key = ""
        for c in s:
            key += "#" + str((ord(c) - ord(s[0])) % 26)
        mp[key].append(s)
        print(list(mp.values()))


if __name__ == '__main__':
    str_list = ["acd", "dfg", "wyz",
                "yab", "mop", "bdfh",
                "a", "x", "moqs"]
    groupStrings(str_list)
