"""
Comprehensive File Operations - Complete Guide to File Handling in Python
========================================================================

Master class covering all aspects of file operations including reading, writing,
appending, binary operations, file management, advanced techniques, and real-world
applications with professional error handling and performance optimization.

Author: Python Learning Notes
Date: September 2025
Topic: Complete File Handling, I/O Operations, File Management
"""

import os
import sys
import json
import csv
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from datetime import datetime
import shutil
import tempfile
import contextlib
import io

# =============================================================================
# COMPREHENSIVE FILE OPERATIONS THEORY
# =============================================================================

def explain_file_operations_theory():
    """
    Educational explanation of complete file operations concepts
    """
    print("📚 COMPREHENSIVE FILE OPERATIONS")
    print("=" * 35)
    
    print("\n🔑 File Operations Fundamentals:")
    print("File operations are the foundation of data persistence:")
    print("   • Creating and managing data files")
    print("   • Configuration and settings storage")
    print("   • Log file management and analysis")
    print("   • Data import/export operations")
    print("   • Backup and recovery systems")
    print("   • Inter-application communication")
    
    print("\n📋 File Modes Reference:")
    modes = [
        ("'r'", "Read only", "Default, file must exist", "Text reading"),
        ("'w'", "Write only", "Truncates/creates file", "Text writing"),
        ("'a'", "Append only", "Creates if not exists", "Adding to end"),
        ("'x'", "Exclusive create", "Fails if file exists", "Safe creation"),
        ("'r+'", "Read & Write", "File must exist", "Update existing"),
        ("'w+'", "Write & Read", "Truncates/creates", "Create & modify"),
        ("'a+'", "Append & Read", "Creates if needed", "Append & read"),
        ("'rb'", "Binary read", "For binary files", "Images, executables"),
        ("'wb'", "Binary write", "Binary output", "Binary creation"),
        ("'ab'", "Binary append", "Binary addition", "Binary logs")
    ]
    
    print("   ┌─────────┬─────────────┬─────────────────┬─────────────────┐")
    print("   │ Mode    │ Operation   │ File Behavior   │ Use Case        │")
    print("   ├─────────┼─────────────┼─────────────────┼─────────────────┤")
    for mode, operation, behavior, use_case in modes:
        print(f"   │ {mode:<7} │ {operation:<11} │ {behavior:<15} │ {use_case:<15} │")
    print("   └─────────┴─────────────┴─────────────────┴─────────────────┘")
    
    print("\n⚠️  Common File Operation Challenges:")
    print("   • File locking and concurrent access")
    print("   • Encoding and character set issues")
    print("   • Path separators across platforms")
    print("   • File permissions and security")
    print("   • Large file memory management")
    print("   • Atomic operations and consistency")

# =============================================================================
# PROFESSIONAL FILE OPERATIONS CLASS
# =============================================================================

