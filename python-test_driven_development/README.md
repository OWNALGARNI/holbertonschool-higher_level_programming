# Python - Test Driven Development

This project focuses on practicing Test Driven Development (TDD) in Python.  
Each task requires writing documentation and tests **before** writing the actual code.  
The goal is to understand how Python's `doctest` and `unittest` modules can be used  
to validate code correctness and catch edge cases.

---

Project Tasks

0. Integers addition
Write a function `add_integer(a, b=98)` that:
- Adds two integers
- Casts floats to integers
- Raises `TypeError` when inputs are not numbers
- Includes doctests in the function documentation

---

1. Divide a matrix
Write a function `matrix_divided(matrix, div)` that:
- Validates the matrix structure
- Divides all elements by a number
- Raises exceptions for invalid input
- Returns a new matrix
- Includes doctests

---

2. Say my name
Write a function `say_my_name(first_name, last_name="")` that:
- Validates both names as strings
- Prints the formatted full name
- Includes doctests

---

3. Print square
Write a function `print_square(size)` that:
- Prints a square made of `#`
- Validates the input type and value
- Includes doctests

---

4. Text indentation
Write a function `text_indentation(text)` that:
- Adds a newline after `.`, `?`, and `:`
- Validates input type
- Includes doctests

---

5. Max integer - Unittest
Write unit tests for the function `max_integer(list=[])` using Python's `unittest`:
- Test empty list
- Test list with one element
- Test positive and negative integers
- Test edge cases


Test Files
- All tests stored inside `tests/` directory
- Doctest files use `.txt` extension
- Run all tests using:

