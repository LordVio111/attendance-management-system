"""
Student Model Class
Represents a single student with attendance tracking
"""

class Student:
    """Class to represent a student"""
    
    def __init__(self, student_id, name, email=None):
        """
        Initialize a student object
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Name of the student
            email (str): Email address of the student (optional)
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.attendance = {}  # Dictionary to store attendance: {date: status}
        
    def mark_present(self, date):
        """Mark student as present on a specific date"""
        self.attendance[date] = 'Present'
        
    def mark_absent(self, date):
        """Mark student as absent on a specific date"""
        self.attendance[date] = 'Absent'
        
    def mark_leave(self, date):
        """Mark student as on leave on a specific date"""
        self.attendance[date] = 'Leave'
        
    def get_attendance_percentage(self):
        """
        Calculate attendance percentage
        
        Returns:
            float: Attendance percentage (0-100)
        """
        if not self.attendance:
            return 0.0
        
        present_days = sum(1 for status in self.attendance.values() if status == 'Present')
        total_days = len(self.attendance)
        
        return (present_days / total_days) * 100 if total_days > 0 else 0.0
    
    def get_score(self, max_score=100):
        """
        Calculate score based on attendance percentage
        
        Args:
            max_score (int): Maximum score possible (default: 100)
            
        Returns:
            float: Score calculated from attendance percentage
        """
        percentage = self.get_attendance_percentage()
        return (percentage / 100) * max_score
    
    def get_total_days(self):
        """Get total days tracked"""
        return len(self.attendance)
    
    def get_present_days(self):
        """Get total days marked as present"""
        return sum(1 for status in self.attendance.values() if status == 'Present')
    
    def get_absent_days(self):
        """Get total days marked as absent"""
        return sum(1 for status in self.attendance.values() if status == 'Absent')
    
    def get_leave_days(self):
        """Get total days marked as leave"""
        return sum(1 for status in self.attendance.values() if status == 'Leave')
    
    def to_dict(self):
        """Convert student object to dictionary for JSON storage"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'attendance': self.attendance
        }
    
    @staticmethod
    def from_dict(data):
        """Create student object from dictionary"""
        student = Student(data['student_id'], data['name'], data.get('email'))
        student.attendance = data.get('attendance', {})
        return student
    
    def __str__(self):
        """String representation of student"""
        return f"ID: {self.student_id} | Name: {self.name} | Email: {self.email}"
