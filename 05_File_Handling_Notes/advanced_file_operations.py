"""
Advanced File Operations - Complex File Handling and Management
============================================================

Comprehensive file handling system demonstrating advanced operations including
binary files, CSV/JSON handling, file compression, encryption basics, and
enterprise-level file management patterns with robust error handling.

Author: Python Learning Notes
Date: September 2025
Topic: Advanced File I/O, Binary Operations, Data Serialization, File Security
"""

import os
import csv
import json
import pickle
import gzip
import shutil
import hashlib
import mimetypes
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Union, Generator
import base64
import threading
import concurrent.futures

# =============================================================================
# ADVANCED FILE CONCEPTS AND THEORY
# =============================================================================

def explain_advanced_file_concepts():
    """
    Educational explanation of advanced file handling concepts
    """
    print("💾 ADVANCED FILE HANDLING CONCEPTS")
    print("=" * 35)
    
    print("\n📚 Beyond Basic File Operations:")
    print("Advanced file handling includes:")
    print("   • Binary file operations and data structures")
    print("   • Serialization and deserialization (pickle, JSON)")
    print("   • File compression and decompression")
    print("   • File encryption and security measures")
    print("   • Concurrent file operations and locking")
    print("   • Memory-mapped files for large datasets")
    print("   • Temporary files and directories")
    
    print("\n🔄 File Types and Formats:")
    file_types = [
        ("Text Files", ".txt, .csv, .json", "Human-readable, encoding-dependent"),
        ("Binary Files", ".exe, .jpg, .pdf", "Machine-readable, raw bytes"),
        ("Structured Data", ".xml, .yaml, .ini", "Hierarchical data formats"),
        ("Compressed Files", ".zip, .gz, .bz2", "Space-efficient storage"),
        ("Database Files", ".db, .sqlite", "Structured data storage")
    ]
    
    print("   ┌─────────────────┬─────────────────┬─────────────────────────┐")
    print("   │ Type            │ Extensions      │ Description             │")
    print("   ├─────────────────┼─────────────────┼─────────────────────────┤")
    for file_type, ext, desc in file_types:
        print(f"   │ {file_type:<15} │ {ext:<15} │ {desc:<23} │")
    print("   └─────────────────┴─────────────────┴─────────────────────────┘")
    
    print("\n🔐 File Security Considerations:")
    print("   • File permissions and access control")
    print("   • Data encryption for sensitive information")
    print("   • Integrity checking with checksums/hashes")
    print("   • Secure deletion and data wiping")
    print("   • Backup and recovery strategies")

# =============================================================================
# BINARY FILE OPERATIONS
# =============================================================================

