def removeDuplicates(head):
    node = pointer = head
    while node.next:
        print(node.data)
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head
