"""
File Reading Examples - Comprehensive File Input Operations
=========================================================

Advanced file reading techniques demonstrating various methods, error handling,
encoding support, performance optimization, and practical applications for
different file types and reading scenarios.

Author: Python Learning Notes
Date: September 2025
Topic: File Reading, Text Processing, Error Handling, Performance
"""

import os
import sys
import time
import mimetypes
from pathlib import Path
from typing import List, Optional, Generator, Dict, Any
import csv
import json

# =============================================================================
# FILE READING CONCEPTS AND THEORY
# =============================================================================

def explain_file_reading_concepts():
    """
    Educational explanation of file reading concepts and best practices
    """
    print("📖 FILE READING CONCEPTS")
    print("=" * 25)
    
    print("\n📚 Why Learn File Reading?")
    print("File reading is essential for:")
    print("   • Data processing and analysis")
    print("   • Configuration file parsing")
    print("   • Log file analysis and monitoring")
    print("   • Document processing and text analysis")
    print("   • Importing data from external sources")
    
    print("\n🔄 Reading Methods Comparison:")
    methods = [
        ("read()", "Entire file", "Small files", "High memory usage"),
        ("readline()", "Single line", "Line processing", "Memory efficient"),
        ("readlines()", "All lines as list", "Line manipulation", "Moderate memory"),
        ("Iterator", "Line by line", "Large files", "Very efficient"),
        ("read(size)", "Fixed chunks", "Binary/large files", "Controlled memory")
    ]
    
    print("   ┌─────────────┬─────────────────┬─────────────────┬─────────────────┐")
    print("   │ Method      │ Reads           │ Best For        │ Memory Impact   │")
    print("   ├─────────────┼─────────────────┼─────────────────┼─────────────────┤")
    for method, reads, best_for, memory in methods:
        print(f"   │ {method:<11} │ {reads:<15} │ {best_for:<15} │ {memory:<15} │")
    print("   └─────────────┴─────────────────┴─────────────────┴─────────────────┘")
    
    print("\n⚠️  Common Reading Challenges:")
    print("   • Encoding issues (UTF-8, ASCII, etc.)")
    print("   • Large file memory consumption")
    print("   • File locking and permissions")
    print("   • Cross-platform path handling")
    print("   • Binary vs text file detection")

# =============================================================================
# BASIC FILE READING METHODS
# =============================================================================