class BinaryFileHandler:
    """
    Advanced binary file operations handler
    """
    
    def __init__(self, base_path: str = "binary_files"):
        """Initialize with base directory for binary files"""
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
        
    def write_binary_data(self, filename: str, data: bytes, 
                         show_progress: bool = True) -> bool:
        """
        Write binary data to file with progress tracking
        
        Args:
            filename: Target filename
            data: Binary data to write
            show_progress: Whether to show write progress
            
        Returns:
            bool: Success status
        """
        try:
            filepath = self.base_path / filename
            
            print(f"\n💾 Writing Binary Data to '{filename}'")
            print("=" * 35)
            print(f"   Target: {filepath}")
            print(f"   Data size: {len(data):,} bytes")
            
            with open(filepath, 'wb') as file:
                if show_progress and len(data) > 1000:
                    # Write in chunks with progress
                    chunk_size = 1024
                    chunks_written = 0
                    total_chunks = (len(data) + chunk_size - 1) // chunk_size
                    
                    for i in range(0, len(data), chunk_size):
                        chunk = data[i:i + chunk_size]
                        file.write(chunk)
                        chunks_written += 1
                        
                        if chunks_written % 10 == 0 or chunks_written == total_chunks:
                            progress = (chunks_written / total_chunks) * 100
                            print(f"   Progress: {progress:.1f}% ({chunks_written}/{total_chunks} chunks)")
                else:
                    file.write(data)
                    print("   ✅ Binary data written successfully")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error writing binary data: {e}")
            return False
    
    def read_binary_data(self, filename: str, chunk_size: int = 1024) -> Optional[bytes]:
        """
        Read binary data from file
        
        Args:
            filename: Source filename
            chunk_size: Size of chunks to read
            
        Returns:
            bytes: File contents or None if error
        """
        try:
            filepath = self.base_path / filename
            
            if not filepath.exists():
                print(f"   ❌ File '{filename}' not found")
                return None
            
            print(f"\n📖 Reading Binary Data from '{filename}'")
            print("=" * 35)
            print(f"   Source: {filepath}")
            print(f"   File size: {filepath.stat().st_size:,} bytes")
            
            with open(filepath, 'rb') as file:
                data = file.read()
                print(f"   ✅ Read {len(data):,} bytes successfully")
                
                # Show first few bytes for verification
                preview = data[:min(20, len(data))]
                hex_preview = ' '.join(f'{b:02x}' for b in preview)
                print(f"   Preview (hex): {hex_preview}...")
                
                return data
                
        except Exception as e:
            print(f"   ❌ Error reading binary data: {e}")
            return None
    
    def copy_binary_file(self, source: str, destination: str) -> bool:
        """
        Efficiently copy binary files with verification
        """
        try:
            source_path = Path(source)
            dest_path = self.base_path / destination
            
            print(f"\n📋 Copying Binary File")
            print("=" * 20)
            print(f"   Source: {source_path}")
            print(f"   Destination: {dest_path}")
            
            if not source_path.exists():
                print(f"   ❌ Source file not found")
                return False
            
            # Copy with progress for large files
            file_size = source_path.stat().st_size
            print(f"   File size: {file_size:,} bytes")
            
            shutil.copy2(source_path, dest_path)
            
            # Verify copy integrity
            if self._verify_file_integrity(source_path, dest_path):
                print("   ✅ File copied and verified successfully")
                return True
            else:
                print("   ❌ Copy verification failed")
                return False
                
        except Exception as e:
            print(f"   ❌ Error copying file: {e}")
            return False
    
    def _verify_file_integrity(self, file1: Path, file2: Path) -> bool:
        """Verify two files are identical using checksums"""
        try:
            hash1 = self._calculate_file_hash(file1)
            hash2 = self._calculate_file_hash(file2)
            return hash1 == hash2
        except:
            return False
    
    def _calculate_file_hash(self, filepath: Path) -> str:
        """Calculate SHA-256 hash of file"""
        sha256_hash = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

# =============================================================================
# SERIALIZATION AND DATA PERSISTENCE
# =============================================================================

class DataSerializer:
    """
    Handle various data serialization formats
    """
    
    def __init__(self, base_path: str = "serialized_data"):
        """Initialize serializer with base directory"""
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def save_to_pickle(self, data: Any, filename: str, protocol: int = 4) -> bool:
        """
        Serialize Python object to pickle file
        
        Args:
            data: Python object to serialize
            filename: Target filename
            protocol: Pickle protocol version
            
        Returns:
            bool: Success status
        """
        try:
            filepath = self.base_path / f"{filename}.pkl"
            
            print(f"\n🥒 Pickle Serialization")
            print("=" * 20)
            print(f"   Object type: {type(data).__name__}")
            print(f"   Protocol: {protocol}")
            print(f"   Target: {filepath}")
            
            with open(filepath, 'wb') as file:
                pickle.dump(data, file, protocol=protocol)
            
            file_size = filepath.stat().st_size
            print(f"   ✅ Serialized successfully ({file_size:,} bytes)")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Pickle serialization error: {e}")
            return False
    
    def load_from_pickle(self, filename: str) -> Any:
        """
        Deserialize Python object from pickle file
        
        Args:
            filename: Source filename (without .pkl extension)
            
        Returns:
            Any: Deserialized object or None if error
        """
        try:
            filepath = self.base_path / f"{filename}.pkl"
            
            if not filepath.exists():
                print(f"   ❌ Pickle file '{filename}.pkl' not found")
                return None
            
            print(f"\n🔓 Pickle Deserialization")
            print("=" * 22)
            print(f"   Source: {filepath}")
            
            with open(filepath, 'rb') as file:
                data = pickle.load(file)
            
            print(f"   ✅ Deserialized: {type(data).__name__}")
            
            if hasattr(data, '__len__'):
                try:
                    print(f"   Length: {len(data)}")
                except:
                    pass
            
            return data
            
        except Exception as e:
            print(f"   ❌ Pickle deserialization error: {e}")
            return None
    
    def save_to_json(self, data: Dict, filename: str, indent: int = 2) -> bool:
        """
        Save data to JSON file with formatting
        
        Args:
            data: Dictionary to serialize
            filename: Target filename
            indent: JSON indentation level
            
        Returns:
            bool: Success status
        """
        try:
            filepath = self.base_path / f"{filename}.json"
            
            print(f"\n🔗 JSON Serialization")
            print("=" * 18)
            print(f"   Data keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
            print(f"   Indent: {indent} spaces")
            print(f"   Target: {filepath}")
            
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent, ensure_ascii=False, 
                         separators=(',', ': '))
            
            file_size = filepath.stat().st_size
            print(f"   ✅ JSON saved successfully ({file_size:,} bytes)")
            
            return True
            
        except Exception as e:
            print(f"   ❌ JSON serialization error: {e}")
            return False
    
    def load_from_json(self, filename: str) -> Optional[Dict]:
        """
        Load data from JSON file
        
        Args:
            filename: Source filename (without .json extension)
            
        Returns:
            Dict: Loaded data or None if error
        """
        try:
            filepath = self.base_path / f"{filename}.json"
            
            if not filepath.exists():
                print(f"   ❌ JSON file '{filename}.json' not found")
                return None
            
            print(f"\n📋 JSON Deserialization")
            print("=" * 20)
            print(f"   Source: {filepath}")
            
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            print(f"   ✅ JSON loaded successfully")
            if isinstance(data, dict):
                print(f"   Keys: {list(data.keys())}")
            
            return data
            
        except Exception as e:
            print(f"   ❌ JSON deserialization error: {e}")
            return None

