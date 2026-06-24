"""
Attendance Management System
Core logic for managing attendance operations
"""

import json
import os
from datetime import datetime
from student import Student

class AttendanceSystem:
    """Main class to manage attendance system operations"""
    
    def __init__(self, data_file='attendance_data.json'):
        """
        Initialize the attendance system
        
        Args:
            data_file (str): Name of the JSON file to store data
        """
        self.data_file = data_file
        self.students = {}
        self.load_data()
    
    def load_data(self):
        """Load student data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for student_dict in data:
                        student = Student.from_dict(student_dict)
                        self.students[student.student_id] = student
                print(f"✓ Loaded {len(self.students)} students from file")
            except Exception as e:
                print(f"✗ Error loading data: {e}")
        else:
            print("No existing data file found. Starting fresh.")
    
    def save_data(self):
        """Save student data to JSON file"""
        try:
            data = [student.to_dict() for student in self.students.values()]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=4)
            print("✓ Data saved successfully")
        except Exception as e:
            print(f"✗ Error saving data: {e}")
    
    def add_student(self):
        """Add a new student to the system"""
        print("\n--- ADD NEW STUDENT ---")
        
        student_id = input("Enter Student ID: ").strip()
        
        if student_id in self.students:
            print("✗ Student ID already exists!")
            return
        
        name = input("Enter Student Name: ").strip()
        email = input("Enter Email (optional): ").strip() or None
        
        student = Student(student_id, name, email)
        self.students[student_id] = student
        self.save_data()
        print(f"✓ Student '{name}' added successfully!")
    
    def view_students(self):
        """Display all students in the system"""
        print("\n--- ALL STUDENTS ---")
        
        if not self.students:
            print("No students found in the system.")
            return
        
        print(f"\n{'ID':<10} {'Name':<25} {'Email':<30} {'Attendance %':<15}")
        print("-" * 80)
        
        for student in self.students.values():
            percentage = f"{student.get_attendance_percentage():.2f}%"
            print(f"{student.student_id:<10} {student.name:<25} {str(student.email or 'N/A'):<30} {percentage:<15}")
    
    def mark_attendance(self):
        """Mark attendance for students on a specific date"""
        print("\n--- MARK ATTENDANCE ---")
        
        if not self.students:
            print("No students found. Please add students first.")
            return
        
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")
        
        # Validate date format
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("✗ Invalid date format! Use YYYY-MM-DD")
            return
        
        print(f"\nMarking attendance for {date_str}")
        print("-" * 50)
        
        for student_id, student in self.students.items():
            print(f"\n{student.name} ({student_id}):")
            print("1. Present  2. Absent  3. Leave")
            
            choice = input("Select (1/2/3): ").strip()
            
            if choice == '1':
                student.mark_present(date_str)
                print("✓ Marked as Present")
            elif choice == '2':
                student.mark_absent(date_str)
                print("✓ Marked as Absent")
            elif choice == '3':
                student.mark_leave(date_str)
                print("✓ Marked as Leave")
            else:
                print("✗ Invalid choice!")
        
        self.save_data()
    
    def view_attendance_record(self):
        """View attendance record for a specific student"""
        print("\n--- VIEW ATTENDANCE RECORD ---")
        
        if not self.students:
            print("No students found.")
            return
        
        student_id = input("Enter Student ID: ").strip()
        
        if student_id not in self.students:
            print("✗ Student not found!")
            return
        
        student = self.students[student_id]
        print(f"\nAttendance Record for: {student.name}")
        print("=" * 50)
        
        if not student.attendance:
            print("No attendance records found.")
            return
        
        print(f"{'Date':<15} {'Status':<15}")
        print("-" * 50)
        
        for date in sorted(student.attendance.keys()):
            status = student.attendance[date]
            print(f"{date:<15} {status:<15}")
    
    def calculate_score(self):
        """Calculate and display attendance score for a student"""
        print("\n--- CALCULATE SCORE ---")
        
        if not self.students:
            print("No students found.")
            return
        
        student_id = input("Enter Student ID: ").strip()
        
        if student_id not in self.students:
            print("✗ Student not found!")
            return
        
        max_score = input("Enter maximum score (default: 100): ").strip()
        max_score = int(max_score) if max_score.isdigit() else 100
        
        student = self.students[student_id]
        percentage = student.get_attendance_percentage()
        score = student.get_score(max_score)
        
        print(f"\n--- SCORE DETAILS ---")
        print(f"Student Name: {student.name}")
        print(f"Student ID: {student_id}")
        print(f"Attendance Percentage: {percentage:.2f}%")
        print(f"Score: {score:.2f}/{max_score}")
        
        # Grade assignment
        if percentage >= 90:
            grade = 'A'
        elif percentage >= 80:
            grade = 'B'
        elif percentage >= 70:
            grade = 'C'
        elif percentage >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Grade: {grade}")
    
    def generate_report(self):
        """Generate attendance report for all students"""
        print("\n--- ATTENDANCE REPORT ---")
        
        if not self.students:
            print("No students found.")
            return
        
        print(f"\n{'ID':<10} {'Name':<25} {'Present':<10} {'Absent':<10} {'Leave':<10} {'Percentage':<12} {'Score':<10}")
        print("-" * 97)
        
        for student in self.students.values():
            present = student.get_present_days()
            absent = student.get_absent_days()
            leave = student.get_leave_days()
            percentage = student.get_attendance_percentage()
            score = student.get_score()
            
            print(f"{student.student_id:<10} {student.name:<25} {present:<10} {absent:<10} {leave:<10} {percentage:>10.2f}% {score:>9.2f}")
    
    def view_statistics(self):
        """View overall statistics of the attendance system"""
        print("\n--- SYSTEM STATISTICS ---")
        
        if not self.students:
            print("No students found.")
            return
        
        total_students = len(self.students)
        
        # Calculate averages
        total_percentage = sum(s.get_attendance_percentage() for s in self.students.values())
        avg_percentage = total_percentage / total_students if total_students > 0 else 0
        
        total_score = sum(s.get_score() for s in self.students.values())
        avg_score = total_score / total_students if total_students > 0 else 0
        
        # Find highest and lowest attendance
        highest_student = max(self.students.values(), key=lambda s: s.get_attendance_percentage())
        lowest_student = min(self.students.values(), key=lambda s: s.get_attendance_percentage())
        
        print(f"\nTotal Students: {total_students}")
        print(f"Average Attendance %: {avg_percentage:.2f}%")
        print(f"Average Score: {avg_score:.2f}/100")
        print(f"\nHighest Attendance: {highest_student.name} ({highest_student.get_attendance_percentage():.2f}%)")
        print(f"Lowest Attendance: {lowest_student.name} ({lowest_student.get_attendance_percentage():.2f}%)")
