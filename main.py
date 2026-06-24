"""
Attendance Management System
Main entry point for the application
"""

from attendance_system import AttendanceSystem

def main():
    """Main function to run the attendance management system"""
    system = AttendanceSystem()
    
    while True:
        print("\n" + "="*50)
        print("   ATTENDANCE MANAGEMENT SYSTEM")
        print("="*50)
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Mark Attendance")
        print("4. View Attendance Record")
        print("5. Calculate Attendance Score")
        print("6. Generate Report")
        print("7. View Statistics")
        print("8. Exit")
        print("-"*50)
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            system.mark_attendance()
        elif choice == '4':
            system.view_attendance_record()
        elif choice == '5':
            system.calculate_score()
        elif choice == '6':
            system.generate_report()
        elif choice == '7':
            system.view_statistics()
        elif choice == '8':
            print("\nThank you for using Attendance Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
