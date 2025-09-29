"""
Professional File Deletion Operations
====================================

This module demonstrates safe file deletion operations using Python's
os module with proper error handling and validation.

Author: Anadi Gupta
Date: September 2025
Purpose: Educational demonstration of file deletion with safety checks
"""

import os
import shutil
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def safe_file_delete(file_path):
    """
    Safely delete a file with proper checks and error handling.
    
    Args:
        file_path (str or Path): Path to the file to be deleted
        
    Returns:
        bool: True if deletion successful, False otherwise
    """
    try:
        file_path = Path(file_path)
        
        # Check if file exists
        if not file_path.exists():
            print(f"⚠️  File does not exist: {file_path}")
            return False
        
        # Check if it's actually a file (not a directory)
        if not file_path.is_file():
            print(f"⚠️  Path is not a file: {file_path}")
            return False
        
        # Get file info before deletion
        file_size = file_path.stat().st_size
        print(f"📄 File to delete: {file_path.name}")
        print(f"📊 File size: {file_size} bytes")
        
        # Confirm deletion (in real applications, you might want user input)
        print(f"🗑️  Deleting file: {file_path}")
        
        # Delete the file
        os.remove(file_path)
        
        # Verify deletion
        if not file_path.exists():
            print(f"✅ Successfully deleted: {file_path.name}")
            logging.info(f"File deleted successfully: {file_path}")
            return True
        else:
            print(f"❌ Failed to delete: {file_path.name}")
            return False
            
    except PermissionError:
        print(f"❌ Permission denied: Cannot delete {file_path}")
        logging.error(f"Permission denied deleting: {file_path}")
        return False
    except Exception as e:
        print(f"❌ Error deleting file: {e}")
        logging.error(f"Error deleting file {file_path}: {e}")
        return False

def safe_folder_delete(folder_path):
    """
    Safely delete a folder with proper checks and error handling.
    
    Args:
        folder_path (str or Path): Path to the folder to be deleted
        
    Returns:
        bool: True if deletion successful, False otherwise
    """
    try:
        folder_path = Path(folder_path)
        
        # Check if folder exists
        if not folder_path.exists():
            print(f"⚠️  Folder does not exist: {folder_path}")
            return False
        
        # Check if it's actually a directory
        if not folder_path.is_dir():
            print(f"⚠️  Path is not a directory: {folder_path}")
            return False
        
        print(f"📁 Folder to delete: {folder_path.name}")
        
        # Check if folder is empty
        if any(folder_path.iterdir()):
            print(f"⚠️  Folder is not empty. Use shutil.rmtree() for non-empty folders.")
            # For demonstration, we'll use shutil.rmtree for non-empty folders
            print(f"🗑️  Deleting non-empty folder: {folder_path}")
            shutil.rmtree(folder_path)
        else:
            print(f"🗑️  Deleting empty folder: {folder_path}")
            os.rmdir(folder_path)
        
        # Verify deletion
        if not folder_path.exists():
            print(f"✅ Successfully deleted folder: {folder_path.name}")
            logging.info(f"Folder deleted successfully: {folder_path}")
            return True
        else:
            print(f"❌ Failed to delete folder: {folder_path.name}")
            return False
            
    except PermissionError:
        print(f"❌ Permission denied: Cannot delete {folder_path}")
        logging.error(f"Permission denied deleting folder: {folder_path}")
        return False
    except Exception as e:
        print(f"❌ Error deleting folder: {e}")
        logging.error(f"Error deleting folder {folder_path}: {e}")
        return False

def demonstrate_file_deletion():
    """Demonstrate file and folder deletion with test files"""
    
    print("🚀 Professional File & Folder Deletion Demonstration")
    print("=" * 60)
    
    # Create a test file first
    test_file = Path(__file__).parent / "test_delete_file.txt"
    test_folder = Path(__file__).parent / "test_delete_folder"
    
    try:
        # Create test file
        with open(test_file, "w") as f:
            f.write("This is a test file for deletion demonstration.\n")
            f.write("It will be safely deleted using proper Python practices.\n")
        
        print(f"📝 Created test file: {test_file.name}")
        
        # Create test folder with a file inside
        test_folder.mkdir(exist_ok=True)
        test_sub_file = test_folder / "test_sub_file.txt"
        with open(test_sub_file, "w") as f:
            f.write("This is a file inside the test folder.\n")
        
        print(f"📁 Created test folder: {test_folder.name}")
        print(f"📝 Created file inside folder: {test_sub_file.name}")
        
        print("\n" + "="*30 + " FILE DELETION " + "="*30)
        # Demonstrate safe file deletion
        file_success = safe_file_delete(test_file)
        
        print("\n" + "="*30 + " FOLDER DELETION " + "="*29)
        # Demonstrate safe folder deletion
        folder_success = safe_folder_delete(test_folder)
        
        if file_success and folder_success:
            print("\n✨ File and folder deletion demonstration completed successfully!")
        else:
            print("\n❌ Some deletion operations failed!")
            
    except Exception as e:
        print(f"❌ Error in demonstration: {e}")

def main():
    """Main function"""
    demonstrate_file_deletion()
    
    print("\n📚 Key Points for Safe File/Folder Deletion:")
    print("- Always check if file/folder exists before deletion")
    print("- Verify the path type (file vs directory)")
    print("- Handle permissions and other exceptions")
    print("- Use os.remove() for files")
    print("- Use os.rmdir() for empty folders")
    print("- Use shutil.rmtree() for non-empty folders")
    print("- Log operations for debugging and auditing")
    print("- Consider user confirmation for important files")

if __name__ == "__main__":
    main()
