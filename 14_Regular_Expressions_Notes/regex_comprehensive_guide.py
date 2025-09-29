"""
Regular Expressions in Python - Comprehensive Guide
==================================================

Educational guide to regex patterns, text processing, validation, and practical examples for data extraction.
Includes pattern matching, groups, flags, and real-world applications.

Author: Python Learning Notes
Date: September 2025
Topic: Regular Expressions, Pattern Matching, Text Processing, Validation
"""

import re
from typing import List, Optional, Match

# =============================================================================
# BASIC PATTERN MATCHING
# =============================================================================

def basic_patterns_demo():
    """Demonstrate basic regex patterns"""
    text = "The quick brown fox jumps over the lazy dog"
    
    print("Basic Pattern Matching:")
    
    # Find all words
    words = re.findall(r'\b\w+\b', text)
    print(f"Words: {words}")
    
    # Find words starting with 't'
    t_words = re.findall(r'\bt\w*\b', text, re.IGNORECASE)
    print(f"Words starting with 't': {t_words}")
    
    # Check if text contains a pattern
    has_fox = re.search(r'fox', text)
    print(f"Contains 'fox': {has_fox is not None}")
    
    # Replace patterns
    replaced = re.sub(r'\bthe\b', 'THE', text, flags=re.IGNORECASE)
    print(f"Replaced 'the': {replaced}")

# =============================================================================
# PATTERN COMPONENTS
# =============================================================================

def pattern_components_demo():
    """Demonstrate regex pattern components"""
    print("\nPattern Components:")
    
    patterns = [
        (r'\d+', 'Digits: one or more digits'),
        (r'\w+', 'Word characters: letters, digits, underscore'),
        (r'\s+', 'Whitespace characters'),
        (r'[aeiou]', 'Character class: vowels'),
        (r'[^aeiou]', 'Negated class: non-vowels'),
        (r'a{2,4}', 'Quantifier: 2-4 occurrences of "a"'),
        (r'(abc)+', 'Groups: one or more "abc"'),
        (r'^Hello', 'Anchors: start of string'),
        (r'world$', 'Anchors: end of string')
    ]
    
    test_strings = [
        "Hello123 world!",
        "aaabbbccc",
        "test@example.com",
        "123-456-7890"
    ]
    
    for pattern, description in patterns:
        print(f"\n{description} (pattern: {pattern})")
        for test_str in test_strings:
            matches = re.findall(pattern, test_str)
            if matches:
                print(f"  '{test_str}' -> {matches}")

# =============================================================================
# EMAIL VALIDATION
# =============================================================================

def email_validation_demo():
    """Demonstrate email validation with regex"""
    print("\nEmail Validation:")
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    test_emails = [
        "user@example.com",
        "test.email+tag@domain.co.uk",
        "invalid-email",
        "user@.com",
        "user@domain",
        "@domain.com"
    ]
    
    for email in test_emails:
        is_valid = re.match(email_pattern, email) is not None
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {status}: {email}")

# =============================================================================
# DATA EXTRACTION
# =============================================================================

def data_extraction_demo():
    """Demonstrate data extraction from text"""
    print("\nData Extraction:")
    
    # Extract phone numbers
    text_with_phones = """
    Contact us at (555) 123-4567 or 555-987-6543.
    Emergency: 911
    International: +1-555-000-1111
    """
    
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})'
    phones = re.findall(phone_pattern, text_with_phones)
    print("Phone numbers found:")
    for phone in phones:
        formatted = ''.join(phone).strip()
        print(f"  {formatted}")
    
    # Extract URLs
    text_with_urls = """
    Visit https://www.example.com/page or http://test.org.
    Also check out www.github.com/user/repo
    """
    
    url_pattern = r'https?://[^\s]+|www\.[^\s]+'
    urls = re.findall(url_pattern, text_with_urls)
    print("URLs found:")
    for url in urls:
        print(f"  {url}")

# =============================================================================
# ADVANCED FEATURES
# =============================================================================

def advanced_features_demo():
    """Demonstrate advanced regex features"""
    print("\nAdvanced Features:")
    
    # Named groups
    pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
    date_str = "2025-09-30"
    match = re.match(pattern, date_str)
    if match:
        print(f"Named groups: {match.groupdict()}")
    
    # Non-capturing groups
    pattern = r'(?:https?://)?(?:www\.)?([^/\s]+\.[^/\s]+)'
    urls = ["https://www.example.com", "example.org", "sub.domain.co.uk"]
    for url in urls:
        match = re.search(pattern, url)
        if match:
            print(f"Domain from '{url}': {match.group(1)}")
    
    # Lookahead and lookbehind
    text = "password: secret123, username: admin"
    # Positive lookahead
    passwords = re.findall(r'password:\s*(\w+)(?=\s*,)', text)
    print(f"Passwords: {passwords}")
    
    # Positive lookbehind (fixed width)
    usernames = re.findall(r'(?<=username: )\w+', text)
    print(f"Usernames: {usernames}")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications_demo():
    """Demonstrate practical regex applications"""
    print("\nPractical Applications:")
    
    # Log file parsing
    log_entry = '2025-09-30 14:30:25 ERROR Database connection failed: timeout'
    log_pattern = r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)'
    match = re.match(log_pattern, log_entry)
    if match:
        date, time, level, message = match.groups()
        print(f"Parsed log: Date={date}, Time={time}, Level={level}, Message={message}")
    
    # HTML tag removal
    html_text = "<p>This is <b>bold</b> text with <a href='#'>links</a>.</p>"
    clean_text = re.sub(r'<[^>]+>', '', html_text)
    print(f"HTML cleaned: {clean_text}")
    
    # Password strength validation
    def validate_password(password: str) -> List[str]:
        issues = []
        if len(password) < 8:
            issues.append("At least 8 characters")
        if not re.search(r'[A-Z]', password):
            issues.append("At least one uppercase letter")
        if not re.search(r'[a-z]', password):
            issues.append("At least one lowercase letter")
        if not re.search(r'\d', password):
            issues.append("At least one digit")
        return issues
    
    test_passwords = ["weak", "Strong123", "password", "Str0ng!Pass"]
    for pwd in test_passwords:
        issues = validate_password(pwd)
        strength = "Strong" if not issues else f"Weak: {', '.join(issues)}"
        print(f"Password '{pwd}': {strength}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    basic_patterns_demo()
    pattern_components_demo()
    email_validation_demo()
    data_extraction_demo()
    advanced_features_demo()
    practical_applications_demo()
    
    print("\nRegular expressions guide completed!")

if __name__ == "__main__":
    main()