class FileReader:
    """
    Comprehensive file reading utility with various methods
    """
    
    def __init__(self, base_path: str = None):
        """Initialize file reader with optional base path"""
        self.base_path = Path(base_path) if base_path else Path.cwd()
        
    def read_entire_file(self, filename: str, encoding: str = 'utf-8') -> Optional[str]:
        """
        Read entire file content at once
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default utf-8)
            
        Returns:
            str: File content or None if error
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found in {self.base_path}")
                return None
            
            print(f"\n📖 Reading Entire File: '{filename}'")
            print("=" * 30)
            
            file_size = filepath.stat().st_size
            print(f"   File size: {file_size:,} bytes")
            print(f"   Using encoding: {encoding}")
            
            start_time = time.time()
            
            with open(filepath, 'r', encoding=encoding) as file:
                content = file.read()
            
            read_time = (time.time() - start_time) * 1000
            
            print(f"   Characters read: {len(content):,}")
            print(f"   Lines: {content.count(chr(10)) + 1}")
            print(f"   Read time: {read_time:.2f} ms")
            print(f"   ✅ File read successfully")
            
            # Show preview
            preview_length = min(200, len(content))
            preview = content[:preview_length]
            if len(content) > preview_length:
                preview += "..."
            
            print(f"\n   📝 Content Preview:")
            print(f"   {repr(preview)}")
            
            return content
            
        except UnicodeDecodeError as e:
            print(f"   ❌ Encoding error: {e}")
            print("   💡 Try specifying a different encoding")
            return None
        except Exception as e:
            print(f"   ❌ Error reading file: {e}")
            return None
    
    def read_line_by_line(self, filename: str, encoding: str = 'utf-8',
                         max_lines: int = None) -> List[str]:
        """
        Read file line by line for memory efficiency
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default utf-8)
            max_lines: Maximum lines to read (None for all)
            
        Returns:
            List[str]: List of lines
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return []
            
            print(f"\n📄 Reading Line by Line: '{filename}'")
            print("=" * 30)
            
            lines = []
            line_count = 0
            
            with open(filepath, 'r', encoding=encoding) as file:
                for line_num, line in enumerate(file, 1):
                    lines.append(line.rstrip('\n\r'))
                    line_count += 1
                    
                    # Show progress for large files
                    if line_count % 1000 == 0:
                        print(f"   Read {line_count:,} lines...")
                    
                    # Stop if max_lines reached
                    if max_lines and line_count >= max_lines:
                        print(f"   Stopped at {max_lines:,} lines (limit reached)")
                        break
            
            print(f"   ✅ Read {len(lines):,} lines")
            
            # Show sample lines
            if lines:
                print(f"\n   📝 Sample Lines:")
                sample_size = min(5, len(lines))
                for i in range(sample_size):
                    line_preview = lines[i][:80]
                    if len(lines[i]) > 80:
                        line_preview += "..."
                    print(f"   Line {i+1:3}: {repr(line_preview)}")
                
                if len(lines) > sample_size:
                    print(f"   ... and {len(lines) - sample_size} more lines")
            
            return lines
            
        except Exception as e:
            print(f"   ❌ Error reading file line by line: {e}")
            return []
    
    def read_in_chunks(self, filename: str, chunk_size: int = 1024,
                      encoding: str = 'utf-8') -> Generator[str, None, None]:
        """
        Read file in chunks for memory-efficient processing
        
        Args:
            filename: Name of file to read
            chunk_size: Size of each chunk in bytes
            encoding: File encoding
            
        Yields:
            str: File chunks
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return
            
            print(f"\n🧩 Reading in Chunks: '{filename}'")
            print("=" * 25)
            print(f"   Chunk size: {chunk_size:,} bytes")
            
            chunk_count = 0
            total_bytes = 0
            
            with open(filepath, 'r', encoding=encoding) as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    
                    chunk_count += 1
                    total_bytes += len(chunk.encode(encoding))
                    
                    print(f"   Chunk {chunk_count}: {len(chunk):,} characters")
                    
                    yield chunk
            
            print(f"   ✅ Processed {chunk_count} chunks, {total_bytes:,} total bytes")
            
        except Exception as e:
            print(f"   ❌ Error reading file in chunks: {e}")
    
    def read_specific_lines(self, filename: str, line_numbers: List[int],
                           encoding: str = 'utf-8') -> Dict[int, str]:
        """
        Read specific lines from file by line numbers
        
        Args:
            filename: Name of file to read
            line_numbers: List of line numbers to read (1-indexed)
            encoding: File encoding
            
        Returns:
            Dict[int, str]: Dictionary mapping line numbers to content
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return {}
            
            print(f"\n🎯 Reading Specific Lines: '{filename}'")
            print("=" * 30)
            print(f"   Target lines: {sorted(line_numbers)}")
            
            result = {}
            target_lines = set(line_numbers)
            
            with open(filepath, 'r', encoding=encoding) as file:
                for current_line_num, line in enumerate(file, 1):
                    if current_line_num in target_lines:
                        result[current_line_num] = line.rstrip('\n\r')
                        print(f"   Found line {current_line_num}: {len(line):,} characters")
                        
                        # Remove from target set for efficiency
                        target_lines.remove(current_line_num)
                        
                        # Stop if all lines found
                        if not target_lines:
                            break
            
            # Report missing lines
            missing_lines = set(line_numbers) - set(result.keys())
            if missing_lines:
                print(f"   ⚠️ Lines not found: {sorted(missing_lines)}")
            
            print(f"   ✅ Retrieved {len(result)}/{len(line_numbers)} requested lines")
            
            return result
            
        except Exception as e:
            print(f"   ❌ Error reading specific lines: {e}")
            return {}

# =============================================================================
# ADVANCED READING TECHNIQUES
# =============================================================================

