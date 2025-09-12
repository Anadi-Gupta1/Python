# Comprehensive Python File Handling Examples
"""
File Handling in Python

The key function for working with files in Python is the open() function.
The open() function takes two parameters: filename and mode.

File Modes:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist  
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

Text/Binary Modes:
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

import os

def demonstrate_file_operations():
    print("=== Python File Handling Demonstration ===\n")
    
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Reading a file
    print("1. READING A FILE:")
    try:
        file_path = os.path.join(current_dir, "demofile.txt")
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
