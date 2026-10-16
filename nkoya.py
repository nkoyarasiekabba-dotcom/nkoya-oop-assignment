# student_results.py
# OOP1 Individual Assignment - Real-World Solution under DPG Standards
# Domain: Education - Student Results System
# DPG: Open-source, privacy-respecting (no real names), modular, reusable

class Student:
    """Represents a student with minimal, non-sensitive data."""
    school_name = "Limkokwing University"  # class attribute

    def __init__(self, student_id, age, course, score):
        self.student_id = student_id   # use fake ID, not real name
        self.age = age
        self.course = course
        self.score = score

    def display_info(self):
        """Instance method: show student record."""
        return f"ID: {self.student_id} | Age: {self.age} | Course: {self.course} | Score: {self.score}"

    def update_score(self, new_score):
        """Instance method: update score."""
        self.score = new_score

    @classmethod
    def set_school_name(cls, name):
        """Class method: change school name for all students."""
        cls.school_name = name

    @staticmethod
    def is_passing(score):
        """Static method: check if score is a pass (>= 50)."""
        return score >= 50


class ResultsManager:
    """Manages a list of Student objects."""

    def __init__(self):
        self.students = []  # list data structure

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        if not self.students:
            print("No records yet.")
        for s in self.students:
            print(s.display_info())

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None


# --- Main program ---
if __name__ == "__main__":
    manager = ResultsManager()

    # Create sample students (fake IDs, no real names for privacy)
    s1 = Student("STU001", 20, "Computer Science", 78)
    s2 = Student("STU002", 22, "Business", 45)
    s3 = Student("STU003", 19, "Design", 88)

    # Add to list
    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)

    # Display all
    print("=== All Student Records ===")
    manager.display_all()

    # Update a score
    s2.update_score(55)
    print("\nAfter updating STU002 score:")
    print(s2.display_info())

    # Use static method
    print("\nIs STU001 passing?", Student.is_passing(s1.score))
    print("Is STU002 passing?", Student.is_passing(s2.score))

    # Use class method
    Student.set_school_name("LUCT Freetown")
    print("\nSchool name changed to:", Student.school_name)

    # Simple user input to add a record
    print("\n=== Add a new student ===")
    sid = input("Enter student ID: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    score = float(input("Enter score: "))
    new_student = Student(sid, age, course, score)
    manager.add_student(new_student)
    print("\nUpdated list:")
    manager.display_all()