class AdvancedFileReader(FileReader):
    """
    Advanced file reading with specialized methods
    """
    
    def read_with_progress(self, filename: str, encoding: str = 'utf-8') -> Optional[str]:
        """
        Read file with progress indication for large files
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return None
            
            file_size = filepath.stat().st_size
            
            print(f"\n⏳ Reading with Progress: '{filename}'")
            print("=" * 30)
            print(f"   File size: {file_size:,} bytes")
            
            content_parts = []
            bytes_read = 0
            chunk_size = max(8192, file_size // 100)  # 1% chunks
            
            with open(filepath, 'r', encoding=encoding) as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    
                    content_parts.append(chunk)
                    bytes_read += len(chunk.encode(encoding))
                    
                    progress = (bytes_read / file_size) * 100
                    print(f"   Progress: {progress:.1f}% ({bytes_read:,}/{file_size:,} bytes)")
            
            content = ''.join(content_parts)
            print(f"   ✅ Reading completed: {len(content):,} characters")
            
            return content
            
        except Exception as e:
            print(f"   ❌ Error reading with progress: {e}")
            return None
    
    def read_and_analyze(self, filename: str, encoding: str = 'utf-8') -> Dict[str, Any]:
        """
        Read file and perform basic analysis
        
        Args:
            filename: Name of file to read and analyze
            encoding: File encoding
            
        Returns:
            Dict containing file content and analysis
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"❌ File '{filename}' not found")
                return {}
            
            print(f"\n🔬 Reading and Analyzing: '{filename}'")
            print("=" * 30)
            
            # Read content
            with open(filepath, 'r', encoding=encoding) as file:
                content = file.read()
            
            # Perform analysis
            analysis = {
                'content': content,
                'file_size_bytes': len(content.encode(encoding)),
                'character_count': len(content),
                'line_count': content.count('\n') + 1,
                'word_count': len(content.split()),
                'encoding': encoding,
                'longest_line': max(content.splitlines(), key=len, default=""),
                'shortest_line': min(content.splitlines(), key=len, default=""),
                'empty_lines': content.count('\n\n'),
                'unique_characters': len(set(content))
            }
            
            # Character frequency analysis (top 10)
            char_freq = {}
            for char in content:
                if char.isprintable():
                    char_freq[char] = char_freq.get(char, 0) + 1
            
            top_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10]
            analysis['top_characters'] = top_chars
            
            # Display analysis
            print(f"   📊 File Analysis Results:")
            print(f"   • File size: {analysis['file_size_bytes']:,} bytes")
            print(f"   • Characters: {analysis['character_count']:,}")
            print(f"   • Lines: {analysis['line_count']:,}")
            print(f"   • Words: {analysis['word_count']:,}")
            print(f"   • Encoding: {analysis['encoding']}")
            print(f"   • Longest line: {len(analysis['longest_line']):,} chars")
            print(f"   • Unique characters: {analysis['unique_characters']:,}")
            
            return analysis
            
        except Exception as e:
            print(f"   ❌ Error during analysis: {e}")
            return {}
    
    def safe_read_with_fallbacks(self, filename: str) -> Optional[str]:
        """
        Attempt to read file with multiple encoding fallbacks
        
        Args:
            filename: Name of file to read
            
        Returns:
            str: File content or None if all attempts fail
        """
        filepath = self.base_path / filename
        
        if not filepath.exists():
            print(f"❌ File '{filename}' not found")
            return None
        
        print(f"\n🛡️  Safe Reading with Fallbacks: '{filename}'")
        print("=" * 35)
        
        # Common encodings to try
        encodings_to_try = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252', 'ascii']
        
        for encoding in encodings_to_try:
            try:
                print(f"   Trying encoding: {encoding}")
                
                with open(filepath, 'r', encoding=encoding) as file:
                    content = file.read()
                
                print(f"   ✅ Success with {encoding}")
                print(f"   Characters read: {len(content):,}")
                
                return content
                
            except UnicodeDecodeError as e:
                print(f"   ❌ Failed with {encoding}: {str(e)[:50]}...")
                continue
            except Exception as e:
                print(f"   ❌ Error with {encoding}: {e}")
                continue
        
        print("   ❌ All encoding attempts failed")
        return None

# =============================================================================
# SPECIALIZED FILE READERS
# =============================================================================

def read_csv_file(filename: str) -> Optional[List[List[str]]]:
    """
    Specialized CSV file reader with error handling
    """
    try:
        print(f"\n📊 Reading CSV File: '{filename}'")
        print("=" * 20)
        
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            rows = []
            row_count = 0
            
            for row_num, row in enumerate(csv_reader, 1):
                rows.append(row)
                row_count += 1
                
                if row_num == 1:
                    print(f"   Columns detected: {len(row)}")
                    print(f"   Headers: {row[:5]}...")  # Show first 5 headers
            
            print(f"   ✅ Read {row_count:,} rows")
            
            return rows
            
    except Exception as e:
        print(f"   ❌ CSV reading error: {e}")
        return None

