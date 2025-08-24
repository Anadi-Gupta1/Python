# write a program to input a value in tones and conver it into quantal and kg
a = int(input("Enter the value in tones: "))
b = 1000 * a  # 1 tone = 1000 kg
c = 1000000 * a  # 1 tone = 1000000 grams
print("The value in kg is: ", b)
print("The value in grams is: ", c)
