"""
Student Enrollment and Grading Management System
Manages student records with enrollment and grade tracking
"""

import os

# Global list to store student records
students = []

def load_records():
    """Load student records from records.txt file"""
    global students
    students = []
    
    if not os.path.exists('records.txt'):
        print("No existing records file found. Starting fresh.")
        return
    
    try:
        with open('records.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 6:
                        student = {
                            'id': parts[0],
                            'name': parts[1],
                            'course': parts[2],
                            'quiz': float(parts[3]),
                            'exam': float(parts[4]),
                            'final': float(parts[5])
                        }
                        students.append(student)
        print(f"Loaded {len(students)} student record(s).")
    except Exception as e:
        print(f"Error loading records: {e}")

def save_records():
    """Save all student records to records.txt file"""
    try:
        with open('records.txt', 'w') as file:
            for student in students:
                line = f"{student['id']},{student['name']},{student['course']},{student['quiz']},{student['exam']},{student['final']}\n"
                file.write(line)
        print("Records saved successfully.")
    except Exception as e:
        print(f"Error saving records: {e}")

def compute_final_grade(quiz_score, exam_score):
    """Calculate final grade using the formula: (Quiz × 0.4) + (Exam × 0.6)"""
    return (quiz_score * 0.4) + (exam_score * 0.6)

def student_id_exists(student_id):
    """Check if a student ID already exists"""
    for student in students:
        if student['id'] == student_id:
            return True
    return False

def add_student_record():
    """Add a new student record"""
    print("\n=== Add Student Record ===")
    
    # Get Student ID
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return
    
    if student_id_exists(student_id):
        print("Error: Student ID already exists.")
        return
    
    # Get Full Name
    full_name = input("Enter Full Name: ").strip()
    if not full_name:
        print("Error: Name cannot be empty.")
        return
    
    # Get Course
    course = input("Enter Course: ").strip()
    if not course:
        print("Error: Course cannot be empty.")
        return
    
    # Get Quiz Score
    try:
        quiz_score = float(input("Enter Quiz Score (0-100): "))
        if quiz_score < 0 or quiz_score > 100:
            print("Error: Quiz score must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Quiz score must be a number.")
        return
    
    # Get Exam Score
    try:
        exam_score = float(input("Enter Exam Score (0-100): "))
        if exam_score < 0 or exam_score > 100:
            print("Error: Exam score must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Exam score must be a number.")
        return
    
    # Compute Final Grade
    final_grade = compute_final_grade(quiz_score, exam_score)
    
    # Create student record
    student = {
        'id': student_id,
        'name': full_name,
        'course': course,
        'quiz': quiz_score,
        'exam': exam_score,
        'final': final_grade
    }
    
    students.append(student)
    save_records()
    print(f"\nStudent record added successfully! Final Grade: {final_grade:.2f}")

def view_all_records():
    """Display all student records"""
    print("\n=== All Student Records ===")
    
    if not students:
        print("No records found.")
        return
    
    print(f"\n{'ID':<10} {'Name':<25} {'Course':<10} {'Quiz':<8} {'Exam':<8} {'Final':<8}")
    print("-" * 80)
    
    for student in students:
        print(f"{student['id']:<10} {student['name']:<25} {student['course']:<10} "
              f"{student['quiz']:<8.2f} {student['exam']:<8.2f} {student['final']:<8.2f}")
    
    print(f"\nTotal Records: {len(students)}")

def search_student_by_id():
    """Search for a student by their ID"""
    print("\n=== Search Student by ID ===")
    
    student_id = input("Enter Student ID to search: ").strip()
    
    for student in students:
        if student['id'] == student_id:
            print("\nStudent Found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Quiz Score: {student['quiz']:.2f}")
            print(f"Exam Score: {student['exam']:.2f}")
            print(f"Final Grade: {student['final']:.2f}")
            return
    
    print("Error: Student ID not found.")

def update_student_scores():
    """Update quiz and exam scores for a student"""
    print("\n=== Update Student Scores ===")
    
    student_id = input("Enter Student ID to update: ").strip()
    
    student_found = None
    for student in students:
        if student['id'] == student_id:
            student_found = student
            break
    
    if not student_found:
        print("Error: Student ID not found.")
        return
    
    print(f"\nCurrent Scores for {student_found['name']}:")
    print(f"Quiz Score: {student_found['quiz']:.2f}")
    print(f"Exam Score: {student_found['exam']:.2f}")
    print(f"Final Grade: {student_found['final']:.2f}")
    
    # Update Quiz Score
    try:
        quiz_score = float(input("\nEnter new Quiz Score (0-100): "))
        if quiz_score < 0 or quiz_score > 100:
            print("Error: Quiz score must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Quiz score must be a number.")
        return
    
    # Update Exam Score
    try:
        exam_score = float(input("Enter new Exam Score (0-100): "))
        if exam_score < 0 or exam_score > 100:
            print("Error: Exam score must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Exam score must be a number.")
        return
    
    # Update student record
    student_found['quiz'] = quiz_score
    student_found['exam'] = exam_score
    student_found['final'] = compute_final_grade(quiz_score, exam_score)
    
    save_records()
    print(f"\nScores updated successfully! New Final Grade: {student_found['final']:.2f}")

def compute_class_average():
    """Compute and display the class average of final grades"""
    print("\n=== Compute Class Average ===")
    
    if not students:
        print("No records found. Cannot compute average.")
        return
    
    total = sum(student['final'] for student in students)
    average = total / len(students)
    
    print(f"\nTotal Students: {len(students)}")
    print(f"Class Average (Final Grade): {average:.2f}")

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("Student Enrollment and Grading Management System")
    print("=" * 50)
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Search Student by ID")
    print("4. Update Student Scores")
    print("5. Compute Class Average")
    print("6. Exit")
    print("=" * 50)

def main():
    """Main program loop"""
    print("Welcome to Student Management System!")
    load_records()
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student_record()
        elif choice == '2':
            view_all_records()
        elif choice == '3':
            search_student_by_id()
        elif choice == '4':
            update_student_scores()
        elif choice == '5':
            compute_class_average()
        elif choice == '6':
            print("\nSaving all records...")
            save_records()
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
