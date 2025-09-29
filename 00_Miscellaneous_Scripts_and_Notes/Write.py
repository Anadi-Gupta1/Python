"""
Python File Writing Operations - Learning Notes
=============================================

This module demonstrates various methods for writing to files in Python.
Covers different writing modes, best practices, and common use cases.

Author: Python Learning Notes
Date: September 2025
Topic: File Writing & I/O Operations
"""

def basic_file_writing():
    """
    Basic file writing using the 'w' mode
    WARNING: 'w' mode overwrites existing files
    """
    print("=== Basic File Writing ===")
    
    # Method 1: Using with statement (RECOMMENDED)
    with open("basic_output.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("File handling in Python is easy and fun!\n")
    
    print("✅ Basic file written successfully")
    print("📄 File: basic_output.txt")

def append_to_file():
    """
    Append content to existing file using 'a' mode
    This adds content without overwriting existing data
    """
    print("\n=== Appending to File ===")
    
    with open("append_output.txt", "a") as file:
        file.write("This line is appended.\n")
        file.write("Appending preserves existing content.\n")
        file.write(f"Current timestamp: {__import__('datetime').datetime.now()}\n")
    
    print("✅ Content appended successfully")
    print("📄 File: append_output.txt")

def write_multiple_lines():
    """
    Write multiple lines using different methods
    """
    print("\n=== Writing Multiple Lines ===")
    
    lines = [
        "Line 1: Introduction to file writing\n",
        "Line 2: Python makes file I/O simple\n",
        "Line 3: Always use context managers (with statement)\n",
        "Line 4: Don't forget to handle exceptions\n"
    ]
    
    # Method 1: Using writelines()
    with open("multiline_output.txt", "w") as file:
        file.writelines(lines)
    
    # Method 2: Using a loop
    with open("multiline_loop.txt", "w") as file:
        for i, line in enumerate(lines, 1):
            file.write(f"Entry {i}: {line}")
    
    print("✅ Multiple line files created")
    print("📄 Files: multiline_output.txt, multiline_loop.txt")

def write_with_formatting():
    """
    Demonstrate formatted writing with f-strings and .format()
    """
    print("\n=== Formatted File Writing ===")
    
    # Sample data
    student_data = [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 21, "grade": "B+"},
        {"name": "Charlie", "age": 19, "grade": "A-"}
    ]
    
    with open("formatted_output.txt", "w") as file:
        file.write("STUDENT REPORT\n")
        file.write("=" * 30 + "\n")
        
        for student in student_data:
            # Using f-strings (recommended for Python 3.6+)
            line = f"Name: {student['name']:10} | Age: {student['age']:2} | Grade: {student['grade']}\n"
            file.write(line)
        
        file.write("=" * 30 + "\n")
        file.write(f"Total Students: {len(student_data)}\n")
    
    print("✅ Formatted file written successfully")
    print("📄 File: formatted_output.txt")

def write_with_error_handling():
    """
    Demonstrate proper error handling when writing files
    """
    print("\n=== File Writing with Error Handling ===")
    
    try:
        with open("safe_output.txt", "w") as file:
            file.write("This is safely written content.\n")
            file.write("Error handling ensures robust code.\n")
            
            # Simulate writing different data types
            numbers = [1, 2, 3, 4, 5]
            file.write(f"Numbers: {', '.join(map(str, numbers))}\n")
            
        print("✅ File written safely with error handling")
        print("📄 File: safe_output.txt")
        
    except PermissionError:
        print("❌ Permission denied - cannot write to file")
    except IOError:
        print("❌ I/O error occurred while writing")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def write_different_encodings():
    """
    Demonstrate writing files with different character encodings
    """
    print("\n=== Writing with Different Encodings ===")
    
    # UTF-8 encoding (default and recommended)
    with open("utf8_output.txt", "w", encoding="utf-8") as file:
        file.write("English: Hello World!\n")
        file.write("Spanish: ¡Hola Mundo!\n")
        file.write("French: Bonjour le monde!\n")
        file.write("German: Hallo Welt!\n")
        file.write("Emoji: 🐍 Python is awesome! 🚀\n")
    
    print("✅ UTF-8 encoded file written")
    print("📄 File: utf8_output.txt")

def demonstrate_all_methods():
    """
    Run all file writing demonstrations
    """
    print("📝 PYTHON FILE WRITING METHODS - DEMONSTRATION")
    print("=" * 50)
    
    basic_file_writing()
    append_to_file()
    write_multiple_lines()
    write_with_formatting()
    write_with_error_handling()
    write_different_encodings()
    
    print("\n📁 Files created during demonstration:")
    import os
    for file in os.listdir('.'):
        if file.endswith('_output.txt') or 'loop' in file:
            print(f"  - {file}")

if __name__ == "__main__":
    """
    Main execution block for testing writing methods
    """
    print(__doc__)
    
    # Run all demonstrations
    demonstrate_all_methods()
    
    print("\n📚 LEARNING POINTS:")
    print("1. Use 'with' statement for automatic file closing")
    print("2. 'w' mode overwrites, 'a' mode appends")
    print("3. Always handle exceptions when working with files")
    print("4. Use f-strings for modern string formatting")
    print("5. Specify encoding explicitly when needed")
    
    print("\n💡 BEST PRACTICES:")
    print("- Always use context managers (with statement)")
    print("- Handle file operations errors gracefully")
    print("- Choose appropriate file modes ('w', 'a', 'x')")
    print("- Use meaningful filenames and organize output")