"""
BMI Calculator - Health and Fitness Mathematical Tool
==================================================

Comprehensive Body Mass Index (BMI) calculator with health categories,
recommendations, and detailed analysis. Demonstrates mathematical
calculations, health data processing, and user interaction.

Author: Python Learning Notes
Date: September 2025
Topic: BMI Calculation, Health Mathematics, Data Validation
"""

import math

# =============================================================================
# BMI FUNDAMENTALS AND THEORY
# =============================================================================

def explain_bmi_concept():
    """
    Educational explanation of BMI and its significance
    """
    print("⚕️ BODY MASS INDEX (BMI) CALCULATOR")
    print("=" * 40)
    
    print("\n📋 What is BMI?")
    print("Body Mass Index (BMI) is a measurement that:")
    print("   • Assesses body weight relative to height")
    print("   • Provides a general indication of body fat")
    print("   • Used for health screening and assessment")
    print("   • Helps identify weight-related health risks")
    
    print("\n📐 BMI Formula:")
    print("   BMI = weight (kg) ÷ (height (m))²")
    print("   BMI = weight (kg) ÷ height² (m²)")
    
    print("\n📊 BMI Categories (WHO Standards):")
    categories = [
        ("Underweight", "< 18.5", "May indicate malnutrition"),
        ("Normal weight", "18.5 - 24.9", "Healthy weight range"),
        ("Overweight", "25.0 - 29.9", "Above normal weight"),
        ("Obese Class I", "30.0 - 34.9", "Moderate obesity"),
        ("Obese Class II", "35.0 - 39.9", "Severe obesity"),
        ("Obese Class III", "≥ 40.0", "Very severe obesity")
    ]
    
    print("   ┌─────────────────┬─────────────┬─────────────────────────┐")
    print("   │ Category        │ BMI Range   │ Health Indication       │")
    print("   ├─────────────────┼─────────────┼─────────────────────────┤")
    for category, bmi_range, indication in categories:
        print(f"   │ {category:<15} │ {bmi_range:<11} │ {indication:<23} │")
    print("   └─────────────────┴─────────────┴─────────────────────────┘")

# =============================================================================
# INPUT VALIDATION FUNCTIONS
# =============================================================================

def get_weight():
    """
    Get and validate weight input from user
    """
    while True:
        try:
            weight = float(input("\n📏 Enter your weight in kilograms (kg): "))
            
            if weight <= 0:
                print("❌ Error: Weight must be a positive number!")
                continue
            elif weight > 1000:
                print("❌ Error: Weight seems unrealistic (> 1000 kg)!")
                continue
            
            return weight
            
        except ValueError:
            print("❌ Error: Please enter a valid number!")

def get_height():
    """
    Get and validate height input from user with unit options
    """
    print("\n📐 Height Input Options:")
    print("   1. Meters (e.g., 1.75)")
    print("   2. Centimeters (e.g., 175)")
    print("   3. Feet and inches (e.g., 5'9\")")
    
    while True:
        try:
            choice = input("\nChoose input format (1/2/3): ").strip()
            
            if choice == "1":
                height = float(input("Enter height in meters: "))
                if height <= 0 or height > 3:
                    print("❌ Error: Height must be between 0 and 3 meters!")
                    continue
                return height
                
            elif choice == "2":
                height_cm = float(input("Enter height in centimeters: "))
                if height_cm <= 0 or height_cm > 300:
                    print("❌ Error: Height must be between 0 and 300 cm!")
                    continue
                return height_cm / 100  # Convert to meters
                
            elif choice == "3":
                feet = int(input("Enter feet: "))
                inches = float(input("Enter inches: "))
                
                if feet < 0 or inches < 0 or feet > 10 or inches >= 12:
                    print("❌ Error: Invalid feet/inches values!")
                    continue
                
                # Convert to meters
                total_inches = feet * 12 + inches
                height_meters = total_inches * 0.0254
                return height_meters
                
            else:
                print("❌ Error: Please choose 1, 2, or 3!")
                
        except ValueError:
            print("❌ Error: Please enter valid numbers!")

# =============================================================================
# BMI CALCULATION FUNCTIONS
# =============================================================================

def calculate_bmi(weight, height):
    """
    Calculate BMI and return detailed results
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        dict: BMI calculation results
    """
    bmi = weight / (height ** 2)
    
    return {
        'bmi': bmi,
        'weight': weight,
        'height': height,
        'height_cm': height * 100,
        'category': get_bmi_category(bmi),
        'health_status': get_health_status(bmi),
        'recommendations': get_health_recommendations(bmi)
    }

