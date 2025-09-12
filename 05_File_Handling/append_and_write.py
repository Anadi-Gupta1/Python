"""
Professional File Writing and Appending Operations in Python

This module demonstrates various file writing and appending techniques
with proper error handling and best practices.

Author: Anadi Gupta
Date: September 2025
Purpose: Educational demonstration of file operations
"""

import os
import logging
from datetime import datetime
from pathlib import Path

# Configure logging for better error tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_operations.log'),
        logging.StreamHandler()
    ]
)


class FileOperations:
    """
    A class to demonstrate professional file operations
    including writing, appending, and creating files.
    """
    
    def __init__(self):
        """Initialize with current directory path."""
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        
    def demonstrate_write_operations(self):
        """
        Comprehensive demonstration of file writing operations.
        
        Covers:
        - Writing to new files
        - Overwriting existing files
        - Appending to files
        - Creating files with different modes
        """
        print("="*60)
        print("    PROFESSIONAL FILE WRITING OPERATIONS")
        print("="*60)
        
        # 1. Writing to a new file
        self._write_new_file()
        
        # 2. Appending to existing file
        self._append_to_file()
        
        # 3. Overwriting existing content
        self._overwrite_file()
        
        # 4. Creating file with 'x' mode
        self._create_exclusive_file()
        
        # 5. Safe file operations
        self._demonstrate_safe_operations()
        
    def _write_new_file(self):
        """Write content to a new file."""
        print("\n1. WRITING TO A NEW FILE")
        print("-" * 30)
        
        file_path = os.path.join(self.current_dir, "output.txt")
        
        try:
            with open(file_path, 'w') as file:
                content = [
                    "Professional Python File Operations\n",
                    "=====================================\n",
                    f"Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
                    "This file demonstrates professional file writing.\n",
                    "\nKey Features:\n",
                    "- Error handling\n",
                    "- Context managers\n",
                    "- Proper documentation\n"
                ]
                
                file.writelines(content)
                
            print(f"✓ Successfully created and wrote to: {os.path.basename(file_path)}")
            self._display_file_content(file_path)
            
        except IOError as e:
            print(f"✗ Error writing to file: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            
    def _append_to_file(self):
        """Append content to an existing file."""
        print("\n2. APPENDING TO EXISTING FILE")
        print("-" * 30)
        
        file_path = os.path.join(self.current_dir, "output.txt")
        
        try:
            with open(file_path, 'a') as file:
                append_content = [
                    f"\n--- Appended at {datetime.now().strftime('%H:%M:%S')} ---\n",
                    "This content was appended to the existing file.\n",
                    "Append mode preserves original content.\n",
                    "Multiple append operations are possible.\n"
                ]
                
                file.writelines(append_content)
                
            print(f"✓ Successfully appended to: {os.path.basename(file_path)}")
            self._display_file_content(file_path)
            
        except IOError as e:
            print(f"✗ Error appending to file: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            
    def _overwrite_file(self):
        """Demonstrate overwriting existing file content."""
        print("\n3. OVERWRITING FILE CONTENT")
        print("-" * 30)
        
        demo_file = os.path.join(self.current_dir, "demo_overwrite.txt")
        
        try:
            # First, create a file with initial content
            with open(demo_file, 'w') as file:
                file.write("This is the original content.\n")
                file.write("This will be overwritten.\n")
            
            print(f"✓ Created initial file: {os.path.basename(demo_file)}")
            
            # Now overwrite it
            with open(demo_file, 'w') as file:
                new_content = [
                    "OVERWRITTEN CONTENT\n",
                    "==================\n",
                    f"Overwritten at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
                    "The original content has been completely replaced.\n"
                ]
                file.writelines(new_content)
                
            print(f"✓ Successfully overwrote: {os.path.basename(demo_file)}")
            self._display_file_content(demo_file)
            
        except IOError as e:
            print(f"✗ Error overwriting file: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            
    def _create_exclusive_file(self):
        """Create a file using exclusive creation mode."""
        print("\n4. EXCLUSIVE FILE CREATION")
        print("-" * 30)
        
        exclusive_file = os.path.join(self.current_dir, "exclusive_file.txt")
        
        try:
            with open(exclusive_file, 'x') as file:
                content = [
                    "Exclusive File Creation Demonstration\n",
                    "====================================\n",
                    f"Created using 'x' mode at: {datetime.now()}\n",
                    "This mode fails if file already exists.\n",
                    "Useful for preventing accidental overwrites.\n"
                ]
                file.writelines(content)
                
            print(f"✓ Successfully created exclusive file: {os.path.basename(exclusive_file)}")
            
        except FileExistsError:
            print(f"⚠ File already exists: {os.path.basename(exclusive_file)}")
            print("  'x' mode prevents overwriting existing files.")
        except IOError as e:
            print(f"✗ Error creating exclusive file: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            
    def _demonstrate_safe_operations(self):
        """Demonstrate safe file operations with comprehensive error handling."""
        print("\n5. SAFE FILE OPERATIONS")
        print("-" * 30)
        
        safe_file = os.path.join(self.current_dir, "safe_operations.txt")
        
        # Safe write operation
        success = self._safe_write(safe_file, [
            "Safe File Operations\n",
            "===================\n",
            "This demonstrates error-safe file operations.\n",
            f"Operation timestamp: {datetime.now()}\n"
        ])
        
        if success:
            print(f"✓ Safe write operation completed: {os.path.basename(safe_file)}")
        
        # Safe append operation
        success = self._safe_append(safe_file, [
            "\n--- Safe Append Operation ---\n",
            "This content was safely appended.\n",
            "Error handling ensures data integrity.\n"
        ])
        
        if success:
            print(f"✓ Safe append operation completed: {os.path.basename(safe_file)}")
            self._display_file_content(safe_file)
            
    def _safe_write(self, file_path, content):
        """Safely write content to a file with error handling."""
        try:
            with open(file_path, 'w') as file:
                file.writelines(content)
            return True
        except Exception as e:
            print(f"✗ Safe write failed: {e}")
            return False
            
    def _safe_append(self, file_path, content):
        """Safely append content to a file with error handling."""
        try:
            with open(file_path, 'a') as file:
                file.writelines(content)
            return True
        except Exception as e:
            print(f"✗ Safe append failed: {e}")
            return False
            
    def _display_file_content(self, file_path, max_lines=10):
        """Display file content with line numbering."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
            print(f"\n📄 Content of {os.path.basename(file_path)}:")
            print("─" * 40)
            
            for i, line in enumerate(lines[:max_lines], 1):
                print(f"{i:2d}│ {line.rstrip()}")
                
            if len(lines) > max_lines:
                print(f"   │ ... ({len(lines) - max_lines} more lines)")
                
            print("─" * 40)
            
        except Exception as e:
            print(f"✗ Error reading file: {e}")


def main():
    """
    Main function to demonstrate professional file operations.
    """
    print("🐍 Python Professional File Operations Demo")
    print("Author: Anadi Gupta")
    print("Purpose: Educational demonstration of file writing and appending")
    
    # Create and run demonstration
    file_ops = FileOperations()
    file_ops.demonstrate_write_operations()
    
    print("\n" + "="*60)
    print("📚 KEY LEARNING POINTS:")
    print("="*60)
    print("• Always use 'with' statement for automatic file closing")
    print("• Handle exceptions to prevent program crashes")
    print("• Use appropriate file modes for your operation:")
    print("  - 'w': Write (overwrites existing content)")
    print("  - 'a': Append (adds to end of file)")
    print("  - 'x': Create (fails if file exists)")
    print("• Validate file operations and provide user feedback")
    print("• Use absolute paths to avoid path-related issues")
    print("\n🎯 Professional file handling ensures data integrity!")


if __name__ == "__main__":
    main()