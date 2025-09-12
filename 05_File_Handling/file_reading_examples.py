# File handling program with proper error handling
import os

try:
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "demofile.txt")
    
    # Method 1: Using open() with error handling
    print("=== Method 1: Basic file reading ===")
    with open(file_path, 'r') as f:
        content = f.read()
        print("File content:")
        print(content)
        
    print("\n=== Method 2: Reading line by line ===")
    with open(file_path, 'r') as f:
        line_number = 1
        for line in f:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
            
    print("\n=== Method 3: Reading all lines into a list ===")
    with open(file_path, 'r') as f:
        lines = f.readlines()
        print(f"Total lines: {len(lines)}")
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file 'demofile.txt' was not found in the directory.")
    print(f"Looking for file at: {file_path}")
    print("Make sure the file exists and is in the same directory as this script.")
    
except PermissionError:
    print("Error: Permission denied. You don't have permission to read this file.")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
finally:
    print("\n=== File operation completed ===")