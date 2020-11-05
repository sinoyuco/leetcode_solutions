
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDupsUnsorted(head):
    c, p = head, None
    s = set()
    while c:
        if c.val in s:
            p.next = c.next
        else:
            s.add(c.val)
            p = c
        c = c.next
    
    # curr,res = head, []
    # while curr:
    #     res.append(curr.val)
    #     curr = curr.next
    # print(res)
    return head



e = ListNode(3)
d = ListNode(2,e)
c = ListNode(2,d)
b = ListNode(1,c)
a = ListNode(2,b)

print(removeDupsUnsorted(a))




