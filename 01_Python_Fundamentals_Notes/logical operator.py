"""
Python Logical Operators - Complete Learning Guide
================================================

Comprehensive guide to logical operators in Python, covering and, or, not
operators, truth tables, short-circuiting, and practical applications
in conditional logic and decision making.

Author: Python Learning Notes
Date: September 2025
Topic: Logical Operators, Boolean Logic, Conditional Statements
"""

# =============================================================================
# UNDERSTANDING LOGICAL OPERATORS
# =============================================================================

def introduction_to_logical_operators():
    """
    Introduction to logical operators and their role in programming
    """
    print("🧠 LOGICAL OPERATORS IN PYTHON")
    print("=" * 35)
    
    print("\n🔍 What are Logical Operators?")
    print("Logical operators are used to:")
    print("   • Combine multiple conditions")
    print("   • Create complex boolean expressions")
    print("   • Control program flow with decision making")
    print("   • Return boolean values (True or False)")
    
    print("\n📋 The Three Main Logical Operators:")
    print("   1️⃣ and  - Returns True if ALL conditions are True")
    print("   2️⃣ or   - Returns True if AT LEAST ONE condition is True")  
    print("   3️⃣ not  - Returns the OPPOSITE of the condition")

# =============================================================================
# THE 'AND' LOGICAL OPERATOR
# =============================================================================

def demonstrate_and_operator():
    """
    Comprehensive demonstration of the 'and' logical operator
    """
    print("\n🔗 THE 'AND' LOGICAL OPERATOR")
    print("=" * 35)
    
    print("📝 How 'and' works:")
    print("   • Returns True only if BOTH conditions are True")
    print("   • Returns False if ANY condition is False")
    print("   • Uses short-circuit evaluation (stops at first False)")
    
    # Truth table for 'and'
    print("\n📊 Truth Table for 'and':")
    print("   ┌─────────┬─────────┬─────────────┐")
    print("   │ Value A │ Value B │ A and B     │")
    print("   ├─────────┼─────────┼─────────────┤")
    print("   │ True    │ True    │ True        │")
    print("   │ True    │ False   │ False       │")
    print("   │ False   │ True    │ False       │")
    print("   │ False   │ False   │ False       │")
    print("   └─────────┴─────────┴─────────────┘")
    
    # Practical examples
    print("\n💡 Practical Examples:")
    
    # Example 1: Basic boolean values
    a = True
    b = False
    result = a and b
    print(f"\n1️⃣ Basic Example:")
    print(f"   a = {a}, b = {b}")
    print(f"   a and b = {result}")
    
    # Example 2: Numeric comparisons
    age = 25
    has_license = True
    
    if age >= 18 and has_license:
        print(f"\n2️⃣ Driving Eligibility:")
        print(f"   Age: {age}, Has License: {has_license}")
        print("   ✅ Can drive (age >= 18 AND has license)")
    else:
        print("   ❌ Cannot drive")
    
    # Example 3: Range checking
    score = 85
    if score >= 80 and score <= 100:
        print(f"\n3️⃣ Grade Checking:")
        print(f"   Score: {score}")
        print("   ✅ Grade A (80 <= score <= 100)")
    
    # Example 4: String conditions
    username = "alice"
    password = "secret123"
    
    if len(username) >= 3 and len(password) >= 8:
        print(f"\n4️⃣ Login Validation:")
        print(f"   Username: '{username}' (length: {len(username)})")
        print(f"   Password: '{password}' (length: {len(password)})")
        print("   ✅ Valid credentials (username >= 3 AND password >= 8)")
    else:
        print("   ❌ Invalid credentials")

# =============================================================================
# THE 'OR' LOGICAL OPERATOR  
# =============================================================================

def demonstrate_or_operator():
    """
    Comprehensive demonstration of the 'or' logical operator
    """
    print("\n🔀 THE 'OR' LOGICAL OPERATOR")
    print("=" * 34)
    
    print("📝 How 'or' works:")
    print("   • Returns True if AT LEAST ONE condition is True")
    print("   • Returns False only if ALL conditions are False")
    print("   • Uses short-circuit evaluation (stops at first True)")
    
    # Truth table for 'or'
    print("\n📊 Truth Table for 'or':")
    print("   ┌─────────┬─────────┬─────────────┐")
    print("   │ Value A │ Value B │ A or B      │")
    print("   ├─────────┼─────────┼─────────────┤")
    print("   │ True    │ True    │ True        │")
    print("   │ True    │ False   │ True        │")
    print("   │ False   │ True    │ True        │")
    print("   │ False   │ False   │ False       │")
    print("   └─────────┴─────────┴─────────────┘")
    
    # Practical examples
    print("\n💡 Practical Examples:")
    
    # Example 1: Basic boolean values
    a = True
    b = False
    result = a or b
    print(f"\n1️⃣ Basic Example:")
    print(f"   a = {a}, b = {b}")
    print(f"   a or b = {result}")
    
    # Example 2: Weekend checking
    day = "Saturday"
    if day == "Saturday" or day == "Sunday":
        print(f"\n2️⃣ Weekend Check:")
        print(f"   Day: {day}")
        print("   ✅ It's a weekend!")
    else:
        print("   ❌ It's a weekday")
    
    # Example 3: Emergency contact
    is_emergency = False
    is_family = True
    
    if is_emergency or is_family:
        print(f"\n3️⃣ Call Permission:")
        print(f"   Emergency: {is_emergency}, Family: {is_family}")
        print("   ✅ Call allowed (emergency OR family)")
    
    # Example 4: Discount eligibility
    is_student = False
    is_senior = False
    is_member = True
    
    if is_student or is_senior or is_member:
        print(f"\n4️⃣ Discount Eligibility:")
        print(f"   Student: {is_student}, Senior: {is_senior}, Member: {is_member}")
        print("   ✅ Eligible for discount")

