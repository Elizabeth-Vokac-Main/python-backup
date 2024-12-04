'''
BMR calculator tool for Basal Metabolic Rate
Liz Vokac Main
May 14, 2024
Finds daily calorie estimation based on gender
'''

#input
weight = float(input('enter your weight in kilograms'))
height = float(input('enter your height in centimeters'))
age = int(input('enter your age in years'))
gender = input('enter m for male or f for female')

#conditions
if gender == 'm':
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
elif gender == "f":
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
else:
    bmr = "invalid gender"

#output
print("Basal Metabolic Rate (BMR)=", bmr)
