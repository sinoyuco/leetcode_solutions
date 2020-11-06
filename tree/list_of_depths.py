def list_of_depths(root):
    if not root:
        return None
    queue = [root]
    res = []
    while queue:
        l, temp = [], []

        while len(queue) > 0:
            el = queue.pop()
            l.append(el.val)
            if el.left:
                temp.append(el.left)
            if el.right:
                temp.append(el.right)
        if l:
            p1 = p = ListNode(l[0])
            for i in range(1,len(l)):
                a = ListNode(l[i])
                p.next = a
                p = p.next
                res.append(p1)
        queue = temp
        

        
        
        
        
