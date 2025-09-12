"""
File Reading Examples in Python
================================

This module demonstrates various methods of reading files in Python
with proper error handling and best practices.

Author: Anadi Gupta
Purpose: Educational demonstration of file reading techniques
"""

import os
import sys

def read_file_basic(file_path):
    """
    Basic file reading using the read() method.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: Content of the file or error message
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found"
    except PermissionError:
        return "Error: Permission denied to read the file"
    except Exception as e:
        return f"Error: {str(e)}"

def read_file_line_by_line(file_path):
    """
    Read file line by line for memory-efficient processing.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        list: List of lines or error message
    """
    try:
        lines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                lines.append(f"Line {line_num}: {line.strip()}")
        return lines
    except FileNotFoundError:
        return [f"Error: File '{file_path}' not found"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def read_file_all_lines(file_path):
    """
    Read all lines into a list using readlines() method.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        list: List of all lines or error message
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return [f"Error: File '{file_path}' not found"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def main():
    """Main function to demonstrate file reading methods."""
    print("=" * 60)
    print("🐍 PYTHON FILE READING EXAMPLES")
    print("=" * 60)
    
    # Get the current directory and file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "demofile.txt")
    
    print(f"\n📂 Working Directory: {current_dir}")
    print(f"📄 Target File: {os.path.basename(file_path)}")
    print(f"🔗 Full Path: {file_path}")
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"\n❌ Error: File '{file_path}' does not exist!")
        print("Please ensure the file exists before running this program.")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    
    # Method 1: Basic file reading
    print("\n📖 METHOD 1: Basic File Reading")
    print("-" * 40)
    content = read_file_basic(file_path)
    if content.startswith("Error:"):
        print(f"❌ {content}")
    else:
        print("✅ File read successfully!")
        print(f"📝 Content:\n{content}")
    
    print("\n" + "=" * 60)
    
    # Method 2: Line by line reading
    print("\n📝 METHOD 2: Line by Line Reading")
    print("-" * 40)
    lines = read_file_line_by_line(file_path)
    if lines and lines[0].startswith("Error:"):
        print(f"❌ {lines[0]}")
    else:
        print("✅ File read line by line successfully!")
        for line in lines:
            print(f"  {line}")
    
    print("\n" + "=" * 60)
    
    # Method 3: Read all lines
    print("\n📋 METHOD 3: Read All Lines")
    print("-" * 40)
    all_lines = read_file_all_lines(file_path)
    if all_lines and all_lines[0].startswith("Error:"):
        print(f"❌ {all_lines[0]}")
    else:
        print("✅ All lines read successfully!")
        print(f"📊 Total lines: {len(all_lines)}")
        for i, line in enumerate(all_lines, 1):
            print(f"  {i:2d}: {line}")
    
    print("\n" + "=" * 60)
    print("✨ File reading demonstration completed!")
    print("💡 Remember: Always use 'with' statement for safe file handling!")
    print("=" * 60)

if __name__ == "__main__":
    main()