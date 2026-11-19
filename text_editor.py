from linked_list import SinglyLinkedList


class TextEditor:
    def __init__(self):
        self.lines = SinglyLinkedList()
        self._undo_stack: list[tuple[str, int, str]] = []
        self._redo_stack: list[tuple[str, int, str]] = []

    def add_line(self, text: str) -> None:
        idx = len(self.lines)
        self.lines.append(text)
        self._undo_stack.append(("insert", idx, text))
        self._redo_stack.clear()

    def insert_line(self, index: int, text: str) -> None:
        self.lines.insert_at(index, text)
        self._undo_stack.append(("insert", index, text))
        self._redo_stack.clear()

    def delete_line(self, index: int) -> None:
        removed_text = self.lines.delete_at(index)
        self._undo_stack.append(("delete", index, removed_text))
        self._redo_stack.clear()

    def undo(self) -> None:
        if not self._undo_stack:
            return

        action, index, text = self._undo_stack.pop()
        if action == "insert":
            self.lines.delete_at(index)
            self._redo_stack.append(("insert", index, text))
        elif action == "delete":
            self.lines.insert_at(index, text)
            self._redo_stack.append(("delete", index, text))

    def redo(self) -> None:
        if not self._redo_stack:
            return

        action, index, text = self._redo_stack.pop()
        if action == "insert":
            self.lines.insert_at(index, text)
            self._undo_stack.append(("insert", index, text))
        elif action == "delete":
            self.lines.delete_at(index)
            self._undo_stack.append(("delete", index, text))

    def show(self) -> None:
        for i, line in enumerate(self.lines, start=1):
            print(f"{i}: {line}")