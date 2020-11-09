def findSuccessorNode(root):
    if not root:
        return None
        
    if root.right:
        r = root.right
        while r.left:
            r = r.left
        return r
    else:
        a = root
        par = a.parent
        while par and par.left != a:
            a = par
            par = par.parent
        return par
