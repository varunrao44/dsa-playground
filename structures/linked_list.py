"""
Day 1 - 1st July 2026
Singly Linked List
Goal for today: implement Node + append, and a visualise() that prints
the list state after every operation so that we can see the pointers
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        """Add a new node to the end of the list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def visualize(self):
        """Print the list as [a] -> [b] -> [c] -> None"""
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        print(" -> ".join(parts))

if __name__ == '__main__':
    l1 = LinkedList()
    l1.visualize()

    l1.append(3)
    l1.visualize()

    l1.append(7)
    l1.append(33)
    l1.visualize()
