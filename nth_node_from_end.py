def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    ahead = behind = head
    for i in range(n):
            ahead = ahead.next

    if not ahead:
        return behind.next

    while ahead.next:
        ahead = ahead.next
        behind = behind.next
        
    behind.next = behind.next.next
    return head
