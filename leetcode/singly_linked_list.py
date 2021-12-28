# Pros
# O(c) insertion and deletions in any position, regular list have o(n)
# LinkedLists can continue to expand without having to specify their size in the beginning
#
# Cons
# To insert  a element into a LinkedList its O(k) time unlike a regular list its O(c)


class Node:
    def __init__(self, value):
        # ignore these for now, they are not being used
        # self.head = None
        # self.tail = None
        self.value = value
        self.prev_node = None
        self.next_node = None


def SinglyLinkedList():
    # create the Nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    # assign the singly linked pointers
    a.next_node = b
    b.next_node = c
    c.next_node = d

    # uncomment if you want a cycle in the LinkedList
    # d.next_node = a

    print("Your LinkedList has been created")
    print(f"{a.value} -> {b.value} -> {c.value} -> {d.value} -> {d.next_node}")

    return a, b, c, d


def cycle_check(root_node):
    marker1 = root_node
    marker2 = root_node

    while marker2 is not None and marker2.next_node is not None:

        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


def get_size(root_node):
    # calculates the size of a singly linked list
    size_counter = 1
    while root_node.next_node is not None:
        root_node = root_node.next_node
        size_counter += 1

    return size_counter


def traverse_linked_list(root_node):
    while root_node.next_node is not None:
        root_node = root_node.next_node
    print(f"I just traversed my linked list and Tail Node is: {root_node.value}")


def reverse_linked_list(root_node):
    # traverse the linked list until you get the to tail node
    traverse_linked_list(root_node)

    # now keep calling the previous node until you get to the head node
    while root_node.prev_node is not None:
        root_node = root_node.prev_node

    print(f"I just reversed my linked list and Head Node is: {root_node.value}")


def reverse_linked_list_pointers(root_node):
    # This will literally flip the way that the linked list is pointing
    # For Example: 1 -> 2 -> 3 -> 4
    # Become this: 1 <- 2 <- 3 <- 4

    # This will create the Nodes and assign the pointers

    current_node = root_node
    previous_node = None
    next_node = None

    while current_node is not None:

        next_node = current_node.next_node
        current_node.next_node = previous_node

        # because we are changing the value of the current Node, make it the next nodes previous node
        previous_node = current_node
        # move the Node along to the next Node
        current_node = next_node

    print(f"{a.next_node} <- {b.next_node.value} <- {c.next_node.value} <- {d.next_node.value} <- {d.value}")


def linked_list_nth_node(root_node, nth_node):
    # create a counter and once that counter == the nth_node, return the current_node
    counter = 1
    current_node = root_node

    if counter == nth_node:
        return current_node.value

    while counter != nth_node:
        current_node = current_node.next_node
        counter += 1

    return current_node.value


def linked_list_nth_to_last_node(root_node, nth_node):
    # get the size of the LinkedList
    size_of_linked_list = get_size(root_node)
    node_we_are_looking_for = size_of_linked_list - nth_node

    current_node = root_node
    counter = 0

    if counter == nth_node:
        return current_node.value

    while counter != node_we_are_looking_for:
        current_node = current_node.next_node
        counter += 1

    return current_node.value


a, b, c, d = SinglyLinkedList()
# print(cycle_check(a))
# reverse_linked_list(a)
# reverse_linked_list_pointers(a)
# print(linked_list_nth_node(a, 3))
# print(linked_list_nth_to_last_node(a, 3))