# =============================================================================
# THE 'NOT' LOGICAL OPERATOR
# =============================================================================

def demonstrate_not_operator():
    """
    Comprehensive demonstration of the 'not' logical operator
    """
    print("\n🔄 THE 'NOT' LOGICAL OPERATOR")
    print("=" * 34)
    
    print("📝 How 'not' works:")
    print("   • Returns the OPPOSITE boolean value")
    print("   • True becomes False, False becomes True")
    print("   • Unary operator (works on single operand)")
    
    # Truth table for 'not'
    print("\n📊 Truth Table for 'not':")
    print("   ┌─────────┬─────────────┐")
    print("   │ Value A │ not A       │")
    print("   ├─────────┼─────────────┤")
    print("   │ True    │ False       │")
    print("   │ False   │ True        │")
    print("   └─────────┴─────────────┘")
    
    # Practical examples
    print("\n💡 Practical Examples:")
    
    # Example 1: Basic boolean negation
    is_raining = False
    result = not is_raining
    print(f"\n1️⃣ Basic Negation:")
    print(f"   is_raining = {is_raining}")
    print(f"   not is_raining = {result}")
    
    # Example 2: Access control
    is_blocked = False
    if not is_blocked:
        print(f"\n2️⃣ Access Control:")
        print(f"   User blocked: {is_blocked}")
        print("   ✅ Access granted (user is NOT blocked)")
    
    # Example 3: Validation
    username = "alice"
    if not (username == ""):
        print(f"\n3️⃣ Input Validation:")
        print(f"   Username: '{username}'")
        print("   ✅ Valid username (NOT empty)")
    
    # Example 4: Game state
    game_over = False
    if not game_over:
        print(f"\n4️⃣ Game State:")
        print(f"   Game over: {game_over}")
        print("   🎮 Continue playing (game is NOT over)")

# =============================================================================
# COMBINING LOGICAL OPERATORS
# =============================================================================

