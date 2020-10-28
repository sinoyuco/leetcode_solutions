def hasCycle2(head):
    fast = slow = head
    # find the first node at which the pointers come together
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    else:
        return None

    # if you take slow pointer back to the head, 
    # they will be at equal distance to the node 
    # that is the starting point of the cycle.
    
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow