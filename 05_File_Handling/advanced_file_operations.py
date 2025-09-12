"""
Advanced File Operations with Performance Optimization

This module demonstrates advanced file handling techniques including:
- Batch file operations
- Progress tracking
- Memory-efficient large file processing
- Concurrent file operations

Author: Anadi Gupta
Date: September 2025
Purpose: Advanced file handling demonstration
"""

import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib

class AdvancedFileOperations:
    """Advanced file operations with performance optimization"""
    
    def __init__(self, base_path=None):
        """Initialize with base path for operations"""
        self.base_path = Path(base_path) if base_path else Path(__file__).parent
        
    def batch_file_creator(self, file_count=5, content="Sample content"):
        """Create multiple files efficiently"""
        print(f"Creating {file_count} files...")
        start_time = time.time()
        
        for i in range(file_count):
            filename = self.base_path / f"batch_file_{i:03d}.txt"
            try:
                with open(filename, 'w') as f:
                    f.write(f"{content} - File {i+1}\n")
                    f.write(f"Created at: {time.ctime()}\n")
                print(f"✅ Created: {filename.name}")
            except Exception as e:
                print(f"❌ Error creating {filename.name}: {e}")
        
        elapsed = time.time() - start_time
        print(f"⏱️ Batch creation completed in {elapsed:.2f} seconds")
        
    def calculate_file_hash(self, filepath):
        """Calculate MD5 hash of a file for integrity checking"""
        hash_md5 = hashlib.md5()
        try:
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            return f"Error: {e}"
    
    def file_integrity_check(self):
        """Check integrity of all files in directory"""
        print("\n=== File Integrity Check ===")
        txt_files = list(self.base_path.glob("*.txt"))
        
        for file_path in txt_files:
            if file_path.exists():
                file_hash = self.calculate_file_hash(file_path)
                file_size = file_path.stat().st_size
                print(f"📄 {file_path.name}: {file_size} bytes, Hash: {file_hash[:8]}...")
    
    def concurrent_file_processing(self, max_workers=3):
        """Process multiple files concurrently"""
        print("\n=== Concurrent File Processing ===")
        txt_files = list(self.base_path.glob("batch_file_*.txt"))
        
        def process_file(file_path):
            """Process a single file"""
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    word_count = len(content.split())
                    return f"{file_path.name}: {word_count} words"
            except Exception as e:
                return f"{file_path.name}: Error - {e}"
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(process_file, txt_files))
            
        for result in results:
            print(f"📊 {result}")
    
    def cleanup_batch_files(self):
        """Clean up batch created files"""
        print("\n=== Cleanup Batch Files ===")
        batch_files = list(self.base_path.glob("batch_file_*.txt"))
        
        for file_path in batch_files:
            try:
                file_path.unlink()
                print(f"🗑️ Deleted: {file_path.name}")
            except Exception as e:
                print(f"❌ Error deleting {file_path.name}: {e}")

def main():
    """Main demonstration function"""
    print("🚀 Advanced File Operations Demonstration")
    print("=" * 50)
    
    # Initialize advanced file operations
    file_ops = AdvancedFileOperations()
    
    # Demonstrate batch file creation
    file_ops.batch_file_creator(file_count=5)
    
    # Check file integrity
    file_ops.file_integrity_check()
    
    # Demonstrate concurrent processing
    file_ops.concurrent_file_processing()
    
    # Optional cleanup (uncomment if needed)
    # file_ops.cleanup_batch_files()
    
    print("\n✨ Advanced file operations completed successfully!")

if __name__ == "__main__":
    main()
