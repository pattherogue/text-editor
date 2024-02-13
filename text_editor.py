class TextEditor:
    def __init__(self):
        self.text = ""
        self.edit_history = []
        self.redo_history = []

    def display_text(self):
        print("Current Text:")
        print(self.text)

    def insert_text(self, new_text):
        self.edit_history.append(self.text)
        self.redo_history = []  # Clear redo history
        self.text += new_text
        self.display_text()  # Display the updated text

    def delete_text(self, num_chars):
        self.edit_history.append(self.text)
        self.redo_history = []  # Clear redo history
        self.text = self.text[:-num_chars]
        self.display_text()  # Display the updated text

    def undo(self):
        if self.edit_history:
            self.redo_history.append(self.text)
            self.text = self.edit_history.pop()
            self.display_text()  # Display the updated text

    def redo(self):
        if self.redo_history:
            self.edit_history.append(self.text)
            self.text = self.redo_history.pop()
            self.display_text()  # Display the updated text

def main():
    editor = TextEditor()
    while True:
        print("\nOptions:")
        print("1. Insert text")
        print("2. Delete text")
        print("3. Undo")
        print("4. Redo")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            text_to_insert = input("Enter text to insert: ")
            editor.insert_text(text_to_insert)
        elif choice == '2':
            try:
                num_chars_to_delete = int(input("Enter number of characters to delete: "))
                if num_chars_to_delete < 0:
                    raise ValueError("Number of characters to delete must be non-negative.")
                editor.delete_text(num_chars_to_delete)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '3':
            editor.undo()
        elif choice == '4':
            editor.redo()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
