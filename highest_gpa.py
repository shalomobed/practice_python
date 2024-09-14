# Shalom Obed. This program is to find the student with the highest GPA in a course.
'''
A program that allows a user to add multiple students to the course until a stop word has been entered.
After the stop word, your program should print out the number of students enrolled in the course
and the first, last, and gpa of the student with the highest GPA.
'''
# Define the Student Class
class Student:
    # Initialize the student with first name, last name and GPA.
    def __init__(self, fname, lname, gpa):
        self.fname = fname
        self.lname = lname
        self.gpa = float(gpa)  # Store the GPA as a float

    # Define the get_gpa() method to return the GPA
    def get_gpa(self):
        return self.gpa

    # Define the get_first() method to return the first name
    def get_first(self):
        return self.fname

    # Define the get_last() method to return the last name
    def get_last(self):
        return self.lname


# Define the Course class
class Course:
    # Initialize the course with an empty roster
    def __init__(self):
        self.roster = []
        self.max_gpa = 0
        self.top_student = None

    # Define the add_student() method to add a student to the roster
    def add_student(self, student):
        self.roster.append(student)
        if student.get_gpa() > self.max_gpa:
            self.max_gpa = student.get_gpa()
            self.top_student = student

    # Define the course_size() method to return the size of the roster
    def course_size(self):
        return len(self.roster)

    # Define the find_student_highest_gpa() method to return the student with the highest GPA
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        return self.top_student


# Define the EmptyRosterError class
class EmptyRosterError(Exception):
    def __init__(self, message):
        self.message = message


# Define the main() function
def main():
    # Create a new course
    course = Course()

    # Print the welcome message
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1\nPlease Add Students to the Course: (quit or q to exit).")

    # Loop until the user quits
    while True:
        try:
            # Get the first name
            fname = input("Enter First Name: ")

            # Check if the user wants to quit
            if fname.lower() == "quit" or fname.lower == "q":
                break
            # Get the last name
            lname = input("Enter Last Name: ")

            # Get the GPA
            gpa = float(input("Enter GPA: "))
            # Create a new student with the given first name, last name and GPA
            student = Student(fname, lname, gpa)

            # Add the student to the course
            course.add_student(student)

        # Handle the ValueError exception raised when the user enters a non-numeric GPA
        except ValueError:
            print("Error: Enter a Numeric GPA")
            continue
    # Print the course size
    print(f"Course Size: {course.course_size()} students")

    # Find the student with the highest GPA
    try:
        top_student = course.find_student_highest_gpa()
        print(f"Top Student: {top_student.get_first()} {top_student.get_last()} (GPA: {top_student.get_gpa()})")
    # Handle the EmptyRosterError exception
    except EmptyRosterError as e:
        print(e.message)


# Call the main function
if __name__ == "__main__":
    main()
