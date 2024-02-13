# Text Editor with Undo/Redo Functionality

This Python project implements a simple text editor that allows users to input and edit text, with support for undo and redo operations. The text editor demonstrates proficiency in various aspects of software development, including the effective use of data structures, efficient text manipulation, error handling, and memory management.

## Features

- **Undo/Redo Functionality**: The core feature of the text editor is the implementation of undo and redo functionality. This is achieved using the stack data structure to store the history of text edits made by the user. Each edit operation is pushed onto the stack, and when the user requests an undo operation, the most recent edit is popped from the stack and applied to the text. Redo operations involve popping edits from a redo stack and reapplying them to the text.

- **Efficient Text Manipulation**: The text editor efficiently handles text manipulation operations using Python's built-in string methods and slicing operations. Text is stored as a string within the text editor class, and operations such as insertion and deletion of text are performed efficiently by leveraging the properties of strings, such as immutability and indexing.

- **Error Handling with Exceptions**: The project includes error handling mechanisms to ensure the robustness of the application. For example, input validation is performed to prevent the user from attempting to delete a negative number of characters. In case of such an invalid input, a ValueError exception is raised, and appropriate error messages are displayed to the user. This demonstrates proficiency in error handling and ensuring the reliability of the program.

- **Memory Management and Efficiency**: The text editor ensures efficient memory usage by managing two separate stacks (`edit_history` and `redo_history`) to store the edit history. By effectively managing memory resources and avoiding memory leaks, the text editor demonstrates proficiency in memory management, which is crucial for building efficient software systems.

## Usage

To use the text editor, simply run the `text_editor.py` script:

```sh
python text_editor.py
```

Follow the on-screen prompts to perform text editing operations, including inserting text, deleting text, undoing, redoing, and exiting the editor.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This project was developed by [Your Name]. Feel free to reach out with any questions or feedback!
