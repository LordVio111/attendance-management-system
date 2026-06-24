# Attendance Management System

A simple, easy-to-modify Python application to manage student attendance, calculate scores, and generate reports.

## Features

✅ **Add Students** - Register new students with ID, name, and email
✅ **Mark Attendance** - Record attendance for students (Present/Absent/Leave)
✅ **View Records** - Check attendance history for individual students
✅ **Calculate Scores** - Compute attendance percentage and scores
✅ **Generate Reports** - Create comprehensive attendance reports
✅ **Statistics** - View system-wide attendance statistics
✅ **Data Persistence** - Automatically saves data to JSON file

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LordVio111/attendance-management-system.git
   cd attendance-management-system
   ```

2. **Ensure Python 3.x is installed**
   ```bash
   python --version
   ```

3. **No additional dependencies required!** (Uses only Python standard library)

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

```
1. Add Student           - Register a new student
2. View All Students     - Display all registered students
3. Mark Attendance       - Record attendance for all students
4. View Attendance Record - Check specific student's attendance
5. Calculate Score       - Get attendance score for a student
6. Generate Report       - View comprehensive attendance report
7. View Statistics       - See system-wide statistics
8. Exit                  - Quit the application
```

## How to Use

### Step 1: Add Students
- Select option `1`
- Enter Student ID (e.g., `S001`)
- Enter Student Name (e.g., `John Doe`)
- Enter Email (optional)

### Step 2: Mark Attendance
- Select option `3`
- Enter date (YYYY-MM-DD) or press Enter for today
- For each student, select:
  - `1` for Present
  - `2` for Absent
  - `3` for Leave

### Step 3: View Records & Reports
- Use options `4`, `5`, `6`, `7` to view various reports

## Example Workflow

```
1. Add 3 students: S001, S002, S003
2. Mark attendance for 2024-06-24
3. Mark attendance for 2024-06-25
4. View attendance record for S001
5. Calculate score for S001
6. Generate report for all students
7. View statistics
```

## File Structure

```
attendance-management-system/
├── main.py                    # Entry point
├── attendance_system.py        # Core system logic
├── student.py                 # Student model class
├── attendance_data.json        # Data storage (auto-created)
└── README.md                  # Documentation
```

## Data Storage

All data is stored in `attendance_data.json` in the following format:

```json
[
    {
        "student_id": "S001",
        "name": "John Doe",
        "email": "john@example.com",
        "attendance": {
            "2024-06-24": "Present",
            "2024-06-25": "Absent"
        }
    }
]
```

## Scoring System

- **Attendance Percentage** = (Days Present / Total Days) × 100
- **Score** = (Attendance % / 100) × Max Score
- **Grade Assignment**:
  - A: 90-100%
  - B: 80-89%
  - C: 70-79%
  - D: 60-69%
  - F: Below 60%

## Customization

### Change Maximum Score
When calculating scores (option 5), enter a custom maximum score instead of the default 100.

### Modify Grade Thresholds
Edit the grade assignment logic in `attendance_system.py`:
```python
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
# ... modify as needed
```

### Add New Features
The modular structure makes it easy to add features:
- Add new methods to `Student` class for custom calculations
- Add new menu options to `main.py`
- Extend `AttendanceSystem` class with new functionality

## Requirements

- Python 3.6+
- No external dependencies

## License

Free to use and modify

## Support

For issues or suggestions, please open an issue on the repository.

---

**Happy Tracking!** 📚✅