def read_json_file(filename: str) -> Optional[Dict]:
    """
    Specialized JSON file reader with validation
    """
    try:
        print(f"\n🔗 Reading JSON File: '{filename}'")
        print("=" * 20)
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(f"   ✅ JSON parsed successfully")
        
        if isinstance(data, dict):
            print(f"   Top-level keys: {list(data.keys())}")
        elif isinstance(data, list):
            print(f"   Array with {len(data)} elements")
        
        return data
        
    except json.JSONDecodeError as e:
        print(f"   ❌ JSON parsing error: {e}")
        return None
    except Exception as e:
        print(f"   ❌ File reading error: {e}")
        return None

# =============================================================================
# PERFORMANCE TESTING
# =============================================================================

def compare_reading_methods(filename: str) -> Dict[str, float]:
    """
    Compare performance of different reading methods
    """
    print(f"\n⏱️  Performance Comparison: '{filename}'")
    print("=" * 30)
    
    reader = AdvancedFileReader()
    results = {}
    
    methods = [
        ("read_entire_file", lambda: reader.read_entire_file(filename)),
        ("read_line_by_line", lambda: reader.read_line_by_line(filename)),
        ("safe_read_fallbacks", lambda: reader.safe_read_with_fallbacks(filename))
    ]
    
    for method_name, method_func in methods:
        try:
            start_time = time.time()
            result = method_func()
            end_time = time.time()
            
            duration = (end_time - start_time) * 1000  # Convert to milliseconds
            results[method_name] = duration
            
            status = "✅" if result else "❌"
            print(f"   {status} {method_name}: {duration:.2f} ms")
            
        except Exception as e:
            results[method_name] = float('inf')
            print(f"   ❌ {method_name}: Error - {e}")
    
    # Find fastest method
    if results:
        fastest_method = min(results.items(), key=lambda x: x[1])
        print(f"\n   🏆 Fastest method: {fastest_method[0]} ({fastest_method[1]:.2f} ms)")
    
    return results

# =============================================================================
# INTERACTIVE FILE READER
# =============================================================================

