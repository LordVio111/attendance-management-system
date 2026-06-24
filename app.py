"""
Attendance Management System - Streamlit Web App
Interactive web interface for managing student attendance
"""

import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime
from student import Student

# Page configuration
st.set_page_config(
    page_title="Attendance Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'students' not in st.session_state:
    st.session_state.students = {}
    load_data()

def load_data(data_file='attendance_data.json'):
    """Load student data from JSON file"""
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
                for student_dict in data:
                    student = Student.from_dict(student_dict)
                    st.session_state.students[student.student_id] = student
        except Exception as e:
            st.error(f"Error loading data: {e}")

def save_data(data_file='attendance_data.json'):
    """Save student data to JSON file"""
    try:
        data = [student.to_dict() for student in st.session_state.students.values()]
        with open(data_file, 'w') as f:
            json.dump(data, f, indent=4)
        st.success("✓ Data saved successfully!")
    except Exception as e:
        st.error(f"Error saving data: {e}")

# Sidebar Navigation
st.sidebar.markdown("## 📊 Navigation")
page = st.sidebar.radio(
    "Select a page:",
    ["🏠 Home", "➕ Add Student", "📋 View Students", "✅ Mark Attendance", 
     "📈 Reports", "📊 Analytics", "⚙️ Settings"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📁 Data Management")
if st.sidebar.button("💾 Save Data", use_container_width=True):
    save_data()

if st.sidebar.button("🔄 Reload Data", use_container_width=True):
    st.session_state.students = {}
    load_data()
    st.rerun()

# ============= HOME PAGE =============
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">📚 Attendance Management System</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Students", len(st.session_state.students))
    
    with col2:
        if st.session_state.students:
            avg_attendance = sum(s.get_attendance_percentage() for s in st.session_state.students.values()) / len(st.session_state.students)
            st.metric("Avg Attendance %", f"{avg_attendance:.2f}%")
        else:
            st.metric("Avg Attendance %", "0%")
    
    with col3:
        total_records = sum(len(s.attendance) for s in st.session_state.students.values())
        st.metric("Total Records", total_records)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Quick Features")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("➕ Add New Student", use_container_width=True):
            st.switch_page("pages/add_student.py")
    
    with col2:
        if st.button("✅ Mark Attendance", use_container_width=True):
            st.switch_page("pages/mark_attendance.py")
    
    with col3:
        if st.button("📈 View Reports", use_container_width=True):
            st.switch_page("pages/reports.py")
    
    with col4:
        if st.button("📊 View Analytics", use_container_width=True):
            st.switch_page("pages/analytics.py")
    
    st.markdown("---")
    st.markdown("""
    ### ℹ️ About This System
    
    This is a comprehensive Attendance Management System that helps you:
    - ✅ Register and manage students
    - ✅ Track daily attendance
    - ✅ Calculate attendance scores and grades
    - ✅ Generate detailed reports
    - ✅ View analytics and statistics
    
    **Get Started**: Use the navigation menu on the left to explore features!
    """)

# ============= ADD STUDENT PAGE =============
elif page == "➕ Add Student":
    st.markdown("## ➕ Add New Student")
    
    with st.form("add_student_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            student_id = st.text_input("Student ID (e.g., S001)")
        
        with col2:
            name = st.text_input("Student Name")
        
        email = st.text_input("Email Address (Optional)")
        
        submit = st.form_submit_button("Add Student", use_container_width=True)
        
        if submit:
            if not student_id or not name:
                st.error("❌ Please fill in Student ID and Name!")
            elif student_id in st.session_state.students:
                st.error("❌ Student ID already exists!")
            else:
                student = Student(student_id, name, email if email else None)
                st.session_state.students[student_id] = student
                save_data()
                st.success(f"✅ Student '{name}' added successfully!")
                st.balloons()

# ============= VIEW STUDENTS PAGE =============
elif page == "📋 View Students":
    st.markdown("## 📋 View All Students")
    
    if not st.session_state.students:
        st.info("No students found. Add a student first!")
    else:
        # Create dataframe
        data = []
        for student in st.session_state.students.values():
            data.append({
                'Student ID': student.student_id,
                'Name': student.name,
                'Email': student.email or 'N/A',
                'Total Days': student.get_total_days(),
                'Present': student.get_present_days(),
                'Absent': student.get_absent_days(),
                'Leave': student.get_leave_days(),
                'Attendance %': f"{student.get_attendance_percentage():.2f}%"
            })
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Delete student
        st.markdown("---")
        st.markdown("### 🗑️ Remove Student")
        col1, col2 = st.columns([3, 1])
        with col1:
            student_to_delete = st.selectbox("Select student to remove:", 
                                            list(st.session_state.students.keys()),
                                            key="delete_select")
        with col2:
            if st.button("Delete", use_container_width=True):
                del st.session_state.students[student_to_delete]
                save_data()
                st.success("Student removed!")
                st.rerun()

# ============= MARK ATTENDANCE PAGE =============
elif page == "✅ Mark Attendance":
    st.markdown("## ✅ Mark Attendance")
    
    if not st.session_state.students:
        st.warning("⚠️ No students found. Add students first!")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            attendance_date = st.date_input("Select Date", datetime.now())
        
        with col2:
            st.write(f"**Date:** {attendance_date.strftime('%Y-%m-%d')}")
        
        st.markdown("---")
        st.markdown("### Mark attendance for each student:")
        
        date_str = attendance_date.strftime("%Y-%m-%d")
        attendance_data = {}
        
        for student_id, student in st.session_state.students.items():
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            
            with col1:
                st.write(f"**{student.name}** ({student_id})")
            
            with col2:
                if st.button("✅ Present", key=f"present_{student_id}", use_container_width=True):
                    attendance_data[student_id] = 'Present'
            
            with col3:
                if st.button("❌ Absent", key=f"absent_{student_id}", use_container_width=True):
                    attendance_data[student_id] = 'Absent'
            
            with col4:
                if st.button("🏥 Leave", key=f"leave_{student_id}", use_container_width=True):
                    attendance_data[student_id] = 'Leave'
        
        st.markdown("---")
        
        # Manual entry form
        with st.expander("📝 Manual Entry (Alternative)"):
            st.markdown("### Or enter attendance manually:")
            
            with st.form("manual_attendance_form"):
                student_choices = list(st.session_state.students.keys())
                selected_student = st.selectbox("Select Student", student_choices)
                status = st.radio("Status", ["Present", "Absent", "Leave"], horizontal=True)
                
                if st.form_submit_button("Mark Attendance", use_container_width=True):
                    st.session_state.students[selected_student].attendance[date_str] = status
                    save_data()
                    st.success(f"✅ Marked {st.session_state.students[selected_student].name} as {status}!")

# ============= REPORTS PAGE =============
elif page == "📈 Reports":
    st.markdown("## 📈 Attendance Reports")
    
    if not st.session_state.students:
        st.warning("⚠️ No attendance data available!")
    else:
        # Generate comprehensive report
        data = []
        for student in st.session_state.students.values():
            percentage = student.get_attendance_percentage()
            score = student.get_score()
            
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
            
            data.append({
                'ID': student.student_id,
                'Name': student.name,
                'Present': student.get_present_days(),
                'Absent': student.get_absent_days(),
                'Leave': student.get_leave_days(),
                'Total': student.get_total_days(),
                'Attendance %': f"{percentage:.2f}",
                'Score': f"{score:.2f}",
                'Grade': grade
            })
        
        df = pd.DataFrame(data)
        
        # Display with formatting
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Report as CSV",
            data=csv,
            file_name=f"attendance_report_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
        
        # Individual student report
        st.markdown("---")
        st.markdown("### 👤 Individual Student Report")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            selected_student_id = st.selectbox("Select Student", 
                                              list(st.session_state.students.keys()),
                                              key="report_select")
        
        student = st.session_state.students[selected_student_id]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Present Days", student.get_present_days())
        with col2:
            st.metric("Absent Days", student.get_absent_days())
        with col3:
            st.metric("Leave Days", student.get_leave_days())
        with col4:
            st.metric("Attendance %", f"{student.get_attendance_percentage():.2f}%")
        
        if student.attendance:
            st.markdown("#### 📅 Detailed Attendance Records:")
            att_df = pd.DataFrame([
                {'Date': date, 'Status': status}
                for date, status in sorted(student.attendance.items())
            ])
            st.dataframe(att_df, use_container_width=True, hide_index=True)

# ============= ANALYTICS PAGE =============
elif page == "📊 Analytics":
    st.markdown("## 📊 System Analytics")
    
    if not st.session_state.students:
        st.warning("⚠️ No data available for analytics!")
    else:
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        total_students = len(st.session_state.students)
        avg_attendance = sum(s.get_attendance_percentage() for s in st.session_state.students.values()) / total_students
        avg_score = sum(s.get_score() for s in st.session_state.students.values()) / total_students
        highest_student = max(st.session_state.students.values(), key=lambda s: s.get_attendance_percentage())
        
        with col1:
            st.metric("Total Students", total_students)
        with col2:
            st.metric("Avg Attendance", f"{avg_attendance:.2f}%")
        with col3:
            st.metric("Avg Score", f"{avg_score:.2f}/100")
        with col4:
            st.metric("Highest Attendance", f"{highest_student.name} ({highest_student.get_attendance_percentage():.2f}%)")
        
        st.markdown("---")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Attendance Distribution")
            attendance_data = {s.name: s.get_attendance_percentage() for s in st.session_state.students.values()}
            st.bar_chart(attendance_data)
        
        with col2:
            st.markdown("### 📈 Student Scores")
            score_data = {s.name: s.get_score() for s in st.session_state.students.values()}
            st.line_chart(score_data)
        
        st.markdown("---")
        
        # Status breakdown
        st.markdown("### 📋 Attendance Status Breakdown")
        
        total_present = sum(s.get_present_days() for s in st.session_state.students.values())
        total_absent = sum(s.get_absent_days() for s in st.session_state.students.values())
        total_leave = sum(s.get_leave_days() for s in st.session_state.students.values())
        
        status_data = {
            'Present': total_present,
            'Absent': total_absent,
            'Leave': total_leave
        }
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Present", total_present)
        with col2:
            st.metric("Total Absent", total_absent)
        with col3:
            st.metric("Total Leave", total_leave)
        
        st.markdown("#### Pie Chart")
        if sum(status_data.values()) > 0:
            st.pie_chart(status_data)

# ============= SETTINGS PAGE =============
elif page == "⚙️ Settings":
    st.markdown("## ⚙️ Settings")
    
    st.markdown("### 📊 Grading System")
    st.info("""
    Current grading system:
    - **A**: 90-100%
    - **B**: 80-89%
    - **C**: 70-79%
    - **D**: 60-69%
    - **F**: Below 60%
    """)
    
    st.markdown("### 💾 Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Save All Data", use_container_width=True):
            save_data()
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear All Data", use_container_width=True):
            if st.checkbox("I understand this will delete all data"):
                st.session_state.students = {}
                if os.path.exists('attendance_data.json'):
                    os.remove('attendance_data.json')
                st.success("All data cleared!")
                st.rerun()
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    **Attendance Management System v1.0**
    
    A comprehensive web application for managing student attendance.
    
    **Features:**
    - Add and manage students
    - Track daily attendance
    - Calculate scores and grades
    - Generate detailed reports
    - View analytics and statistics
    
    **Technology Stack:**
    - Python
    - Streamlit
    - Pandas
    """)
