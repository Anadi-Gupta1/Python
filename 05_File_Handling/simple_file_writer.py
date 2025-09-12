"""
Professional File Writing Operations
====================================

This module demonstrates basic file writing operations using Python's
built-in file handling capabilities with best practices.

Author: Anadi Gupta
Date: September 2025
Purpose: Educational demonstration of file writing
"""

import os
from pathlib import Path

def write_sample_file():
    """
    Creates a sample text file with multiple lines of content.
    Uses context manager for safe file operations.
    """
    try:
        # Get current directory
        current_dir = Path(__file__).parent
        file_path = current_dir / "myfile.txt"
        
        print("📝 Writing sample file...")
        
        with open(file_path, "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a sample file.\n")
            file.write("File handling in Python is easy and fun!\n")
            file.write("Created using professional Python practices.\n")
            file.write(f"File created at: {file_path}\n")
        
        print(f"✅ Successfully created file: {file_path}")
        
        # Verify file was created and read content
        if file_path.exists():
            with open(file_path, "r") as file:
                content = file.read()
                print("\n📖 File contents:")
                print("-" * 40)
                print(content)
                print("-" * 40)
        
        return str(file_path)
        
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return None

def main():
    """Main function to demonstrate file writing"""
    print("🚀 Professional File Writing Demonstration")
    print("=" * 50)
    
    file_created = write_sample_file()
    
    if file_created:
        print(f"\n✨ File writing operation completed successfully!")
        print(f"📁 File location: {file_created}")
    else:
        print("\n❌ File writing operation failed!")

if __name__ == "__main__":
    main()