# Attendance Management System

A comprehensive Python application to manage student attendance, calculate scores, and generate reports. 
Now available as both a **Command-Line Interface (CLI)** and a **Web Application (Streamlit)**.

## 🌟 Features

✅ **Add Students** - Register new students with ID, name, and email
✅ **Mark Attendance** - Record attendance for students (Present/Absent/Leave)
✅ **View Records** - Check attendance history for individual students
✅ **Calculate Scores** - Compute attendance percentage and scores with grades
✅ **Generate Reports** - Create comprehensive attendance reports
✅ **Statistics** - View system-wide attendance statistics
✅ **Data Persistence** - Automatically saves data to JSON file
✅ **Beautiful Web Interface** - Interactive Streamlit dashboard
✅ **Analytics** - Visual charts and graphs of attendance data
✅ **Export Reports** - Download attendance reports as CSV

## 📋 Installation

### 1. Clone the repository
```bash
git clone https://github.com/LordVio111/attendance-management-system.git
cd attendance-management-system
```

### 2. Create a virtual environment (Optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Ensure Python 3.6+ is installed
```bash
python --version
```

## 🚀 Usage

### Option A: Web Application (Recommended) 🌐

Run the Streamlit web app:
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

**Features in Web App:**
- 🏠 Dashboard with key metrics
- ➕ Add students with form validation
- 📋 View all students in a table
- ✅ Mark attendance with interactive buttons
- 📈 Generate detailed attendance reports
- 📊 View analytics with charts and graphs
- ⚙️ Settings and data management
- 💾 Download reports as CSV

### Option B: Command-Line Interface (CLI) 💻

Run the CLI application:
```bash
python main.py
```

**Menu Options:**
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

## 📖 How to Use (Web App)

### Step 1: Add Students
1. Click **"➕ Add Student"** in the navigation menu
2. Enter Student ID (e.g., `S001`)
3. Enter Student Name (e.g., `John Doe`)
4. Enter Email (optional)
5. Click **"Add Student"**

### Step 2: Mark Attendance
1. Click **"✅ Mark Attendance"** in the navigation menu
2. Select the date (defaults to today)
3. For each student:
   - Click **"✅ Present"**, **"❌ Absent"**, or **"🏥 Leave"**
   - Or use the manual entry form below
4. Data automatically saves

### Step 3: View Reports & Analytics
1. **Reports** - View detailed attendance reports with scores and grades
2. **Analytics** - See visual charts of attendance distribution
3. Download reports as CSV for further analysis

### Step 4: Manage Students
1. **View Students** - See all students and their attendance percentage
2. **Delete Students** - Remove students from the system
3. **Settings** - Configure grading system and manage data

## 📁 File Structure

```
attendance-management-system/
├── main.py                    # CLI entry point
├── app.py                     # Streamlit web app
├── attendance_system.py        # Core system logic
├── student.py                 # Student model class
├── requirements.txt           # Python dependencies
├── attendance_data.json        # Data storage (auto-created)
├── .gitignore                 # Git ignore rules
└── README.md                  # Documentation
```

## 💾 Data Storage

All data is stored in `attendance_data.json` in the following format:

```json
[
    {
        "student_id": "S001",
        "name": "John Doe",
        "email": "john@example.com",
        "attendance": {
            "2024-06-24": "Present",
            "2024-06-25": "Absent",
            "2024-06-26": "Leave"
        }
    }
]
```

## 🎯 Scoring System

- **Attendance Percentage** = (Days Present / Total Days) × 100
- **Score** = (Attendance % / 100) × Max Score (default: 100)
- **Grade Assignment**:
  - **A**: 90-100%
  - **B**: 80-89%
  - **C**: 70-79%
  - **D**: 60-69%
  - **F**: Below 60%

## 🔧 Customization

### Web App (Streamlit)
1. Change colors and styling in the CSS section of `app.py`
2. Modify page layout and add new pages
3. Customize metrics and charts
4. Add new features in separate sections

### CLI Application
1. Modify grade thresholds in `attendance_system.py`
2. Add new methods to `Student` class for custom calculations
3. Add new menu options to `main.py`
4. Extend `AttendanceSystem` class with new functionality

### Change Maximum Score
In the web app: Enter custom score when viewing reports
In CLI: Enter custom score when calculating attendance score

### Modify Grade Thresholds
Edit the grade assignment logic in `attendance_system.py` or `app.py`:
```python
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
# ... modify as needed
```

## 🌐 Deploy to Cloud

### Deploy Streamlit App for Free

#### Option 1: Streamlit Cloud (Easiest)
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your GitHub repository and `app.py`
5. Deploy!

#### Option 2: Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run app.py
   ```
2. Deploy to Heroku

#### Option 3: PythonAnywhere
1. Upload files to PythonAnywhere
2. Create a web app using Streamlit
3. Configure and deploy

## 📊 Example Workflow

### Web App Example:
```
1. Click "➕ Add Student" → Add 3 students (S001, S002, S003)
2. Click "✅ Mark Attendance" → Mark attendance for 2024-06-24
3. Click "✅ Mark Attendance" → Mark attendance for 2024-06-25
4. Click "📈 Reports" → View attendance reports with scores
5. Click "📊 Analytics" → View charts and statistics
6. Click "📥 Download Report" → Get CSV file
```

### CLI Example:
```
1. Select option 1 → Add 3 students
2. Select option 3 → Mark attendance for 2 dates
3. Select option 4 → View individual records
4. Select option 5 → Calculate scores
5. Select option 6 → Generate report
6. Select option 7 → View statistics
```

## 📋 Requirements

- Python 3.6+
- Streamlit (for web app)
- Pandas (for data handling)
- No database needed (uses JSON)

## 🐛 Troubleshooting

### Streamlit not starting?
```bash
pip install --upgrade streamlit
streamlit run app.py
```

### Data not saving?
- Make sure the application has write permissions in the directory
- Check that `attendance_data.json` is not corrupted

### Port already in use?
```bash
streamlit run app.py --server.port 8502
```

## 📝 License

Free to use and modify for personal and educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📞 Support

For issues or suggestions, please open an issue on the GitHub repository.

---

**Happy Tracking!** 📚✅

**Version**: 1.0 (With Streamlit Web App)
**Last Updated**: 2024-06-24
