# nkoya-oop-assignment
# Student Results System - OOP1 Individual Assignment
**Domain:** Education | **DPG Standard:** Privacy-respecting, Open-source, Reusable

> No real names used. Only fake IDs (STU001) to protect privacy.

## How To Run - Straight To The Work

1. Run the file:
   python student_results.py

2. What happens automatically:
      - Creates 3 sample students (STU001, STU002, STU003)
      - Adds them to ResultsManager list
      - Displays all records
      - Updates STU002 score from 45 to 55
      - Checks who is passing using static method
      - Changes school name using class method
      - Asks YOU to add a new student

3. For user input part, just type:
   ID: STU004
   Age: 21
   Course: IT
   Score: 75

## Code Meets All OOP Requirements

**TASK 1 & 3: Classes and Methods**
- Class `Student`
    - Attributes: student_id, age, course, score
    - Class Attribute: school_name = "Limkokwing University"
    - Instance Methods: display_info(), update_score()
    - Class Method: set_school_name() -> changes name for ALL students
    - Static Method: is_passing() -> checks if score >= 50

- Class `ResultsManager`
    - Attribute: students = [] (List data structure)
    - Methods: add_student(), display_all(), find_student()

**TASK 2: Data Structure**
- List: self.students holds Student objects
- Loops through list to display and find

**TASK 4: CRUD Operations**
- Create: add_student()
- Read: display_all(), find_student()
- Update: update_score(), set_school_name()
- No real names for DPG privacy

## Files
- student_results.py - Main code
- README.md - This file

## Requirement
Python 3.6+ only, no extra library needed
