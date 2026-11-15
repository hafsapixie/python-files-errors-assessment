Imagine you are developing two small management tools for a training institute.
The institute needs a simple **Expense Tracking System** to record daily operational expenses, such as stationery, internet bills, refreshments, and transport. It also needs an **Attendance Management System** to organize student attendance records, remove duplicate entries, and generate a clean attendance list.

Your responsibility is to build both programs using Python's file handling, exception handling, sets, and comprehensions.

## Task 1: Institute Expense Tracker (`expense_tracker.py`)

Develop a program that helps institute administration maintain daily expense records.

Requirements:
- Save expenses in `expenses.csv` with the columns `date,item,category,amount`.
- When the program starts, load previously saved expenses. If the file does not exist, catch `FileNotFoundError` and start with an empty expense list.
- Display a menu with the following options:
1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
- Allow users to enter the expense date, item name, category, and amount.
- Catch `ValueError` if the entered amount is not a valid number and ask the user to enter it again.
- Use a **set** to display all unique expense categories.
- Ensure newly added expenses are saved to the CSV file so they remain available when the program runs again.

## Task 2: Student Attendance Cleaner (`attendance_cleaner.py`)

The institute maintains attendance records in a text file. However, the file contains repeated student names, inconsistent capitalization, and unnecessary spaces.

Develop a program to clean and organize these records.
**Requirements:**
- Read student names from `attendance.txt`, where each line contains one name.
- Clean names using `strip()` and `title()` with a **list comprehension**.
- Use a **set** to identify unique students and calculate the total number of unique students.
- Sort the cleaned student names alphabetically.
- Save the final cleaned and sorted list to `attendance_clean.csv`.
- Display the original number of records, unique student count, and cleaned attendance list.

## **GitHub Repository Structure**
Create a public GitHub repository with the following structure:

python-files-errors-assessment/
│
├── expense_tracker.py
├── attendance_cleaner.py
├── attendance.txt
└── README.md

## **README.md Requirements**

Your README file must include:
- Overview of both applications and their purpose.
- Instructions on how to run each Python program.
- Explanation of the errors handled and why they are handled.
- Explanation of how sets and list comprehensions are used.
- A sample run demonstrating that expense data is saved and loaded again successfully.

## **Submission Instructions**
1. Complete both Python programs individually.
2. Test both applications with different inputs, including invalid amounts and duplicate attendance names.
3. Push all required files to your GitHub repository.
4. Submit your public GitHub repository link on the LMS.