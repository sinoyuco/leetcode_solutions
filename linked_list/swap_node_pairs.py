def swapPairs(head):
    if not head:
        return None
    if not head.next:
        return head

    behind, ahead = head, head.next

    behind.next = swapPairs(ahead.next)
    ahead.next = behind
    return ahead