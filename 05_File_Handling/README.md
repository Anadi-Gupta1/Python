# 📁 05_File_Handling

This directory contains Python programs demonstrating various file handling operations and techniques with professional-grade implementations.

## 📄 Files Overview

| File | Description | Features |
|------|-------------|----------|
| [`file_reading_examples.py`](file_reading_examples.py) | Basic file reading with error handling | Multiple reading methods, path resolution, exception handling |
| [`comprehensive_file_operations.py`](comprehensive_file_operations.py) | Complete file operations demonstration | Read, write, append, create, file properties |
| [`append_and_write.py`](append_and_write.py) | Professional file writing and appending | Advanced error handling, logging, best practices |
| [`python_file_opener.py`](python_file_opener.py) | Professional file opening operations | Multiple opening methods, security features |
| [`advanced_file_operations.py`](advanced_file_operations.py) | Advanced file processing | Batch operations, concurrent processing, hashing |
| [`simple_file_writer.py`](simple_file_writer.py) | Basic file writing demonstration | Simple file creation, context managers |
| [`safe_file_operations.py`](safe_file_operations.py) | Safe file and folder deletion | Secure deletion with validation, error handling |
| [`demofile.txt`](demofile.txt) | Sample text file for testing | Test data for file operations |
| [`SECURITY.md`](SECURITY.md) | Security guidelines for file operations | Best practices, security considerations |

## 🔧 Generated Files

These files are created automatically when running the programs:
- `output.txt` - Created by write operations
- `newfile.txt` - Created using 'x' mode
- `file_operations.log` - Logging output from operations

## 🚀 How to Run

```bash
# Navigate to the directory
cd 05_File_Handling

# Run basic file reading examples
python file_reading_examples.py

# Run comprehensive file operations
python comprehensive_file_operations.py
```

## 📚 Learning Objectives

- **File Opening Modes**: Understand 'r', 'w', 'a', 'x' modes
- **Error Handling**: Proper exception handling for file operations
- **Context Managers**: Using 'with' statement for safe file operations
- **Path Management**: Working with absolute and relative paths
- **File Properties**: Checking file size, modification time, existence

## 🛡️ Key Concepts

### File Modes
- `'r'` - Read (default)
- `'w'` - Write (overwrites existing content)
- `'a'` - Append (adds to end of file)
- `'x'` - Create (fails if file exists)
- `'b'` - Binary mode
- `'t'` - Text mode (default)

### Best Practices
- Always use `with` statement for automatic file closing
- Handle exceptions properly to prevent crashes
- Use absolute paths when possible
- Check file existence before operations
- Close files properly to prevent resource leaks

## 🎯 Example Output

When you run the programs, you'll see demonstrations of:
- Reading file content in different ways
- Writing new files
- Appending to existing files
- Handling file errors gracefully
- Working with file properties and metadata
