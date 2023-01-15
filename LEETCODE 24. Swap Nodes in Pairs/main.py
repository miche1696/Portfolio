
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: ListNode) -> ListNode:
        nodo1 = head
        if(head.next):
            nodo2 = head.next
            newhead = nodo2
        else:
            return head
        if(head.next.next):
            nodo3 = head.next.next
        while(nodo1 and nodo2):
            nodo1.next = nodo3
            nodo2.next = nodo1
            nodo1 = nodo3
            if(nodo3.next):
                nodo2 = nodo3.next
                if(nodo3.next.next):
                    nodo3 = nodo3.next.next
        return newhead

if __name__=="__main__":
    node6 = ListNode(6)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    head = ListNode(0, node1)
    swapPairs(head)
    while(head):
        print(f"{head.val} - ")
        head=head.next
