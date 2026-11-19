class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def append(self, data: str) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert_at(self, index: int, data: str) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == self._size:
            self.append(data)
            return

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node

        self._size += 1

    def delete_at(self, index: int) -> str:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return removed.data

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next
        if removed is self.tail:
            self.tail = prev

        self._size -= 1
        return removed.data