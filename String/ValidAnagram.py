## Alternate solution is to use Counter method from collections module in python

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
