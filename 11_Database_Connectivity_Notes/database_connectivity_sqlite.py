"""
Database Connectivity in Python - SQLite Examples
=================================================

Educational guide to database operations: SQLite integration, CRUD operations, connection management, and data persistence.
Includes best practices for database interactions.

Author: Python Learning Notes
Date: September 2025
Topic: Database, SQLite, CRUD, Connection Management
"""

import sqlite3
from typing import List, Tuple, Optional
import os

# =============================================================================
# DATABASE CONNECTION MANAGEMENT
# =============================================================================

class DatabaseManager:
    """Context manager for database connections"""
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

# =============================================================================
# TABLE CREATION
# =============================================================================

def create_tables():
    """Create sample tables for demonstration"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        
        # Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT,
                enrollment_date DATE DEFAULT CURRENT_DATE
            )
        ''')
        
        # Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                instructor TEXT,
                credits INTEGER
            )
        ''')
        
        # Enrollments table (many-to-many relationship)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER,
                course_id INTEGER,
                grade TEXT,
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id),
                PRIMARY KEY (student_id, course_id)
            )
        ''')
        
        print("Tables created successfully!")

# =============================================================================
# CRUD OPERATIONS
# =============================================================================

def insert_sample_data():
    """Insert sample data into tables"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        
        # Insert students
        students = [
            ('Alice Johnson', 20, 'A'),
            ('Bob Smith', 19, 'B+'),
            ('Carol Davis', 21, 'A-'),
            ('David Wilson', 18, 'B')
        ]
        cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students)
        
        # Insert courses
        courses = [
            ('Mathematics', 'Dr. Smith', 3),
            ('Physics', 'Dr. Johnson', 4),
            ('Chemistry', 'Dr. Davis', 3),
            ('Computer Science', 'Dr. Wilson', 4)
        ]
        cursor.executemany('INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)', courses)
        
        # Insert enrollments
        enrollments = [
            (1, 1, 'A'), (1, 2, 'B+'), (1, 4, 'A'),
            (2, 1, 'B'), (2, 3, 'A-'),
            (3, 2, 'A'), (3, 3, 'A'), (3, 4, 'A-'),
            (4, 1, 'B+'), (4, 4, 'A')
        ]
        cursor.executemany('INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)', enrollments)
        
        print("Sample data inserted successfully!")

def read_students() -> List[Tuple]:
    """Read all students from database"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()

def update_student_grade(student_id: int, new_grade: str):
    """Update a student's grade"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE students SET grade = ? WHERE id = ?', (new_grade, student_id))
        print(f"Updated student {student_id}'s grade to {new_grade}")

def delete_student(student_id: int):
    """Delete a student and their enrollments"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        # Delete enrollments first (foreign key constraint)
        cursor.execute('DELETE FROM enrollments WHERE student_id = ?', (student_id,))
        cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        print(f"Deleted student {student_id} and their enrollments")

# =============================================================================
# ADVANCED QUERIES
# =============================================================================

def get_student_course_info():
    """Get students with their enrolled courses"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT s.name, c.course_name, e.grade, c.credits
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            JOIN courses c ON e.course_id = c.id
            ORDER BY s.name, c.course_name
        ''')
        return cursor.fetchall()

def get_course_statistics():
    """Get statistics for each course"""
    with DatabaseManager('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.course_name, COUNT(e.student_id) as enrolled_students,
                   AVG(CASE WHEN e.grade = 'A' THEN 4.0
                            WHEN e.grade = 'A-' THEN 3.7
                            WHEN e.grade = 'B+' THEN 3.3
                            WHEN e.grade = 'B' THEN 3.0
                            ELSE 0 END) as avg_gpa
            FROM courses c
            LEFT JOIN enrollments e ON c.id = e.course_id
            GROUP BY c.id, c.course_name
        ''')
        return cursor.fetchall()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    # Create database and tables
    create_tables()
    
    # Insert sample data
    insert_sample_data()
    
    # Read operations
    print("\nStudents:")
    students = read_students()
    for student in students:
        print(student)
    
    # Update operation
    print("\nUpdating student grade...")
    update_student_grade(1, 'A+')
    
    # Advanced queries
    print("\nStudent-Course Information:")
    student_courses = get_student_course_info()
    for info in student_courses:
        print(info)
    
    print("\nCourse Statistics:")
    stats = get_course_statistics()
    for stat in stats:
        print(stat)
    
    # Delete operation (commented out to preserve data)
    # print("\nDeleting student...")
    # delete_student(4)
    
    print("\nDatabase operations completed successfully!")

if __name__ == "__main__":
    main()
