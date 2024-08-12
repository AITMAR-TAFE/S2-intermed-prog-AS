# Overview

> Tic-Tac-Toe Game Refactoring

**NOTE:** You may be asked by your lecturer to submit this assessment via GitHub classrooms. Please check closer to submission date.

## Objective

Refactor a given monolithic tic-tac-toe game, such that the code:

1. Is modular, consisting of at least two files that logically group related functions.
2. Implements an appropriate Python project folder structure.
3. Includes at least one test case.
4. Employs a 2D data structure.

In the process, you must use **at least four functions, two classes, two files, and one import statement of your modules (does not include imports used in the test case or the unittest class)**.

## Instructions

### Step 1: Review the Existing Code

~~Firstly, analyze the given tic-tac-toe game code. Understand the flow and functionality before proceeding with the refactoring.~~

Martina: After looking over the code, I can see several areas for improvement. The code is working, but it needs to be structured and organised properly.

### Step 2: Identify Components to Refactor

~~Identify the parts of the code that can be improved. Determine which parts of the code can be grouped logically into separate modules.~~

Martina: The code that prints the board could be in a separate class and stored in 2D list. Game logic that updates board after player moves could also be separated. Winning and ties could be a methods of game logic. User input code could also be moved to separate method.

### Step 3: Modularizing the Code

Refactor the code to create at least two files. These files should contain logically grouped functions and classes. Ensure the file names are appropriate for the division you have chosen.

### Step 4: Create a Modern Python Folder Structure

The refactored code should adhere to the following modern Python folder structure:

```bash
tic_tac_toe/
|--- src/
|    |--- __init__.py
|    |--- module1.py
|    |--- module2.py
|--- tests/
|    |--- __init__.py
|    |--- test_tic_tac_toe.py
|--- setup.py
```

**Note**:

- `__init__.py` files are used to indicate that a directory should be treated as a Python package. This allows the files within to be imported as a module in the test scripts or other python files.
- `setup.py` is a Python file used to specify what modules and dependencies must be installed. I will provide this file, along with instructions on how to install your modules using this file.
- You must give your Python files appropriate names. **Do not use module1, 2, etc.**
- make sure to complete the **project metadata** section in setup.py

### Step 5: Create a Test Case

Develop at least one test case for your refactored code. The test case should reside in the 'tests' directory. This test should test game play and not set up i.e. does not just check for existence of a blank board but check for a diagonal win.

### Step 6: Implement 2D Data Structure

Refactor the code such that it employs a 2D data structure for the tic-tac-toe game board.

### Step 7: Written Report

Once you have completed your refactoring, write a brief report addressing the following:

1. Justification for your refactoring decisions.

Martina:Refactoring is important because we need to ensure that it's easy to read, maintainable, and can be tested properly. Each class has it's own responsibility - Board is used for creating and displaying the game board while Game_logic is used to store methods for checking wins and user interactions(inputs).

2. The challenges you would have faced maintaining and testing the original monolithic code.

Martina: With the original code, it would have been hard to change some methods or logic, as that would often lead to excessive change in code in overall. It would also be difficult to test and isolate code. 

3. How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how this implementation would be easier to handle than in the original code.

Martina: I would improve creating the board in Board class to accept a row, col size. Additionally I would have to change check_for_win method to accept different board sizes to check for wins. That would accommodate different sizes of boards, making it easier to adjust by the need.

4. Make sure to add this report to your submission

### Step 8: Short Answer (Knowledge Questions)

Provide brief answers to the knowledge-question worksheet.

1. Briefly explain: what is modular programming

Martina : Is a way of coding that separates program into more manageable modules. All modules are encapsulate specific features to their own and have different functionalities.

2. How can you import only a specific function or class from a module in Python? What is the syntax for this?

Martina : To import a class, I would use from board import Board, and then I will create an instance of the board class Board(). For importing function I would use from board import display_board and then call the function display_board()

3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.

Martina : When you pass a variable to a function in Python, you are passing a reference to the object that the variable refers to, not the actual object itself. This means that the function receives a reference to the same object, so if the function modifies the object (for example, a list or dictionary), the changes will be reflected outside the function. However, if the object is immutable (such as an integer or string), any modifications will result in the creation of a new object, leaving the original object unchanged.

4. Given the following Python code, what will be the output and why?

Martina : When we call the method modify_list, it will modify items list by appending the string "new" to it. Because it references to same object it now becomes ["original","new"]. The new list inside the method does not affect original list as it changes local reference to a new list object but original stays the same. 

   ```python
   def modify_list(list_):
       list_.append("new")
       list_ = ["completely", "new"]

   items = ["original"]
   modify_list(items)
   print(items)
   ```

5. In Python even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.

Martina : Because when mutable objects(lists and dictionaries) are modified with functions, the changes are made outside the functions because of pass by object reference system in Python. Even when variables are local, they still refer to the same mutable object, and this means that modifications that are done inside function will last after the function ends.

6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?
Martina : Improved Code Readability and Maintenance, Better Re-usability and Testing.
This will help developers to quickly understand, find and change needed parts of the code without going through a large, complicated and unorganised code, therefore saving time. 
This process will speed up development, because debugging is easier, you can test each isolated module before implementing and also reduces code duplication. 


### Submission

Please submit the refactored code, your test case, and the written report.

### Evaluation Criteria

- Your refactoring will be evaluated on the clarity and modularity of your code, as well as the thoughtful reasoning behind your design decisions.
- Your test case should be robust and cover key aspects of the tic-tac-toe game functionality.
- The written report should accurately reflect your understanding of code refactoring, testing, and the flexibility of your new implementation.
