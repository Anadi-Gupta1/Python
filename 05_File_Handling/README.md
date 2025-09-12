# 📁 05_File_Handling

This directory contains Python programs demonstrating various file handling operations and techniques.

## 📄 Files Overview

| File | Description | Features |
|------|-------------|----------|
| [`file_reading_examples.py`](file_reading_examples.py) | Basic file reading with error handling | Multiple reading methods, path resolution, exception handling |
| [`comprehensive_file_operations.py`](comprehensive_file_operations.py) | Complete file operations demonstration | Read, write, append, create, file properties |
| [`demofile.txt`](demofile.txt) | Sample text file for testing | Test data for file operations |

## 🔧 Generated Files

These files are created automatically when running the programs:
- `output.txt` - Created by write operations
- `newfile.txt` - Created using 'x' mode

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
