"""
Python File Deletion Operations - Learning Notes
===============================================

This module demonstrates various methods for deleting files and folders in Python.
Essential for file management and cleanup operations.

Author: Python Learning Notes
Date: September 2025
Topic: File Deletion & Management
"""

import os

def delete_file_basic():
    """
    Basic file deletion method
    WARNING: This will delete the file without confirmation
    """
    print("=== Basic File Deletion ===")
    try:
        # Basic deletion - USE WITH CAUTION
        os.remove("demofile.txt")
        print("✅ File deleted successfully")
    except FileNotFoundError:
        print("❌ File not found - cannot delete")
    except PermissionError:
        print("❌ Permission denied - cannot delete file")

def delete_file_safe():
    """
    Safe file deletion with existence check
    RECOMMENDED approach for file deletion
    """
    print("\n=== Safe File Deletion (Recommended) ===")
    filename = "demofile.txt"
    
    # Check if file exists before attempting deletion
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"✅ File '{filename}' deleted successfully")
        except PermissionError:
            print(f"❌ Permission denied - cannot delete '{filename}'")
        except Exception as e:
            print(f"❌ Error deleting file: {e}")
    else:
        print(f"ℹ️  File '{filename}' does not exist")

def delete_folder():
    """
    Delete empty folders using os.rmdir()
    NOTE: Can only remove empty folders
    """
    print("\n=== Folder Deletion ===")
    folder_name = "myfolder"
    
    try:
        if os.path.exists(folder_name):
            os.rmdir(folder_name)
            print(f"✅ Folder '{folder_name}' deleted successfully")
        else:
            print(f"ℹ️  Folder '{folder_name}' does not exist")
    except OSError as e:
        print(f"❌ Error deleting folder: {e}")
        print("💡 Tip: Folder must be empty to delete with rmdir()")

def delete_folder_with_contents():
    """
    Delete folder and all its contents using shutil
    DANGER: This will delete everything inside the folder
    """
    import shutil
    print("\n=== Delete Folder with Contents (DANGEROUS) ===")
    folder_name = "test_folder"
    
    try:
        if os.path.exists(folder_name):
            # Ask for confirmation before deleting
            confirm = input(f"⚠️  Delete '{folder_name}' and ALL its contents? (yes/no): ")
            if confirm.lower() == 'yes':
                shutil.rmtree(folder_name)
                print(f"✅ Folder '{folder_name}' and contents deleted")
            else:
                print("❌ Deletion cancelled")
        else:
            print(f"ℹ️  Folder '{folder_name}' does not exist")
    except Exception as e:
        print(f"❌ Error: {e}")

def demonstrate_deletion_methods():
    """
    Demonstrate all deletion methods with examples
    """
    print("🗑️  PYTHON FILE DELETION METHODS - DEMONSTRATION")
    print("=" * 50)
    
    # Create test files for demonstration
    print("📝 Creating test files...")
    with open("test_file1.txt", "w") as f:
        f.write("This is a test file for deletion demo")
    
    with open("test_file2.txt", "w") as f:
        f.write("Another test file")
    
    # Create test folder
    os.makedirs("test_folder", exist_ok=True)
    
    print("✅ Test files created")
    
    # Demonstrate safe deletion
    delete_file_safe()
    
    # List remaining files
    print(f"\n📁 Current directory contents:")
    for item in os.listdir('.'):
        if item.startswith('test_'):
            print(f"  - {item}")

if __name__ == "__main__":
    """
    Main execution block for testing deletion methods
    """
    print(__doc__)
    
    # Uncomment to run demonstrations
    # demonstrate_deletion_methods()
    
    print("\n📚 LEARNING POINTS:")
    print("1. Always check if file exists before deleting")
    print("2. Use try-except blocks for error handling")
    print("3. os.remove() for files, os.rmdir() for empty folders")
    print("4. shutil.rmtree() for folders with contents (DANGEROUS)")
    print("5. Be very careful with deletion operations!")
    
    print("\n⚠️  SAFETY REMINDER:")
    print("File deletion is PERMANENT! Always backup important files.")

if os.path.exists("myfolder"):
    os.rmdir("myfolder")
    else:
    print("The folder does not exist")