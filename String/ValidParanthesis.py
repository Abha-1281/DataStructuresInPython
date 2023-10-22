def isValid(s):
    st = []
    mapped = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for i in s:
        if i in "({[":
            st.append(i)
        else:
            if st:
                if st[-1] == mapped[i]:
                    st.pop()
                else:
                    return False
            else:
                return False

    if st:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "()[]{}"
    print(isValid(s))
