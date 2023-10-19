def findMedian(root):
    # code here
    # return the median

    def inorder(root, ans):
        if not root:
            return
        inorder(root.left, ans)
        ans.append(root.data)
        inorder(root.right, ans)

    def findMed(ans):
        if len(ans) // 2 == 0:
            a = len(ans) // 2
            b = (len(ans) // 2) + 1
            self.med = (a + b) // 2
        else:
            self.med = (len(ans) + 1) // 2

    self.med = -1
    inorderans = []
    inorder(root, inorderans)
    findMed(inorderans)

    return ans[self.med]
