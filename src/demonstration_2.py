"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    current_node = head_of_list
    prev_node = None
    next_node = None

    while current_node:
        # set next_node, access preserved
        next_node = current_node.next

        # make current_node, point prev_node
        current_node.next = prev_node

        # shift current_node & prev_node pointers to right
        prev_node = current_node
        current_node = next_node

    return prev_node

def print_list(head_of_list):
    # start at head as current_node
    # iterate through list, print values
    current_node = head_of_list
    str_result = ''

    while current_node:
        str_result += f'({current_node.value}) -> '
        # move current_node forward
        current_node = current_node.next

    print(str_result)


head = LinkedListNode(4)
head.next = LinkedListNode(3)
head.next.next = LinkedListNode(2)
head.next.next.next = LinkedListNode(1)
​
print_list(head)
new_head = reverse(head)
print_list(new_head)
