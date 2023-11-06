# Exercise 1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name of the publication: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author} Page_count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief_editor}")


publication1 = Magazine("Donald Duck", "Aki Hyppä")
publication2 = Book("Compartment No. 6", "Rosa Liksom", 192)

publication1.print_information()
publication2.print_information()






