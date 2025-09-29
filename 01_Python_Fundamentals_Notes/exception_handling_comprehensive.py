"""
Exception Handling in Python - Comprehensive Guide
==================================================

Educational guide to error handling: try-except blocks, custom exceptions, logging, and debugging techniques.
Includes best practices, patterns, and real-world examples.

Author: Python Learning Notes
Date: September 2025
Topic: Exception Handling, Error Management, Logging, Debugging
"""

import logging
import sys
from typing import Optional

# =============================================================================
# BASIC EXCEPTION HANDLING
# =============================================================================

def divide_numbers(a: float, b: float) -> Optional[float]:
    """
    Safe division with exception handling
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError as e:
        print(f"Error: Invalid types - {e}")
        return None
    finally:
        print("Division operation completed.")

# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance {balance}, needed {amount}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# =============================================================================
# LOGGING
# =============================================================================

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def log_example():
    """Demonstrate logging at different levels"""
    logger = logging.getLogger(__name__)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

# =============================================================================
# CONTEXT MANAGERS FOR RESOURCE MANAGEMENT
# =============================================================================

class FileManager:
    """Custom context manager for file operations"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False  # Re-raise the exception

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    # Basic exception handling
    print("Basic Exception Handling:")
    result = divide_numbers(10, 0)
    print(f"Result: {result}")
    
    # Custom exceptions
    print("\nCustom Exceptions:")
    account = BankAccount(100)
    try:
        account.withdraw(150)
    except InsufficientFundsError as e:
        print(f"Custom exception caught: {e}")
    
    # Logging
    print("\nLogging:")
    setup_logging()
    log_example()
    
    # Context manager
    print("\nContext Manager:")
    with FileManager('test.txt', 'w') as f:
        f.write("Hello, World!")
    print("File operation completed safely.")

if __name__ == "__main__":
    main()