# =============================================================================
# CSV FILE OPERATIONS
# =============================================================================

class CSVHandler:
    """
    Advanced CSV file operations with various formats and options
    """
    
    def __init__(self, base_path: str = "csv_files"):
        """Initialize CSV handler with base directory"""
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def write_csv_data(self, filename: str, data: List[List], 
                      headers: Optional[List[str]] = None,
                      delimiter: str = ',') -> bool:
        """
        Write data to CSV file with customizable options
        
        Args:
            filename: Target CSV filename
            data: 2D list of data
            headers: Optional column headers
            delimiter: Field delimiter
            
        Returns:
            bool: Success status
        """
        try:
            filepath = self.base_path / f"{filename}.csv"
            
            print(f"\n📊 CSV Writing Operation")
            print("=" * 20)
            print(f"   Target: {filepath}")
            print(f"   Rows: {len(data)}")
            print(f"   Delimiter: '{delimiter}'")
            
            if headers:
                print(f"   Headers: {headers}")
            
            with open(filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=delimiter)
                
                # Write headers if provided
                if headers:
                    writer.writerow(headers)
                
                # Write data rows
                writer.writerows(data)
            
            file_size = filepath.stat().st_size
            print(f"   ✅ CSV written successfully ({file_size:,} bytes)")
            
            return True
            
        except Exception as e:
            print(f"   ❌ CSV writing error: {e}")
            return False
    
    def read_csv_data(self, filename: str, delimiter: str = ',',
                     has_headers: bool = True) -> Optional[Tuple[List, List]]:
        """
        Read CSV data with header detection
        
        Args:
            filename: Source CSV filename (without .csv extension)
            delimiter: Field delimiter
            has_headers: Whether first row contains headers
            
        Returns:
            Tuple of (headers, data) or None if error
        """
        try:
            filepath = self.base_path / f"{filename}.csv"
            
            if not filepath.exists():
                print(f"   ❌ CSV file '{filename}.csv' not found")
                return None
            
            print(f"\n📖 CSV Reading Operation")
            print("=" * 20)
            print(f"   Source: {filepath}")
            print(f"   Delimiter: '{delimiter}'")
            print(f"   Has headers: {has_headers}")
            
            headers = None
            data = []
            
            with open(filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=delimiter)
                
                if has_headers:
                    headers = next(reader, None)
                    print(f"   Headers: {headers}")
                
                data = list(reader)
                print(f"   Data rows: {len(data)}")
                
                if data:
                    print(f"   Columns: {len(data[0]) if data else 0}")
            
            return headers, data
            
        except Exception as e:
            print(f"   ❌ CSV reading error: {e}")
            return None
    
    def process_large_csv(self, filename: str, 
                         processor_func, chunk_size: int = 1000) -> bool:
        """
        Process large CSV files in chunks to manage memory
        
        Args:
            filename: CSV filename
            processor_func: Function to process each chunk
            chunk_size: Number of rows per chunk
            
        Returns:
            bool: Success status
        """
        try:
            filepath = self.base_path / f"{filename}.csv"
            
            print(f"\n🔄 Large CSV Processing")
            print("=" * 20)
            print(f"   Source: {filepath}")
            print(f"   Chunk size: {chunk_size} rows")
            
            with open(filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                
                chunk = []
                chunk_num = 1
                total_rows = 0
                
                for row in reader:
                    chunk.append(row)
                    
                    if len(chunk) >= chunk_size:
                        print(f"   Processing chunk {chunk_num} ({len(chunk)} rows)")
                        processor_func(headers, chunk)
                        total_rows += len(chunk)
                        chunk = []
                        chunk_num += 1
                
                # Process remaining rows
                if chunk:
                    print(f"   Processing final chunk {chunk_num} ({len(chunk)} rows)")
                    processor_func(headers, chunk)
                    total_rows += len(chunk)
                
                print(f"   ✅ Processed {total_rows} rows in {chunk_num} chunks")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Large CSV processing error: {e}")
            return False

# =============================================================================
# FILE COMPRESSION AND ARCHIVING
# =============================================================================

class CompressionHandler:
    """
    Handle file compression and decompression operations
    """
    
    def __init__(self, base_path: str = "compressed_files"):
        """Initialize compression handler"""
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def compress_file_gzip(self, source_file: str, 
                          compressed_name: Optional[str] = None) -> bool:
        """
        Compress a file using gzip compression
        
        Args:
            source_file: Path to source file
            compressed_name: Optional name for compressed file
            
        Returns:
            bool: Success status
        """
        try:
            source_path = Path(source_file)
            
            if not source_path.exists():
                print(f"   ❌ Source file '{source_file}' not found")
                return False
            
            if not compressed_name:
                compressed_name = f"{source_path.stem}.gz"
            
            compressed_path = self.base_path / compressed_name
            
            print(f"\n🗜️  GZIP Compression")
            print("=" * 16)
            print(f"   Source: {source_path}")
            print(f"   Target: {compressed_path}")
            
            original_size = source_path.stat().st_size
            print(f"   Original size: {original_size:,} bytes")
            
            with open(source_path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            compressed_size = compressed_path.stat().st_size
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            print(f"   Compressed size: {compressed_size:,} bytes")
            print(f"   Compression ratio: {compression_ratio:.1f}%")
            print(f"   ✅ Compression successful")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Compression error: {e}")
            return False
    
    def decompress_file_gzip(self, compressed_file: str,
                            output_name: Optional[str] = None) -> bool:
        """
        Decompress a gzip file
        
        Args:
            compressed_file: Path to compressed file
            output_name: Optional name for decompressed file
            
        Returns:
            bool: Success status
        """
        try:
            compressed_path = self.base_path / compressed_file
            
            if not compressed_path.exists():
                print(f"   ❌ Compressed file '{compressed_file}' not found")
                return False
            
            if not output_name:
                # Remove .gz extension for output name
                output_name = compressed_path.stem
            
            output_path = self.base_path / output_name
            
            print(f"\n📤 GZIP Decompression")
            print("=" * 18)
            print(f"   Source: {compressed_path}")
            print(f"   Target: {output_path}")
            
            compressed_size = compressed_path.stat().st_size
            print(f"   Compressed size: {compressed_size:,} bytes")
            
            with gzip.open(compressed_path, 'rb') as f_in:
                with open(output_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            decompressed_size = output_path.stat().st_size
            expansion_ratio = (decompressed_size / compressed_size)
            
            print(f"   Decompressed size: {decompressed_size:,} bytes")
            print(f"   Expansion ratio: {expansion_ratio:.1f}x")
            print(f"   ✅ Decompression successful")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Decompression error: {e}")
            return False

# =============================================================================
# FILE SECURITY AND INTEGRITY
# =============================================================================

class FileSecurityHandler:
    """
    Handle file security operations including hashing and basic encryption
    """
    
    def __init__(self, base_path: str = "secure_files"):
        """Initialize security handler"""
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def calculate_file_checksums(self, filepath: str) -> Dict[str, str]:
        """
        Calculate multiple checksums for file integrity verification
        
        Args:
            filepath: Path to file
            
        Returns:
            Dict containing various checksums
        """
        try:
            file_path = Path(filepath)
            
            if not file_path.exists():
                print(f"   ❌ File '{filepath}' not found")
                return {}
            
            print(f"\n🔐 Checksum Calculation")
            print("=" * 20)
            print(f"   File: {file_path}")
            
            file_size = file_path.stat().st_size
            print(f"   Size: {file_size:,} bytes")
            
            # Initialize hash objects
            md5_hash = hashlib.md5()
            sha1_hash = hashlib.sha1()
            sha256_hash = hashlib.sha256()
            
            # Read file in chunks for memory efficiency
            with open(file_path, 'rb') as file:
                chunk_size = 8192
                chunks_processed = 0
                
                while chunk := file.read(chunk_size):
                    md5_hash.update(chunk)
                    sha1_hash.update(chunk)
                    sha256_hash.update(chunk)
                    chunks_processed += 1
                    
                    if chunks_processed % 1000 == 0:
                        print(f"   Processed {chunks_processed * chunk_size:,} bytes...")
            
            checksums = {
                'md5': md5_hash.hexdigest(),
                'sha1': sha1_hash.hexdigest(),
                'sha256': sha256_hash.hexdigest()
            }
            
            print(f"\n   📊 Checksums:")
            for alg, checksum in checksums.items():
                print(f"   {alg.upper():6}: {checksum}")
            
            # Save checksums to file
            checksum_file = self.base_path / f"{file_path.stem}_checksums.txt"
            with open(checksum_file, 'w') as f:
                f.write(f"File: {file_path}\n")
                f.write(f"Size: {file_size} bytes\n")
                f.write(f"Date: {datetime.now().isoformat()}\n\n")
                for alg, checksum in checksums.items():
                    f.write(f"{alg.upper()}: {checksum}\n")
            
            print(f"   ✅ Checksums saved to {checksum_file}")
            
            return checksums
            
        except Exception as e:
            print(f"   ❌ Checksum calculation error: {e}")
            return {}
    
    def verify_file_integrity(self, filepath: str, 
                            expected_checksums: Dict[str, str]) -> bool:
        """
        Verify file integrity against expected checksums
        
        Args:
            filepath: Path to file to verify
            expected_checksums: Dictionary of algorithm: checksum pairs
            
        Returns:
            bool: True if all checksums match
        """
        try:
            print(f"\n🔍 File Integrity Verification")
            print("=" * 25)
            
            current_checksums = self.calculate_file_checksums(filepath)
            
            if not current_checksums:
                return False
            
            print(f"\n   📋 Verification Results:")
            all_match = True
            
            for algorithm, expected in expected_checksums.items():
                current = current_checksums.get(algorithm.lower())
                
                if current:
                    match = (current == expected.lower())
                    status = "✅ MATCH" if match else "❌ MISMATCH"
                    print(f"   {algorithm.upper():6}: {status}")
                    
                    if not match:
                        all_match = False
                        print(f"          Expected: {expected}")
                        print(f"          Current:  {current}")
                else:
                    print(f"   {algorithm.upper():6}: ⚠️ NOT CALCULATED")
                    all_match = False
            
            print(f"\n   🎯 Overall: {'✅ VERIFIED' if all_match else '❌ FAILED'}")
            return all_match
            
        except Exception as e:
            print(f"   ❌ Verification error: {e}")
            return False
    
    def simple_encrypt_file(self, filepath: str, key: str) -> bool:
        """
        Simple XOR-based file encryption (educational purposes only)
        
        Args:
            filepath: Path to file to encrypt
            key: Encryption key string
            
        Returns:
            bool: Success status
        """
        try:
            file_path = Path(filepath)
            
            if not file_path.exists():
                print(f"   ❌ File '{filepath}' not found")
                return False
            
            encrypted_path = self.base_path / f"{file_path.stem}_encrypted{file_path.suffix}"
            
            print(f"\n🔒 Simple File Encryption")
            print("=" * 22)
            print(f"   Source: {file_path}")
            print(f"   Target: {encrypted_path}")
            print(f"   Key length: {len(key)} characters")
            print("   ⚠️ WARNING: This is educational encryption only!")
            
            # Convert key to bytes
            key_bytes = key.encode('utf-8')
            key_length = len(key_bytes)
            
            with open(file_path, 'rb') as infile, \
                 open(encrypted_path, 'wb') as outfile:
                
                byte_count = 0
                while byte := infile.read(1):
                    if byte:
                        # XOR with key byte
                        key_byte = key_bytes[byte_count % key_length]
                        encrypted_byte = bytes([byte[0] ^ key_byte])
                        outfile.write(encrypted_byte)
                        byte_count += 1
            
            print(f"   ✅ Encrypted {byte_count:,} bytes")
            return True
            
        except Exception as e:
            print(f"   ❌ Encryption error: {e}")
            return False

# =============================================================================
# CONCURRENT FILE OPERATIONS
# =============================================================================

class ConcurrentFileHandler:
    """
    Handle concurrent file operations for improved performance
    """
    
    def __init__(self, max_workers: int = 4):
        """Initialize with maximum worker threads"""
        self.max_workers = max_workers
    
    def process_files_concurrently(self, file_list: List[str], 
                                  processor_func, *args) -> List[bool]:
        """
        Process multiple files concurrently
        
        Args:
            file_list: List of file paths to process
            processor_func: Function to process each file
            *args: Additional arguments for processor function
            
        Returns:
            List of success statuses for each file
        """
        print(f"\n⚡ Concurrent File Processing")
        print("=" * 25)
        print(f"   Files to process: {len(file_list)}")
        print(f"   Max workers: {self.max_workers}")
        
        results = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(processor_func, filepath, *args): filepath
                for filepath in file_list
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_file):
                filepath = future_to_file[future]
                try:
                    result = future.result()
                    results.append(result)
                    status = "✅" if result else "❌"
                    print(f"   {status} Processed: {Path(filepath).name}")
                except Exception as e:
                    results.append(False)
                    print(f"   ❌ Error processing {Path(filepath).name}: {e}")
        
        success_count = sum(results)
        print(f"\n   📊 Summary: {success_count}/{len(file_list)} files processed successfully")
        
        return results

# =============================================================================
# TEMPORARY FILE OPERATIONS
# =============================================================================

class TemporaryFileManager:
    """
    Manage temporary files and directories safely
    """
    
    def __init__(self):
        """Initialize temporary file manager"""
        self.temp_files = []
        self.temp_dirs = []
    
    def create_temp_file(self, suffix: str = ".tmp", 
                        delete_on_exit: bool = True) -> str:
        """
        Create a temporary file
        
        Args:
            suffix: File suffix
            delete_on_exit: Whether to delete file automatically
            
        Returns:
            str: Path to temporary file
        """
        try:
            temp_file = tempfile.NamedTemporaryFile(
                suffix=suffix, delete=False
            )
            temp_path = temp_file.name
            temp_file.close()
            
            if delete_on_exit:
                self.temp_files.append(temp_path)
            
            print(f"   📁 Created temporary file: {temp_path}")
            return temp_path
            
        except Exception as e:
            print(f"   ❌ Error creating temporary file: {e}")
            return ""
    
    def create_temp_directory(self, delete_on_exit: bool = True) -> str:
        """
        Create a temporary directory
        
        Args:
            delete_on_exit: Whether to delete directory automatically
            
        Returns:
            str: Path to temporary directory
        """
        try:
            temp_dir = tempfile.mkdtemp()
            
            if delete_on_exit:
                self.temp_dirs.append(temp_dir)
            
            print(f"   📂 Created temporary directory: {temp_dir}")
            return temp_dir
            
        except Exception as e:
            print(f"   ❌ Error creating temporary directory: {e}")
            return ""
    
    def cleanup(self):
        """Clean up all temporary files and directories"""
        print(f"\n🧹 Cleaning up temporary files...")
        
        # Clean up temporary files
        for temp_file in self.temp_files:
            try:
                if Path(temp_file).exists():
                    Path(temp_file).unlink()
                    print(f"   ✅ Deleted temporary file: {temp_file}")
            except Exception as e:
                print(f"   ❌ Error deleting {temp_file}: {e}")
        
        # Clean up temporary directories
        for temp_dir in self.temp_dirs:
            try:
                if Path(temp_dir).exists():
                    shutil.rmtree(temp_dir)
                    print(f"   ✅ Deleted temporary directory: {temp_dir}")
            except Exception as e:
                print(f"   ❌ Error deleting {temp_dir}: {e}")
        
        self.temp_files.clear()
        self.temp_dirs.clear()

# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_binary_operations():
    """Demonstrate binary file operations"""
    print("\n" + "="*60)
    print("BINARY FILE OPERATIONS DEMONSTRATION")
    print("="*60)
    
    binary_handler = BinaryFileHandler()
    
    # Create sample binary data
    sample_data = bytes(range(256)) * 10  # 2560 bytes of sample data
    
    # Write binary data
    binary_handler.write_binary_data("sample_binary.bin", sample_data)
    
    # Read binary data
    read_data = binary_handler.read_binary_data("sample_binary.bin")
    
    if read_data:
        print(f"   ✅ Verification: Data integrity {'preserved' if read_data == sample_data else 'lost'}")

def demonstrate_serialization():
    """Demonstrate data serialization"""
    print("\n" + "="*60)
    print("DATA SERIALIZATION DEMONSTRATION")
    print("="*60)
    
    serializer = DataSerializer()
    
    # Sample complex data structure
    sample_data = {
        'name': 'Advanced File Operations',
        'version': 1.0,
        'features': ['binary', 'compression', 'serialization'],
        'config': {
            'max_workers': 4,
            'chunk_size': 1024,
            'compression': True
        },
        'metadata': {
            'created': datetime.now().isoformat(),
            'author': 'Python Learning Notes'
        }
    }
    
    # Demonstrate pickle serialization
    serializer.save_to_pickle(sample_data, "sample_config")
    loaded_pickle = serializer.load_from_pickle("sample_config")
    
    # Demonstrate JSON serialization
    serializer.save_to_json(sample_data, "sample_config")
    loaded_json = serializer.load_from_json("sample_config")
    
    print(f"   ✅ Pickle roundtrip: {'success' if loaded_pickle == sample_data else 'failed'}")
    print(f"   ✅ JSON roundtrip: {'success' if loaded_json == sample_data else 'failed'}")

def demonstrate_csv_operations():
    """Demonstrate CSV operations"""
    print("\n" + "="*60)
    print("CSV OPERATIONS DEMONSTRATION")
    print("="*60)
    
    csv_handler = CSVHandler()
    
    # Sample CSV data
    headers = ['Name', 'Age', 'City', 'Score']
    data = [
        ['Alice', '25', 'New York', '95.5'],
        ['Bob', '30', 'London', '87.2'],
        ['Charlie', '35', 'Tokyo', '92.8'],
        ['Diana', '28', 'Paris', '89.1']
    ]
    
    # Write CSV data
    csv_handler.write_csv_data("sample_data", data, headers)
    
    # Read CSV data
    read_headers, read_data = csv_handler.read_csv_data("sample_data")
    
    print(f"   ✅ CSV roundtrip: {'success' if read_data == data else 'failed'}")

def demonstrate_compression():
    """Demonstrate file compression"""
    print("\n" + "="*60)
    print("FILE COMPRESSION DEMONSTRATION")
    print("="*60)
    
    compression_handler = CompressionHandler()
    
    # Create a sample text file for compression
    sample_file = "sample_text.txt"
    sample_content = "This is sample text content for compression testing. " * 100
    
    with open(sample_file, 'w') as f:
        f.write(sample_content)
    
    # Compress the file
    compression_handler.compress_file_gzip(sample_file)
    
    # Decompress the file
    compression_handler.decompress_file_gzip("sample_text.gz", "decompressed_text.txt")
    
    # Verify integrity
    with open("decompressed_text.txt", 'r') as f:
        decompressed_content = f.read()
    
    print(f"   ✅ Compression roundtrip: {'success' if decompressed_content == sample_content else 'failed'}")
    
    # Cleanup
    Path(sample_file).unlink(missing_ok=True)
    Path("decompressed_text.txt").unlink(missing_ok=True)

def demonstrate_security_features():
    """Demonstrate file security features"""
    print("\n" + "="*60)
    print("FILE SECURITY DEMONSTRATION")
    print("="*60)
    
    security_handler = FileSecurityHandler()
    
    # Create a sample file
    sample_file = "security_test.txt"
    sample_content = "This is confidential data that needs protection."
    
    with open(sample_file, 'w') as f:
        f.write(sample_content)
    
    # Calculate checksums
    checksums = security_handler.calculate_file_checksums(sample_file)
    
    # Verify integrity
    if checksums:
        integrity_ok = security_handler.verify_file_integrity(sample_file, checksums)
        print(f"   ✅ Integrity verification: {'passed' if integrity_ok else 'failed'}")
    
    # Demonstrate simple encryption
    security_handler.simple_encrypt_file(sample_file, "secret_key_123")
    
    # Cleanup
    Path(sample_file).unlink(missing_ok=True)

def interactive_advanced_file_operations():
    """
    Interactive advanced file operations tool
    """
    print(f"\n🎮 INTERACTIVE ADVANCED FILE OPERATIONS")
    print("=" * 38)
    
    while True:
        try:
            print(f"\n🎯 Choose an operation:")
            print("   1. Binary file operations")
            print("   2. Data serialization (Pickle/JSON)")
            print("   3. CSV file handling")
            print("   4. File compression/decompression")
            print("   5. File security and checksums")
            print("   6. Concurrent file processing demo")
            print("   7. Temporary file management")
            print("   8. Run all demonstrations")
            print("   9. Learn about advanced concepts")
            print("   10. Exit")
            
            choice = input("\nEnter your choice (1-10): ").strip()
            
            if choice == "1":
                demonstrate_binary_operations()
                
            elif choice == "2":
                demonstrate_serialization()
                
            elif choice == "3":
                demonstrate_csv_operations()
                
            elif choice == "4":
                demonstrate_compression()
                
            elif choice == "5":
                demonstrate_security_features()
                
            elif choice == "6":
                # Concurrent processing demo
                files = ["file1.txt", "file2.txt", "file3.txt"]
                concurrent_handler = ConcurrentFileHandler()
                
                def sample_processor(filepath):
                    # Simulate processing
                    import time
                    time.sleep(1)
                    return True
                
                concurrent_handler.process_files_concurrently(files, sample_processor)
                
            elif choice == "7":
                # Temporary file demo
                temp_manager = TemporaryFileManager()
                temp_file = temp_manager.create_temp_file(".txt")
                temp_dir = temp_manager.create_temp_directory()
                
                if temp_file and temp_dir:
                    print("   ✅ Temporary resources created successfully")
                
                temp_manager.cleanup()
                
            elif choice == "8":
                demonstrate_binary_operations()
                demonstrate_serialization()
                demonstrate_csv_operations()
                demonstrate_compression()
                demonstrate_security_features()
                
            elif choice == "9":
                explain_advanced_file_concepts()
                
            elif choice == "10":
                print("\n👋 Thanks for exploring advanced file operations!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-10.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    """
    Main execution demonstrating advanced file operations
    """
    print(__doc__)
    
    # Educational content
    explain_advanced_file_concepts()
    
    # Run demonstrations
    demonstrate_binary_operations()
    demonstrate_serialization()
    demonstrate_csv_operations()
    demonstrate_compression()
    demonstrate_security_features()
    
    # Interactive tool
    interactive_advanced_file_operations()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Advanced file handling techniques and patterns")
    print("✅ Binary file operations and data manipulation")
    print("✅ Data serialization with Pickle and JSON")
    print("✅ CSV processing and structured data handling")
    print("✅ File compression and decompression methods")
    print("✅ File security, integrity, and encryption basics")
    print("✅ Concurrent processing for improved performance")
    print("✅ Temporary file and resource management")
    
    print("\n💡 Key Concepts Learned:")
    print("• Binary vs text file handling differences")
    print("• Data persistence and serialization formats")
    print("• Memory-efficient processing of large files")
    print("• File integrity verification with checksums")
    print("• Performance optimization through concurrency")
    print("• Secure file operations and encryption concepts")
    
    print("\n🎯 Next Steps:")
    print("• Study database file formats and operations")
    print("• Explore advanced compression algorithms")
    print("• Learn professional encryption and cryptography")
    print("• Investigate memory-mapped files for big data")
    print("• Master enterprise file management patterns")
