import copy
from pprint import pprint


class Node:
    def __init__(self, value, prev=None, next=None) -> None:
        if value is None:
            raise ValueError("Value can't be None type")
        self.prev: Node | None = prev
        self.next: Node | None = next
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def __str__(self) -> str:
        if self.head is None:
            return "List is empty"
        return f"prev - {self.head.prev}, next - {self.head.next}, value - {self.head.value}"

    def add_node(self, value):
        if self.head:
            self.head.next = Node(value, prev=self.head)
            self.head = self.head.next
        else:
            self.head = Node(value)

    def pack(self, values: iter) -> None:
        for value in values:
            self.add_node(value)

    def unpack(self) -> list:
        """
        Returns a list of values from linked list by destroying yourself
        """
        values = []
        while not self.head is None:
            values.append(self.head.value)
            self.head = self.head.prev
        return values[::-1]

    def preview_unpack(self) -> list:
        """
        Returns a list of values from linked list by creating a deepcopy of list
        """
        values, copied_list = [], copy.deepcopy(self)
        while not copied_list.head is None:
            values.append(copied_list.head.value)
            copied_list.head = copied_list.head.prev
        return values[::-1]

    def show_list(self):
        values, copied_list = [], copy.deepcopy(self)
        while not copied_list.head is None:
            values.append(
                {
                    "prev": str(copied_list.head.prev),
                    "next": str(copied_list.head.next),
                    "value": str(copied_list.head.value),
                }
            )
            copied_list.head = copied_list.head.prev
        return values[::-1]


linked_list = LinkedList()
linked_list.pack([i for i in range(5)])
print(linked_list.preview_unpack())
pprint(linked_list.show_list())
print(linked_list.unpack())
print(linked_list)
