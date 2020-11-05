def getNode(head, positionFromTail):
    slow = fast = head
    for i in range(positionFromTail):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.data