def demonstrate_combined_operators():
    """
    Demonstrate combining multiple logical operators
    """
    print("\n🔗 COMBINING LOGICAL OPERATORS")
    print("=" * 38)
    
    print("📝 Operator Precedence (highest to lowest):")
    print("   1️⃣ not  (highest)")
    print("   2️⃣ and")
    print("   3️⃣ or   (lowest)")
    print("\n💡 Use parentheses to control evaluation order!")
    
    # Complex conditions
    print("\n🎯 Complex Condition Examples:")
    
    # Example 1: Age and membership check
    age = 25
    is_student = False
    is_member = True
    
    # Without parentheses (follows precedence)
    condition1 = age >= 18 and is_student or is_member
    print(f"\n1️⃣ Library Access Check:")
    print(f"   Age: {age}, Student: {is_student}, Member: {is_member}")
    print(f"   age >= 18 and is_student or is_member = {condition1}")
    
    # With parentheses (explicit grouping)
    condition2 = age >= 18 and (is_student or is_member)
    print(f"   age >= 18 and (is_student or is_member) = {condition2}")
    
    # Example 2: Login validation
    username = "alice"
    password = "secret123"
    is_admin = False
    
    # Complex validation
    valid_login = (len(username) >= 3 and len(password) >= 8) or is_admin
    
    print(f"\n2️⃣ Login Validation:")
    print(f"   Username: '{username}', Password: '{password}', Admin: {is_admin}")
    print(f"   Valid login: {valid_login}")
    
    # Example 3: Shopping discount
    total_amount = 150
    is_vip = False
    has_coupon = True
    
    # Discount eligibility
    gets_discount = (total_amount >= 100 and is_vip) or (has_coupon and total_amount >= 50)
    
    print(f"\n3️⃣ Shopping Discount:")
    print(f"   Amount: ${total_amount}, VIP: {is_vip}, Coupon: {has_coupon}")
    print(f"   Gets discount: {gets_discount}")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """
    Real-world applications of logical operators
    """
    print("\n🌟 PRACTICAL APPLICATIONS")
    print("=" * 30)
    
    # Application 1: User authentication system
    print("\n🔐 Application 1: User Authentication System")
    
    def authenticate_user(username, password, is_active=True, attempts_left=3):
        """Simple authentication function"""
        correct_username = "admin"
        correct_password = "password123"
        
        # Check all conditions
        valid_credentials = username == correct_username and password == correct_password
        can_attempt = attempts_left > 0
        account_active = is_active
        
        # Final authentication decision
        authenticated = valid_credentials and can_attempt and account_active
        
        print(f"   Username: '{username}' ({'✅' if username == correct_username else '❌'})")
        print(f"   Password: {'✅' if password == correct_password else '❌'}")
        print(f"   Account active: {'✅' if is_active else '❌'}")
        print(f"   Attempts left: {attempts_left} ({'✅' if attempts_left > 0 else '❌'})")
        print(f"   Authentication result: {'✅ Success' if authenticated else '❌ Failed'}")
        
        return authenticated
    
    # Test authentication
    authenticate_user("admin", "password123", True, 2)
    
    # Application 2: Grade calculator
    print(f"\n📊 Application 2: Grade Calculator")
    
    def calculate_grade(exam_score, homework_avg, attendance_rate):
        """Calculate final grade with multiple criteria"""
        
        # Grade criteria
        excellent = exam_score >= 90 and homework_avg >= 85 and attendance_rate >= 95
        good = exam_score >= 80 and homework_avg >= 75 and attendance_rate >= 90
        satisfactory = exam_score >= 70 and homework_avg >= 65 and attendance_rate >= 85
        passing = exam_score >= 60 or (homework_avg >= 80 and attendance_rate >= 90)
        
        print(f"   Exam Score: {exam_score}%")
        print(f"   Homework Average: {homework_avg}%")
        print(f"   Attendance Rate: {attendance_rate}%")
        
        if excellent:
            grade = "A"
        elif good:
            grade = "B"
        elif satisfactory:
            grade = "C"
        elif passing:
            grade = "D"
        else:
            grade = "F"
        
        print(f"   Final Grade: {grade}")
        return grade
    
    # Test grade calculation
    calculate_grade(88, 82, 96)
    
    # Application 3: Weather recommendation system
    print(f"\n🌤️  Application 3: Weather Recommendation System")
    
    def weather_recommendation(temperature, is_raining, wind_speed, humidity):
        """Provide clothing and activity recommendations"""
        
        # Weather conditions
        cold = temperature < 10
        warm = temperature >= 20 and temperature <= 30
        hot = temperature > 30
        
        # Activity recommendations
        indoor_day = is_raining or wind_speed > 30 or hot
        perfect_outdoor = not is_raining and warm and wind_speed < 15
        
        print(f"   Temperature: {temperature}°C")
        print(f"   Raining: {is_raining}")
        print(f"   Wind Speed: {wind_speed} km/h")
        print(f"   Humidity: {humidity}%")
        
        # Recommendations
        if cold and not is_raining:
            print("   🧥 Recommendation: Wear warm clothes, short outdoor activities")
        elif perfect_outdoor:
            print("   ☀️ Recommendation: Perfect for outdoor activities!")
        elif indoor_day:
            print("   🏠 Recommendation: Indoor activities recommended")
        else:
            print("   🌤️ Recommendation: Check conditions before going out")
    
    # Test weather recommendation
    weather_recommendation(25, False, 10, 60)

if __name__ == "__main__":
    """
    Main execution demonstrating all logical operator concepts
    """
    print(__doc__)
    
    # Run all demonstrations
    introduction_to_logical_operators()
    demonstrate_and_operator()
    demonstrate_or_operator()
    demonstrate_not_operator()
    demonstrate_combined_operators()
    practical_applications()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of all three logical operators (and, or, not)")
    print("✅ Knowledge of truth tables and operator behavior")
    print("✅ Mastery of operator precedence and combination")
    print("✅ Practical applications in real-world scenarios")
    print("✅ Complex condition construction and evaluation")
    
    print("\n💡 Key Takeaways:")
    print("• and operator: ALL conditions must be True")
    print("• or operator: AT LEAST ONE condition must be True")
    print("• not operator: Returns the OPPOSITE boolean value")
    print("• Operator precedence: not > and > or")
    print("• Use parentheses for complex conditions")
    print("• Short-circuit evaluation improves performance")
    
    print("\n🎯 Next Steps:")
    print("• Learn about comparison operators")
    print("• Practice with complex conditional statements")
    print("• Study De Morgan's laws for logical equivalence")
    print("• Explore bitwise operators for advanced logic")
# Using 'not' operator
if not a:
    print("a is False")
else:
    print("a is True")
# Example of logical operators with variables
x = 5
y = 10
# Check if x is greater than 0 and y is less than 20
if x > 0 and y < 20:
    print("x is greater than 0 and y is less than 20")
else:
    print("Either x is not greater than 0 or y is not less than 20")
# Check if x is less than 10 or y is greater than 5
if x < 10 or y > 5:
    print("Either x is less than 10 or y is greater than 5")
else:
    print("x is not less than 10 and y is not greater than 5")
# Check if x is not equal to 5
if not x == 5:
    print("x is not equal to 5")
    