class ComprehensiveFileOperations:
    """
    Professional file operations with comprehensive error handling
    """
    
    def __init__(self, base_directory: str = None):
        """
        Initialize file operations manager
        
        Args:
            base_directory: Base directory for operations (default: current)
        """
        self.base_dir = Path(base_directory) if base_directory else Path.cwd()
        self.operations_log = []
        self.start_time = datetime.now()
        
        # Ensure base directory exists
        self.base_dir.mkdir(exist_ok=True)
        
        print(f"🔧 File Operations Manager Initialized")
        print(f"   Base directory: {self.base_dir}")
        print(f"   Start time: {self.start_time}")
    
    def log_operation(self, operation: str, details: str, success: bool = True):
        """Log file operations for tracking"""
        log_entry = {
            'timestamp': datetime.now(),
            'operation': operation,
            'details': details,
            'success': success
        }
        self.operations_log.append(log_entry)
    
    # =========================================================================
    # BASIC FILE OPERATIONS
    # =========================================================================
    
    def write_file(self, filename: str, content: str, mode: str = 'w',
                  encoding: str = 'utf-8') -> bool:
        """
        Professional file writing with comprehensive error handling
        
        Args:
            filename: Name of file to write
            content: Content to write
            mode: File mode ('w', 'a', 'x')
            encoding: Text encoding
            
        Returns:
            bool: True if successful
        """
        try:
            filepath = self.base_dir / filename
            
            print(f"\n📝 Writing File: '{filename}'")
            print("=" * 20)
            print(f"   Mode: {mode}")
            print(f"   Encoding: {encoding}")
            print(f"   Content length: {len(content):,} characters")
            
            # Pre-write validations
            if mode == 'x' and filepath.exists():
                print(f"   ❌ File already exists (exclusive mode)")
                return False
            
            if mode in ['r+', 'a+'] and not filepath.exists():
                print(f"   ❌ File doesn't exist (required for mode {mode})")
                return False
            
            start_time = time.time()
            
            with open(filepath, mode, encoding=encoding) as file:
                file.write(content)
            
            write_time = (time.time() - start_time) * 1000
            
            file_size = filepath.stat().st_size
            
            print(f"   ✅ File written successfully")
            print(f"   File size: {file_size:,} bytes")
            print(f"   Write time: {write_time:.2f} ms")
            
            self.log_operation('write', f'{filename} ({len(content)} chars)', True)
            return True
            
        except PermissionError:
            print(f"   ❌ Permission denied writing to '{filename}'")
            self.log_operation('write', f'{filename} (permission denied)', False)
            return False
        except Exception as e:
            print(f"   ❌ Error writing file: {e}")
            self.log_operation('write', f'{filename} (error: {e})', False)
            return False
    
    def read_file(self, filename: str, encoding: str = 'utf-8') -> Optional[str]:
        """
        Professional file reading with error handling
        
        Args:
            filename: Name of file to read
            encoding: Text encoding
            
        Returns:
            str: File content or None if error
        """
        try:
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return None
            
            print(f"\n📖 Reading File: '{filename}'")
            print("=" * 20)
            
            file_size = filepath.stat().st_size
            modified_time = datetime.fromtimestamp(filepath.stat().st_mtime)
            
            print(f"   File size: {file_size:,} bytes")
            print(f"   Modified: {modified_time}")
            print(f"   Encoding: {encoding}")
            
            start_time = time.time()
            
            with open(filepath, 'r', encoding=encoding) as file:
                content = file.read()
            
            read_time = (time.time() - start_time) * 1000
            
            print(f"   ✅ File read successfully")
            print(f"   Characters read: {len(content):,}")
            print(f"   Read time: {read_time:.2f} ms")
            
            self.log_operation('read', f'{filename} ({len(content)} chars)', True)
            return content
            
        except UnicodeDecodeError as e:
            print(f"   ❌ Encoding error: {e}")
            self.log_operation('read', f'{filename} (encoding error)', False)
            return None
        except Exception as e:
            print(f"   ❌ Error reading file: {e}")
            self.log_operation('read', f'{filename} (error: {e})', False)
            return None
    
    def append_to_file(self, filename: str, content: str, 
                      encoding: str = 'utf-8') -> bool:
        """
        Append content to file with professional handling
        
        Args:
            filename: Name of file to append to
            content: Content to append
            encoding: Text encoding
            
        Returns:
            bool: True if successful
        """
        try:
            filepath = self.base_dir / filename
            
            print(f"\n➕ Appending to File: '{filename}'")
            print("=" * 25)
            
            original_size = filepath.stat().st_size if filepath.exists() else 0
            print(f"   Original size: {original_size:,} bytes")
            print(f"   Appending: {len(content):,} characters")
            
            start_time = time.time()
            
            with open(filepath, 'a', encoding=encoding) as file:
                file.write(content)
            
            append_time = (time.time() - start_time) * 1000
            
            new_size = filepath.stat().st_size
            added_bytes = new_size - original_size
            
            print(f"   ✅ Content appended successfully")
            print(f"   New size: {new_size:,} bytes")
            print(f"   Added: {added_bytes:,} bytes")
            print(f"   Append time: {append_time:.2f} ms")
            
            self.log_operation('append', f'{filename} (+{len(content)} chars)', True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error appending to file: {e}")
            self.log_operation('append', f'{filename} (error: {e})', False)
            return False
    
    # =========================================================================
    # ADVANCED FILE OPERATIONS
    # =========================================================================
    
    def copy_file(self, source: str, destination: str, 
                 preserve_metadata: bool = True) -> bool:
        """
        Professional file copying with metadata preservation
        
        Args:
            source: Source filename
            destination: Destination filename
            preserve_metadata: Whether to preserve file metadata
            
        Returns:
            bool: True if successful
        """
        try:
            src_path = self.base_dir / source
            dest_path = self.base_dir / destination
            
            if not src_path.exists():
                print(f"❌ Source file '{source}' not found")
                return False
            
            print(f"\n📋 Copying File: '{source}' → '{destination}'")
            print("=" * 30)
            
            src_size = src_path.stat().st_size
            print(f"   Source size: {src_size:,} bytes")
            print(f"   Preserve metadata: {preserve_metadata}")
            
            start_time = time.time()
            
            if preserve_metadata:
                shutil.copy2(src_path, dest_path)
            else:
                shutil.copy(src_path, dest_path)
            
            copy_time = (time.time() - start_time) * 1000
            
            dest_size = dest_path.stat().st_size
            
            print(f"   ✅ File copied successfully")
            print(f"   Destination size: {dest_size:,} bytes")
            print(f"   Copy time: {copy_time:.2f} ms")
            
            self.log_operation('copy', f'{source} → {destination}', True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error copying file: {e}")
            self.log_operation('copy', f'{source} → {destination} (error)', False)
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        """
        Professional file moving/renaming
        
        Args:
            source: Source filename
            destination: Destination filename
            
        Returns:
            bool: True if successful
        """
        try:
            src_path = self.base_dir / source
            dest_path = self.base_dir / destination
            
            if not src_path.exists():
                print(f"❌ Source file '{source}' not found")
                return False
            
            print(f"\n🔄 Moving File: '{source}' → '{destination}'")
            print("=" * 30)
            
            src_size = src_path.stat().st_size
            print(f"   File size: {src_size:,} bytes")
            
            start_time = time.time()
            
            shutil.move(src_path, dest_path)
            
            move_time = (time.time() - start_time) * 1000
            
            print(f"   ✅ File moved successfully")
            print(f"   Move time: {move_time:.2f} ms")
            
            self.log_operation('move', f'{source} → {destination}', True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error moving file: {e}")
            self.log_operation('move', f'{source} → {destination} (error)', False)
            return False
    
    def delete_file(self, filename: str, confirm: bool = False) -> bool:
        """
        Safe file deletion with confirmation
        
        Args:
            filename: Name of file to delete
            confirm: Skip confirmation if True
            
        Returns:
            bool: True if successful
        """
        try:
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return False
            
            print(f"\n🗑️  Deleting File: '{filename}'")
            print("=" * 20)
            
            file_size = filepath.stat().st_size
            print(f"   File size: {file_size:,} bytes")
            
            if not confirm:
                response = input(f"   Confirm deletion of '{filename}'? (y/N): ")
                if response.lower() != 'y':
                    print("   ❌ Deletion cancelled")
                    return False
            
            filepath.unlink()
            
            print(f"   ✅ File deleted successfully")
            
            self.log_operation('delete', filename, True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error deleting file: {e}")
            self.log_operation('delete', f'{filename} (error: {e})', False)
            return False
    
    # =========================================================================
    # STRUCTURED DATA OPERATIONS
    # =========================================================================
    
    def write_json(self, filename: str, data: Dict[str, Any], 
                  indent: int = 2) -> bool:
        """
        Write data to JSON file with formatting
        
        Args:
            filename: JSON filename
            data: Dictionary to write
            indent: JSON indentation level
            
        Returns:
            bool: True if successful
        """
        try:
            filepath = self.base_dir / filename
            
            print(f"\n🔗 Writing JSON: '{filename}'")
            print("=" * 20)
            print(f"   Data keys: {list(data.keys())}")
            print(f"   Indent level: {indent}")
            
            start_time = time.time()
            
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent, ensure_ascii=False)
            
            write_time = (time.time() - start_time) * 1000
            
            file_size = filepath.stat().st_size
            
            print(f"   ✅ JSON written successfully")
            print(f"   File size: {file_size:,} bytes")
            print(f"   Write time: {write_time:.2f} ms")
            
            self.log_operation('write_json', filename, True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error writing JSON: {e}")
            self.log_operation('write_json', f'{filename} (error: {e})', False)
            return False
    
    def read_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Read and parse JSON file
        
        Args:
            filename: JSON filename
            
        Returns:
            Dict: Parsed JSON data or None if error
        """
        try:
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"❌ JSON file '{filename}' not found")
                return None
            
            print(f"\n🔗 Reading JSON: '{filename}'")
            print("=" * 20)
            
            start_time = time.time()
            
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            read_time = (time.time() - start_time) * 1000
            
            print(f"   ✅ JSON loaded successfully")
            print(f"   Data type: {type(data).__name__}")
            
            if isinstance(data, dict):
                print(f"   Keys: {list(data.keys())}")
            elif isinstance(data, list):
                print(f"   Items: {len(data)}")
            
            print(f"   Read time: {read_time:.2f} ms")
            
            self.log_operation('read_json', filename, True)
            return data
            
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON parsing error: {e}")
            self.log_operation('read_json', f'{filename} (parse error)', False)
            return None
        except Exception as e:
            print(f"   ❌ Error reading JSON: {e}")
            self.log_operation('read_json', f'{filename} (error: {e})', False)
            return None
    
    def write_csv(self, filename: str, data: List[List[str]], 
                 headers: List[str] = None) -> bool:
        """
        Write data to CSV file with headers
        
        Args:
            filename: CSV filename
            data: List of rows (each row is a list)
            headers: Optional column headers
            
        Returns:
            bool: True if successful
        """
        try:
            filepath = self.base_dir / filename
            
            print(f"\n📊 Writing CSV: '{filename}'")
            print("=" * 20)
            print(f"   Rows: {len(data):,}")
            print(f"   Columns: {len(data[0]) if data else 0}")
            print(f"   Headers: {'Yes' if headers else 'No'}")
            
            start_time = time.time()
            
            with open(filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                if headers:
                    writer.writerow(headers)
                
                writer.writerows(data)
            
            write_time = (time.time() - start_time) * 1000
            
            file_size = filepath.stat().st_size
            
            print(f"   ✅ CSV written successfully")
            print(f"   File size: {file_size:,} bytes")
            print(f"   Write time: {write_time:.2f} ms")
            
            self.log_operation('write_csv', f'{filename} ({len(data)} rows)', True)
            return True
            
        except Exception as e:
            print(f"   ❌ Error writing CSV: {e}")
            self.log_operation('write_csv', f'{filename} (error: {e})', False)
            return False
    
    def read_csv(self, filename: str, has_headers: bool = True) -> Optional[Dict[str, Any]]:
        """
        Read and parse CSV file
        
        Args:
            filename: CSV filename
            has_headers: Whether first row contains headers
            
        Returns:
            Dict: Contains 'headers' and 'data' keys, or None if error
        """
        try:
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"❌ CSV file '{filename}' not found")
                return None
            
            print(f"\n📊 Reading CSV: '{filename}'")
            print("=" * 20)
            
            start_time = time.time()
            
            with open(filepath, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                
                rows = list(csv_reader)
                
                if has_headers and rows:
                    headers = rows[0]
                    data = rows[1:]
                else:
                    headers = None
                    data = rows
            
            read_time = (time.time() - start_time) * 1000
            
            print(f"   ✅ CSV loaded successfully")
            print(f"   Rows: {len(data):,}")
            print(f"   Columns: {len(data[0]) if data else 0}")
            print(f"   Headers: {headers[:5] if headers else 'None'}...")
            print(f"   Read time: {read_time:.2f} ms")
            
            result = {
                'headers': headers,
                'data': data
            }
            
            self.log_operation('read_csv', f'{filename} ({len(data)} rows)', True)
            return result
            
        except Exception as e:
            print(f"   ❌ Error reading CSV: {e}")
            self.log_operation('read_csv', f'{filename} (error: {e})', False)
            return None
    
    # =========================================================================
    # UTILITY AND INFORMATION METHODS
    # =========================================================================
    
    def list_files(self, pattern: str = "*", show_details: bool = True) -> List[Path]:
        """
        List files in the base directory with optional filtering
        
        Args:
            pattern: Glob pattern to filter files
            show_details: Whether to show detailed information
            
        Returns:
            List[Path]: List of matching file paths
        """
        try:
            print(f"\n📁 Listing Files: '{pattern}'")
            print("=" * 20)
            
            files = list(self.base_dir.glob(pattern))
            files = [f for f in files if f.is_file()]  # Only files
            
            print(f"   Found {len(files)} files")
            
            if show_details and files:
                print("\n   📋 File Details:")
                print("   ┌─────────────────────┬─────────────┬─────────────────────┐")
                print("   │ Name                │ Size        │ Modified            │")
                print("   ├─────────────────────┼─────────────┼─────────────────────┤")
                
                for file_path in sorted(files):
                    name = file_path.name
                    size = file_path.stat().st_size
                    modified = datetime.fromtimestamp(file_path.stat().st_mtime)
                    
                    # Truncate long names
                    display_name = name[:19] if len(name) <= 19 else name[:16] + "..."
                    
                    print(f"   │ {display_name:<19} │ {size:>9,} B │ {modified:%Y-%m-%d %H:%M} │")
                
                print("   └─────────────────────┴─────────────┴─────────────────────┘")
            
            return files
            
        except Exception as e:
            print(f"   ❌ Error listing files: {e}")
            return []
    
    def get_file_info(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Get comprehensive information about a file
        
        Args:
            filename: Name of file to analyze
            
        Returns:
            Dict: File information or None if error
        """
        try:
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return None
            
            print(f"\n🔍 File Information: '{filename}'")
            print("=" * 25)
            
            stat = filepath.stat()
            
            info = {
                'name': filename,
                'path': str(filepath),
                'size_bytes': stat.st_size,
                'size_kb': stat.st_size / 1024,
                'size_mb': stat.st_size / (1024 * 1024),
                'created': datetime.fromtimestamp(stat.st_ctime),
                'modified': datetime.fromtimestamp(stat.st_mtime),
                'accessed': datetime.fromtimestamp(stat.st_atime),
                'is_readable': os.access(filepath, os.R_OK),
                'is_writable': os.access(filepath, os.W_OK),
                'is_executable': os.access(filepath, os.X_OK)
            }
            
            # Display information
            print(f"   📁 Path: {info['path']}")
            print(f"   📏 Size: {info['size_bytes']:,} bytes ({info['size_kb']:.1f} KB)")
            print(f"   📅 Created: {info['created']}")
            print(f"   📝 Modified: {info['modified']}")
            print(f"   👁️  Accessed: {info['accessed']}")
            print(f"   🔒 Permissions: R{'✓' if info['is_readable'] else '✗'} "
                  f"W{'✓' if info['is_writable'] else '✗'} "
                  f"X{'✓' if info['is_executable'] else '✗'}")
            
            return info
            
        except Exception as e:
            print(f"   ❌ Error getting file info: {e}")
            return None
    
    def get_operations_summary(self) -> Dict[str, Any]:
        """
        Get summary of all operations performed
        
        Returns:
            Dict: Operations summary
        """
        print(f"\n📊 OPERATIONS SUMMARY")
        print("=" * 21)
        
        total_ops = len(self.operations_log)
        successful_ops = sum(1 for op in self.operations_log if op['success'])
        failed_ops = total_ops - successful_ops
        
        # Count operations by type
        op_counts = {}
        for op in self.operations_log:
            op_type = op['operation']
            op_counts[op_type] = op_counts.get(op_type, 0) + 1
        
        session_duration = datetime.now() - self.start_time
        
        summary = {
            'total_operations': total_ops,
            'successful_operations': successful_ops,
            'failed_operations': failed_ops,
            'success_rate': (successful_ops / total_ops * 100) if total_ops > 0 else 0,
            'operation_counts': op_counts,
            'session_duration': session_duration
        }
        
        # Display summary
        print(f"   Total operations: {total_ops}")
        print(f"   Successful: {successful_ops} ({summary['success_rate']:.1f}%)")
        print(f"   Failed: {failed_ops}")
        print(f"   Session duration: {session_duration}")
        
        if op_counts:
            print(f"\n   📋 Operations by type:")
            for op_type, count in sorted(op_counts.items()):
                print(f"   • {op_type}: {count}")
        
        return summary

# =============================================================================
# DEMONSTRATION AND INTERACTIVE FUNCTIONS
# =============================================================================

def demonstrate_all_operations():
    """
    Comprehensive demonstration of all file operations
    """
    print("\n" + "="*60)
    print("COMPREHENSIVE FILE OPERATIONS DEMONSTRATION")
    print("="*60)
    
    # Initialize operations manager
    file_ops = ComprehensiveFileOperations()
    
    # Sample data for demonstrations
    sample_text = """Hello, World!
This is a sample file created for demonstration.
It contains multiple lines of text.
Each line demonstrates different aspects of file operations.
Final line: File operations in Python are powerful!"""
    
    sample_json_data = {
        'application': 'File Operations Demo',
        'version': '1.0.0',
        'features': ['read', 'write', 'append', 'copy', 'move', 'delete'],
        'settings': {
            'encoding': 'utf-8',
            'auto_backup': True,
            'buffer_size': 8192
        },
        'metadata': {
            'created': datetime.now().isoformat(),
            'author': 'Python Learning Notes'
        }
    }
    
    sample_csv_data = [
        ['Alice', '25', 'Engineer', 'New York'],
        ['Bob', '30', 'Designer', 'London'],
        ['Charlie', '35', 'Manager', 'Tokyo'],
        ['Diana', '28', 'Analyst', 'Paris']
    ]
    csv_headers = ['Name', 'Age', 'Role', 'City']
    
    # Demonstrate operations
    operations = [
        ("Basic file writing", lambda: file_ops.write_file("demo.txt", sample_text)),
        ("File reading", lambda: file_ops.read_file("demo.txt")),
        ("File appending", lambda: file_ops.append_to_file("demo.txt", "\nAppended content!")),
        ("JSON writing", lambda: file_ops.write_json("demo.json", sample_json_data)),
        ("JSON reading", lambda: file_ops.read_json("demo.json")),
        ("CSV writing", lambda: file_ops.write_csv("demo.csv", sample_csv_data, csv_headers)),
        ("CSV reading", lambda: file_ops.read_csv("demo.csv")),
        ("File copying", lambda: file_ops.copy_file("demo.txt", "demo_copy.txt")),
        ("File information", lambda: file_ops.get_file_info("demo.txt")),
        ("Directory listing", lambda: file_ops.list_files()),
        ("Operations summary", lambda: file_ops.get_operations_summary())
    ]
    
    for operation_name, operation_func in operations:
        print(f"\n{'='*50}")
        print(f"DEMONSTRATING: {operation_name.upper()}")
        print('='*50)
        
        try:
            result = operation_func()
            print("✅ Operation completed successfully")
        except Exception as e:
            print(f"❌ Error in {operation_name}: {e}")

if __name__ == "__main__":
    """
    Main execution demonstrating comprehensive file operations
    """
    print(__doc__)
    
    # Educational content
    explain_file_operations_theory()
    
    # Comprehensive demonstration
    demonstrate_all_operations()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Complete file operations mastery")
    print("✅ Professional error handling and logging")
    print("✅ Structured data formats (JSON, CSV)")
    print("✅ File management and metadata handling")
    print("✅ Performance monitoring and optimization")
    print("✅ Cross-platform compatibility considerations")
    
    print("\n💡 Key Concepts Mastered:")
    print("• All file modes and their appropriate usage")
    print("• Robust error handling and recovery strategies")
    print("• Structured data serialization and parsing")
    print("• File system operations and metadata management")
    print("• Performance measurement and optimization")
    print("• Professional logging and operation tracking")
    
    print("\n🎯 Advanced Topics to Explore:")
    print("• Memory-mapped files for large datasets")
    print("• Asynchronous file operations")
    print("• File compression and archiving")
    print("• Database integration for structured data")
    print("• Network file operations and protocols")
    print("• File system watching and event handling")
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"Content of demofile.txt:\n{content}")
    except FileNotFoundError:
        print("demofile.txt not found!")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Reading line by line using readline()
    print("2. READING LINE BY LINE:")
    try:
        with open(file_path, 'r') as f:
            line1 = f.readline()
            line2 = f.readline()
            print(f"First line: {line1.strip()}")
            print(f"Second line: {line2.strip()}")
    except FileNotFoundError:
        print("File not found for line reading!")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Writing to a file
    print("3. WRITING TO A FILE:")
    write_file_path = os.path.join(current_dir, "output.txt")
    try:
        with open(write_file_path, 'w') as f:
            f.write("Hello, this is a new file!\n")
            f.write("This demonstrates file writing in Python.\n")
            f.write("Current timestamp: " + str(__import__('datetime').datetime.now()) + "\n")
        print(f"Successfully wrote to {write_file_path}")
        
        # Read back the written content
        with open(write_file_path, 'r') as f:
            written_content = f.read()
            print(f"Content written:\n{written_content}")
    except Exception as e:
        print(f"Error writing file: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Appending to a file
    print("4. APPENDING TO A FILE:")
    try:
        with open(write_file_path, 'a') as f:
            f.write("This line was appended!\n")
            f.write("Append operation completed.\n")
        print("Successfully appended to file")
        
        # Read the updated content
        with open(write_file_path, 'r') as f:
            updated_content = f.read()
            print(f"Updated content:\n{updated_content}")
    except Exception as e:
        print(f"Error appending to file: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 5. Creating a new file with 'x' mode
    print("5. CREATING A NEW FILE:")
    new_file_path = os.path.join(current_dir, "newfile.txt")
    try:
        with open(new_file_path, 'x') as f:
            f.write("This is a newly created file using 'x' mode.\n")
            f.write("This mode creates a file only if it doesn't exist.\n")
        print(f"Successfully created {new_file_path}")
    except FileExistsError:
        print(f"File {new_file_path} already exists! Cannot create with 'x' mode.")
    except Exception as e:
        print(f"Error creating file: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 6. File operations with error handling
    print("6. FILE OPERATIONS WITH ERROR HANDLING:")
    
    def safe_file_operation(filename, mode, operation):
        try:
            with open(filename, mode) as f:
                result = operation(f)
                return result
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except PermissionError:
            return f"Error: Permission denied for '{filename}'"
        except Exception as e:
            return f"Error: {e}"
    
    # Example of safe reading
    result = safe_file_operation(
        file_path, 
        'r', 
        lambda f: f.read()
    )
    print(f"Safe read result: {result[:50]}..." if len(str(result)) > 50 else f"Safe read result: {result}")
    
    print("\n" + "="*50 + "\n")
    
    # 7. Working with file properties
    print("7. FILE PROPERTIES:")
    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            file_modified = os.path.getmtime(file_path)
            print(f"File: {os.path.basename(file_path)}")
            print(f"Size: {file_size} bytes")
            print(f"Last modified: {__import__('datetime').datetime.fromtimestamp(file_modified)}")
        else:
            print("File doesn't exist to check properties")
    except Exception as e:
        print(f"Error checking file properties: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # 8. Listing files in directory
    print("8. LISTING FILES IN DIRECTORY:")
    try:
        files = os.listdir(current_dir)
        print("Files in current directory:")
        for file in files:
            if os.path.isfile(os.path.join(current_dir, file)):
                print(f"  📄 {file}")
            else:
                print(f"  📁 {file}")
    except Exception as e:
        print(f"Error listing directory: {e}")

# Main execution
if __name__ == "__main__":
    demonstrate_file_operations()
    print("\n🎉 File handling demonstration completed!")
    print("\nKey Points:")
    print("- Always use 'with' statement for automatic file closing")
    print("- Handle exceptions properly to avoid crashes")
    print("- Choose appropriate file mode for your operation")
    print("- Use absolute paths when possible to avoid path issues")