def interactive_file_reader():
    """
    Interactive file reading tool with multiple options
    """
    print(f"\n🎮 INTERACTIVE FILE READER")
    print("=" * 25)
    
    reader = AdvancedFileReader()
    
    while True:
        try:
            print(f"\n🎯 Choose a reading method:")
            print("   1. Read entire file")
            print("   2. Read line by line")
            print("   3. Read in chunks")
            print("   4. Read specific lines")
            print("   5. Read with progress indicator")
            print("   6. Read and analyze content")
            print("   7. Safe read with encoding fallbacks")
            print("   8. Read CSV file")
            print("   9. Read JSON file")
            print("   10. Compare reading methods")
            print("   11. Learn about file reading")
            print("   12. Exit")
            
            choice = input("\nEnter your choice (1-12): ").strip()
            
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                filename = input("Enter filename: ").strip()
                
                if choice == "1":
                    content = reader.read_entire_file(filename)
                elif choice == "2":
                    max_lines = input("Max lines (press Enter for all): ").strip()
                    max_lines = int(max_lines) if max_lines else None
                    lines = reader.read_line_by_line(filename, max_lines=max_lines)
                elif choice == "3":
                    chunk_size = input("Chunk size in bytes (default 1024): ").strip()
                    chunk_size = int(chunk_size) if chunk_size else 1024
                    chunk_count = 0
                    for chunk in reader.read_in_chunks(filename, chunk_size):
                        chunk_count += 1
                        if chunk_count > 5:  # Limit display
                            print("   ... (truncated for display)")
                            break
                elif choice == "4":
                    line_nums = input("Enter line numbers (comma-separated): ").strip()
                    line_numbers = [int(x.strip()) for x in line_nums.split(',')]
                    result = reader.read_specific_lines(filename, line_numbers)
                    for line_num, content in result.items():
                        preview = content[:100] + "..." if len(content) > 100 else content
                        print(f"   Line {line_num}: {repr(preview)}")
                elif choice == "5":
                    content = reader.read_with_progress(filename)
                elif choice == "6":
                    analysis = reader.read_and_analyze(filename)
                elif choice == "7":
                    content = reader.safe_read_with_fallbacks(filename)
                    
            elif choice == "8":
                filename = input("Enter CSV filename: ").strip()
                rows = read_csv_file(filename)
                if rows:
                    print(f"   Preview (first 3 rows):")
                    for i, row in enumerate(rows[:3]):
                        print(f"   Row {i+1}: {row}")
                        
            elif choice == "9":
                filename = input("Enter JSON filename: ").strip()
                data = read_json_file(filename)
                if data:
                    print(f"   JSON structure: {type(data).__name__}")
                    
            elif choice == "10":
                filename = input("Enter filename for performance test: ").strip()
                compare_reading_methods(filename)
                
            elif choice == "11":
                explain_file_reading_concepts()
                
            elif choice == "12":
                print("\n👋 Thanks for exploring file reading!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-12.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# =============================================================================
# DEMONSTRATION AND MAIN EXECUTION
# =============================================================================

def create_sample_files():
    """Create sample files for demonstration"""
    print("🔧 Creating sample files for demonstration...")
    
    # Create a simple text file
    with open("demofile.txt", 'w', encoding='utf-8') as f:
        f.write("Hello World!\n")
        f.write("This is a sample file.\n")
        f.write("Created for demonstration purposes.\n")
        f.write("Line 4 with some special characters: àáâãäå\n")
        f.write("Final line with numbers: 12345\n")
    
    # Create a CSV file
    with open("sample.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', '25', 'New York'])
        writer.writerow(['Bob', '30', 'London'])
        writer.writerow(['Charlie', '35', 'Tokyo'])
    
    # Create a JSON file
    sample_data = {
        'name': 'File Reading Demo',
        'version': 1.0,
        'features': ['text reading', 'CSV parsing', 'JSON handling'],
        'config': {'encoding': 'utf-8', 'buffer_size': 1024}
    }
    
    with open("sample.json", 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2)
    
    print("✅ Sample files created successfully!")

def demonstrate_all_reading_methods():
    """Demonstrate all file reading methods"""
    print("\n" + "="*60)
    print("FILE READING METHODS DEMONSTRATION")
    print("="*60)
    
    # Create sample files
    create_sample_files()
    
    reader = AdvancedFileReader()
    
    # Demonstrate each method
    methods = [
        ("Basic file reading", lambda: reader.read_entire_file("demofile.txt")),
        ("Line by line reading", lambda: reader.read_line_by_line("demofile.txt")),
        ("Specific lines reading", lambda: reader.read_specific_lines("demofile.txt", [1, 3, 5])),
        ("Analysis reading", lambda: reader.read_and_analyze("demofile.txt")),
        ("CSV reading", lambda: read_csv_file("sample.csv")),
        ("JSON reading", lambda: read_json_file("sample.json"))
    ]
    
    for method_name, method_func in methods:
        print(f"\n{'='*50}")
        print(f"DEMONSTRATING: {method_name.upper()}")
        print('='*50)
        
        try:
            result = method_func()
            if result:
                print("✅ Method executed successfully")
        except Exception as e:
            print(f"❌ Error in {method_name}: {e}")

if __name__ == "__main__":
    """
    Main execution demonstrating file reading concepts and methods
    """
    print(__doc__)
    
    # Educational content
    explain_file_reading_concepts()
    
    # Create sample files and demonstrate
    demonstrate_all_reading_methods()
    
    # Performance comparison
    if Path("demofile.txt").exists():
        compare_reading_methods("demofile.txt")
    
    # Interactive tool
    interactive_file_reader()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Comprehensive file reading techniques and methods")
    print("✅ Encoding detection and handling strategies")
    print("✅ Memory-efficient reading for large files")
    print("✅ Error handling and fallback mechanisms")
    print("✅ Performance optimization and comparison")
    print("✅ Specialized readers for structured data")
    
    print("\n💡 Key Concepts Learned:")
    print("• Different reading methods and their use cases")
    print("• Encoding issues and automatic detection")
    print("• Memory management for large files")
    print("• Progress tracking and user feedback")
    print("• Robust error handling and recovery")
    print("• Performance measurement and optimization")
    
    print("\n🎯 Next Steps:")
    print("• Study memory-mapped files for very large datasets")
    print("• Explore async file reading for concurrent operations")
    print("• Learn about streaming parsers for XML/JSON")
    print("• Master binary file reading and protocol parsing")
    print("• Investigate file watching and real-time processing")