def get_bmi_category(bmi):
    """
    Determine BMI category based on WHO standards
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    elif 30.0 <= bmi < 35.0:
        return "Obese Class I"
    elif 35.0 <= bmi < 40.0:
        return "Obese Class II"
    else:
        return "Obese Class III"

def get_health_status(bmi):
    """
    Get health status description based on BMI
    """
    if bmi < 18.5:
        return "May indicate malnutrition or other health issues"
    elif 18.5 <= bmi < 25.0:
        return "Healthy weight range with lower health risks"
    elif 25.0 <= bmi < 30.0:
        return "Above normal weight, increased health risks"
    elif 30.0 <= bmi < 35.0:
        return "Moderate obesity with significant health risks"
    elif 35.0 <= bmi < 40.0:
        return "Severe obesity with high health risks"
    else:
        return "Very severe obesity with very high health risks"

def get_health_recommendations(bmi):
    """
    Provide health recommendations based on BMI category
    """
    if bmi < 18.5:
        return [
            "🍎 Focus on gaining healthy weight",
            "💪 Consider strength training exercises",
            "👨‍⚕️ Consult healthcare provider for guidance",
            "🥗 Eat nutrient-rich, calorie-dense foods"
        ]
    elif 18.5 <= bmi < 25.0:
        return [
            "✅ Maintain current healthy weight",
            "🏃‍♂️ Continue regular physical activity",
            "🥗 Keep balanced, nutritious diet",
            "😴 Maintain good sleep and stress management"
        ]
    elif 25.0 <= bmi < 30.0:
        return [
            "🎯 Aim for gradual weight loss (1-2 lbs/week)",
            "🏃‍♂️ Increase physical activity",
            "🥗 Focus on portion control and healthy eating",
            "👨‍⚕️ Consider consulting a healthcare provider"
        ]
    else:  # BMI >= 30
        return [
            "🚨 Strongly consider medical consultation",
            "📋 Develop comprehensive weight loss plan",
            "👥 Consider support groups or counseling",
            "🩺 Monitor for obesity-related health conditions"
        ]

# =============================================================================
# ADVANCED BMI CALCULATIONS
# =============================================================================

def calculate_ideal_weight_range(height):
    """
    Calculate ideal weight range for normal BMI (18.5-24.9)
    """
    min_weight = 18.5 * (height ** 2)
    max_weight = 24.9 * (height ** 2)
    
    return min_weight, max_weight

def calculate_weight_difference(current_weight, height):
    """
    Calculate how much weight to lose/gain for normal BMI
    """
    min_ideal, max_ideal = calculate_ideal_weight_range(height)
    
    if current_weight < min_ideal:
        # Need to gain weight
        weight_to_gain = min_ideal - current_weight
        return f"gain {weight_to_gain:.1f} kg to reach normal BMI"
    elif current_weight > max_ideal:
        # Need to lose weight
        weight_to_lose = current_weight - max_ideal
        return f"lose {weight_to_lose:.1f} kg to reach normal BMI"
    else:
        return "already in normal BMI range"

def display_bmi_results(results):
    """
    Display comprehensive BMI calculation results
    """
    print("\n" + "=" * 50)
    print("📊 BMI CALCULATION RESULTS")
    print("=" * 50)
    
    # Basic information
    print(f"\n📏 Input Information:")
    print(f"   Weight: {results['weight']:.1f} kg")
    print(f"   Height: {results['height']:.2f} m ({results['height_cm']:.0f} cm)")
    
    # BMI calculation
    print(f"\n🔢 BMI Calculation:")
    print(f"   BMI = {results['weight']:.1f} ÷ ({results['height']:.2f})²")
    print(f"   BMI = {results['weight']:.1f} ÷ {results['height']**2:.4f}")
    print(f"   BMI = {results['bmi']:.2f}")
    
    # Category and status
    print(f"\n📋 BMI Analysis:")
    print(f"   Category: {results['category']}")
    print(f"   Health Status: {results['health_status']}")
    
    # Ideal weight range
    min_ideal, max_ideal = calculate_ideal_weight_range(results['height'])
    print(f"\n🎯 Ideal Weight Range:")
    print(f"   For normal BMI: {min_ideal:.1f} - {max_ideal:.1f} kg")
    
    # Weight difference
    weight_difference = calculate_weight_difference(results['weight'], results['height'])
    print(f"   To reach normal BMI: {weight_difference}")
    
    # Recommendations
    print(f"\n💡 Health Recommendations:")
    for recommendation in results['recommendations']:
        print(f"   {recommendation}")

# =============================================================================
# BMI COMPARISON AND TRACKING
# =============================================================================

def bmi_comparison_tool():
    """
    Compare BMI values and track changes
    """
    print(f"\n📈 BMI COMPARISON TOOL")
    print("=" * 30)
    
    # Get comparison data
    print("Enter data for comparison:")
    
    try:
        # Previous BMI
        prev_weight = float(input("Previous weight (kg): "))
        prev_height = float(input("Previous height (m): "))
        prev_bmi = prev_weight / (prev_height ** 2)
        
        # Current BMI  
        curr_weight = float(input("Current weight (kg): "))
        curr_height = float(input("Current height (m): "))
        curr_bmi = curr_weight / (curr_height ** 2)
        
        # Calculate changes
        weight_change = curr_weight - prev_weight
        bmi_change = curr_bmi - prev_bmi
        
        print(f"\n📊 Comparison Results:")
        print(f"   Previous BMI: {prev_bmi:.2f} ({get_bmi_category(prev_bmi)})")
        print(f"   Current BMI: {curr_bmi:.2f} ({get_bmi_category(curr_bmi)})")
        print(f"   Weight change: {weight_change:+.1f} kg")
        print(f"   BMI change: {bmi_change:+.2f}")
        
        # Progress assessment
        if abs(bmi_change) < 0.1:
            print("   📊 Status: BMI remained stable")
        elif bmi_change > 0:
            if prev_bmi < 18.5:
                print("   📈 Status: BMI increased (good if previously underweight)")
            else:
                print("   📈 Status: BMI increased")
        else:
            if prev_bmi > 25:
                print("   📉 Status: BMI decreased (good progress!)")
            else:
                print("   📉 Status: BMI decreased")
                
    except ValueError:
        print("❌ Error: Please enter valid numbers!")

# =============================================================================
# INTERACTIVE BMI CALCULATOR
# =============================================================================

def interactive_bmi_calculator():
    """
    Main interactive BMI calculator function
    """
    print("🏥 INTERACTIVE BMI CALCULATOR")
    print("=" * 35)
    
    while True:
        try:
            print("\n🎯 Choose an option:")
            print("   1. Calculate BMI")
            print("   2. BMI comparison tool")
            print("   3. View BMI information")
            print("   4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                # Get user input
                weight = get_weight()
                height = get_height()
                
                # Calculate BMI
                results = calculate_bmi(weight, height)
                
                # Display results
                display_bmi_results(results)
                
            elif choice == "2":
                bmi_comparison_tool()
                
            elif choice == "3":
                explain_bmi_concept()
                
            elif choice == "4":
                print("\n👋 Thank you for using the BMI Calculator!")
                break
                
            else:
                print("❌ Error: Please choose a valid option (1-4)!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

# =============================================================================
# EXAMPLE CALCULATIONS
# =============================================================================

def demonstrate_bmi_examples():
    """
    Demonstrate BMI calculations with sample data
    """
    print("\n🎯 BMI CALCULATION EXAMPLES")
    print("=" * 35)
    
    # Sample data for different categories
    examples = [
        {"name": "Underweight Example", "weight": 50, "height": 1.75},
        {"name": "Normal Weight Example", "weight": 65, "height": 1.70},
        {"name": "Overweight Example", "weight": 80, "height": 1.65},
        {"name": "Obese Example", "weight": 100, "height": 1.60}
    ]
    
    for example in examples:
        print(f"\n📋 {example['name']}:")
        results = calculate_bmi(example['weight'], example['height'])
        print(f"   Weight: {results['weight']} kg")
        print(f"   Height: {results['height']} m")
        print(f"   BMI: {results['bmi']:.2f}")
        print(f"   Category: {results['category']}")

if __name__ == "__main__":
    """
    Main execution block
    """
    print(__doc__)
    
    # Show BMI concept explanation
    explain_bmi_concept()
    
    # Show examples
    demonstrate_bmi_examples()
    
    # Start interactive calculator
    interactive_bmi_calculator()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of BMI concept and calculation")
    print("✅ Knowledge of health categories and implications")
    print("✅ Input validation and error handling")
    print("✅ Mathematical formula implementation")
    print("✅ Health data interpretation and recommendations")
    
    print("\n💡 Key Concepts Learned:")
    print("• BMI formula: weight(kg) ÷ height²(m²)")
    print("• Health category classification")
    print("• Data validation and user interaction")
    print("• Mathematical problem solving")
    print("• Health informatics applications")
    
    print("\n🎯 Next Steps:")
    print("• Learn about other health metrics (body fat %, muscle mass)")
    print("• Explore data visualization for health tracking")
    print("• Study statistical analysis of health data")
    print("• Implement more advanced health calculators")
