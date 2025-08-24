# write a program to calculate the body mass index (BMI)
#concept
# The Body Mass Index (BMI) is a measure of body fat based on height and weight.
# It is calculated using the formula: BMI = weight (kg) / (height (m) * height (m))
w = float(input("Enter the weight in kg: "))
h = float(input("Enter the height in meters: "))
bmi = w / (h * h)
print("The Body Mass Index (BMI) is: ", bmi)
