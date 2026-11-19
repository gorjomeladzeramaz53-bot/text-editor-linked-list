from text_editor import TextEditor


if __name__ == "__main__":
    ed = TextEditor()
    ed.add_line("A")
    ed.add_line("B")
    ed.add_line("C")
    ed.delete_line(1)  # A, C
    ed.undo()         # A, B, C
    ed.undo()         # A, B
    ed.redo()         # A, B, C
    ed.add_line("D")  # A, B, C, D (redo სტეკი გასუფთავდა)
    ed.redo()         # არაფერი ხდება
    ed.show()