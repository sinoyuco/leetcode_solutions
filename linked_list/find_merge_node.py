def findMergeNode(head1, head2):
    a, b = head1, head2
    while a and b:
        if not a.next:
            a = head1
        else:
            a = a.next

        if not b.next:
            b = head2
        else:
            b = b.next

        if a == b:
            return a.data
