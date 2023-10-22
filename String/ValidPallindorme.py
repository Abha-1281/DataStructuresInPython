# Given a String . After converting all uppercase letters into lowercase letters and removing all non-alphanumeric
# characters, Check if its a pallindromic string or not


def isPalindrome(s):
    new_str = ""
    for i in s:
        if i.isalnum():
            new_str += i

    return new_str.lower() == new_str.lower()[::-1]


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
