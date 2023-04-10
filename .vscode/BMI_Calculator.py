while True:
    height = input("Enter your height in feet:")
    if height.replace(".", "", 1).isdigit() and float(height) > 0:
        break
    else:
        print("Height cannot be less than or equal to 0 or contain special characters")

while True:
    weight = input("Enter your weight in kg:")
    if weight.replace(".", "", 1).isdigit() and float(weight) > 0:
        break
    else:
        print("Weight cannot be less than or equal to 0 or contain special characters")

bmi = float(weight)/(float(height)/3.281)**2
bmi_rounded = round(bmi, 1)

print("Your BMI is:", bmi_rounded)
if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi_rounded < 25:
    print("You have Normal weight")
elif 25 <= bmi_rounded < 30:
    print("You are Overweight")
else:
    print("You have Obesity")
