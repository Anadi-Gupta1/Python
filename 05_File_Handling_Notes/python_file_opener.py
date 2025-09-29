"""
Professional Python File Opening and Reading Operations

This module demonstrates various file opening and reading techniques
with best practices, error handling, and different reading methods.

Author: Anadi Gupta
Date: September 2025
Purpose: Educational demonstration of file opening operations
"""

import os
from pathlib import Path
from typing import List, Optional


class FileReader:
    """
    Professional file reading class with comprehensive error handling
    and multiple reading strategies.
    """
    
    def __init__(self, base_directory: Optional[str] = None):
        """
        Initialize FileReader with base directory.
        
        Args:
            base_directory: Optional base directory path. 
                          If None, uses current script directory.
        """
        if base_directory:
            self.base_dir = Path(base_directory)
        else:
            self.base_dir = Path(__file__).parent
            
    def demonstrate_file_opening(self):
        """
        Comprehensive demonstration of file opening and reading operations.
        
        Covers:
        - Basic file opening
        - Different reading methods
        - Error handling
        - Path management
        - Best practices
        """
        print("="*70)
        print("    PROFESSIONAL PYTHON FILE OPENING & READING")
        print("="*70)
        
        # 1. Basic file opening
        self._basic_file_opening()
        
        # 2. Using with statement (recommended)
        self._with_statement_opening()
        
        # 3. Different reading methods
        self._different_reading_methods()
        
        # 4. Reading specific portions
        self._partial_reading()
        
        # 5. Line-by-line reading
        self._line_by_line_reading()
        
        # 6. Safe file operations
        self._safe_file_operations()
        
        # 7. Working with different file paths
        self._path_management()
        
    def _basic_file_opening(self):
        """Demonstrate basic file opening (not recommended approach)."""
        print("\n1. BASIC FILE OPENING (Legacy Method)")
        print("-" * 45)
        
        file_path = self.base_dir / "demofile.txt"
        
        try:
            # Traditional method (not recommended)
            file = open(file_path, 'r')
            content = file.read()
            file.close()  # Must manually close
            
            print(f"✓ Successfully opened: {file_path.name}")
            print(f"📄 Content preview: {content[:50]}...")
            print("⚠ Note: Manual file closing required with this method")
            
        except FileNotFoundError:
            print(f"✗ File not found: {file_path}")
        except Exception as e:
            print(f"✗ Error opening file: {e}")
            
    def _with_statement_opening(self):
        """Demonstrate file opening with 'with' statement (recommended)."""
        print("\n2. WITH STATEMENT OPENING (Recommended)")
        print("-" * 45)
        
        file_path = self.base_dir / "demofile.txt"
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                
            print(f"✓ Successfully opened: {file_path.name}")
            print(f"📄 Content preview: {content[:50]}...")
            print("✓ File automatically closed by 'with' statement")
            
        except FileNotFoundError:
            print(f"✗ File not found: {file_path}")
        except Exception as e:
            print(f"✗ Error opening file: {e}")
            
    def _different_reading_methods(self):
        """Demonstrate different file reading methods."""
        print("\n3. DIFFERENT READING METHODS")
        print("-" * 35)
        
        file_path = self.base_dir / "demofile.txt"
        
        if not file_path.exists():
            print(f"✗ File not found: {file_path}")
            return
            
        try:
            # Method 1: read() - entire file
            with open(file_path, 'r') as file:
                entire_content = file.read()
            print("📖 Method 1: read() - Entire file content")
            print(f"   Content: {entire_content.strip()}")
            
            # Method 2: readlines() - all lines as list
            with open(file_path, 'r') as file:
                all_lines = file.readlines()
            print(f"\n📋 Method 2: readlines() - All lines as list")
            print(f"   Lines count: {len(all_lines)}")
            for i, line in enumerate(all_lines, 1):
                print(f"   Line {i}: {line.strip()}")
                
            # Method 3: readline() - single line
            with open(file_path, 'r') as file:
                first_line = file.readline()
                second_line = file.readline()
            print(f"\n📝 Method 3: readline() - Single line reading")
            print(f"   First line: {first_line.strip()}")
            print(f"   Second line: {second_line.strip()}")
            
        except Exception as e:
            print(f"✗ Error in reading methods: {e}")
            
    def _partial_reading(self):
        """Demonstrate reading specific portions of files."""
        print("\n4. PARTIAL FILE READING")
        print("-" * 30)
        
        file_path = self.base_dir / "demofile.txt"
        
        if not file_path.exists():
            print(f"✗ File not found: {file_path}")
            return
            
        try:
            # Read first N characters
            with open(file_path, 'r') as file:
                first_10_chars = file.read(10)
            print(f"📄 First 10 characters: '{first_10_chars}'")
            
            # Read specific number of characters
            with open(file_path, 'r') as file:
                first_25_chars = file.read(25)
            print(f"📄 First 25 characters: '{first_25_chars}'")
            
            # Reset and read different portion
            with open(file_path, 'r') as file:
                file.read(10)  # Skip first 10 characters
                next_15_chars = file.read(15)
            print(f"📄 Characters 11-25: '{next_15_chars}'")
            
        except Exception as e:
            print(f"✗ Error in partial reading: {e}")
            
    def _line_by_line_reading(self):
        """Demonstrate line-by-line file reading."""
        print("\n5. LINE-BY-LINE READING")
        print("-" * 30)
        
        file_path = self.base_dir / "demofile.txt"
        
        if not file_path.exists():
            print(f"✗ File not found: {file_path}")
            return
            
        try:
            print("📚 Reading file line by line:")
            with open(file_path, 'r') as file:
                line_number = 1
                for line in file:
                    print(f"   Line {line_number:2d}: {line.strip()}")
                    line_number += 1
                    
            print(f"✓ Successfully read {line_number - 1} lines")
            
        except Exception as e:
            print(f"✗ Error in line-by-line reading: {e}")
            
    def _safe_file_operations(self):
        """Demonstrate safe file operations with comprehensive error handling."""
        print("\n6. SAFE FILE OPERATIONS")
        print("-" * 30)
        
        # Try to read existing file
        result = self._safe_read_file("demofile.txt")
        if result:
            print(f"✓ Safe read successful: {result[:50]}...")
        
        # Try to read non-existent file
        result = self._safe_read_file("nonexistent.txt")
        if not result:
            print("✓ Safe read handled missing file gracefully")
            
    def _safe_read_file(self, filename: str) -> Optional[str]:
        """
        Safely read a file with comprehensive error handling.
        
        Args:
            filename: Name of the file to read
            
        Returns:
            File content as string if successful, None otherwise
        """
        file_path = self.base_dir / filename
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"✓ Successfully read: {filename}")
            return content
            
        except FileNotFoundError:
            print(f"⚠ File not found: {filename}")
            return None
        except PermissionError:
            print(f"✗ Permission denied: {filename}")
            return None
        except UnicodeDecodeError:
            print(f"✗ Encoding error in: {filename}")
            return None
        except Exception as e:
            print(f"✗ Unexpected error reading {filename}: {e}")
            return None
            
    def _path_management(self):
        """Demonstrate different path management techniques."""
        print("\n7. PATH MANAGEMENT")
        print("-" * 25)
        
        # Current directory files
        print("📁 Files in current directory:")
        try:
            for file_path in self.base_dir.iterdir():
                if file_path.is_file():
                    size = file_path.stat().st_size
                    print(f"   📄 {file_path.name} ({size} bytes)")
                    
        except Exception as e:
            print(f"✗ Error listing directory: {e}")
            
        # Different path formats
        print("\n🛤 Path format examples:")
        demo_file = self.base_dir / "demofile.txt"
        print(f"   Absolute path: {demo_file.absolute()}")
        print(f"   Relative path: {demo_file.name}")
        print(f"   Parent directory: {demo_file.parent}")
        print(f"   File exists: {demo_file.exists()}")
        print(f"   Is file: {demo_file.is_file()}")
        
    def get_file_info(self, filename: str) -> dict:
        """
        Get comprehensive information about a file.
        
        Args:
            filename: Name of the file to analyze
            
        Returns:
            Dictionary containing file information
        """
        file_path = self.base_dir / filename
        
        info = {
            'name': filename,
            'exists': file_path.exists(),
            'is_file': file_path.is_file() if file_path.exists() else False,
            'size': None,
            'absolute_path': str(file_path.absolute()),
            'extension': file_path.suffix
        }
        
        if file_path.exists() and file_path.is_file():
            try:
                stat = file_path.stat()
                info['size'] = stat.st_size
                info['modified'] = stat.st_mtime
            except Exception:
                pass
                
        return info


def main():
    """
    Main function to demonstrate professional file opening operations.
    """
    print("🐍 Python Professional File Opening & Reading Demo")
    print("Author: Anadi Gupta")
    print("Purpose: Educational demonstration of file opening best practices")
    
    # Create and run demonstration
    reader = FileReader()
    reader.demonstrate_file_opening()
    
    print("\n" + "="*70)
    print("📚 PROFESSIONAL FILE OPENING BEST PRACTICES:")
    print("="*70)
    print("✅ Always use 'with' statement for automatic file management")
    print("✅ Handle exceptions to prevent program crashes")
    print("✅ Use appropriate encoding (UTF-8 recommended)")
    print("✅ Choose the right reading method for your needs:")
    print("   • read() - Entire file content")
    print("   • readline() - Single line at a time")
    print("   • readlines() - All lines as a list")
    print("   • Iterator - Memory-efficient line-by-line")
    print("✅ Use pathlib.Path for modern path handling")
    print("✅ Always validate file existence before operations")
    print("✅ Consider file size and memory usage for large files")
    print("\n🎯 Professional file handling ensures reliability and efficiency!")


if __name__ == "__main__":
    main()