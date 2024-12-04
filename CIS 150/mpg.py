'''Program finds the miles per gallon for your car.
Liz VM
May 5, 24'''

miles = float(input("How many miles did you drive on the trip?"))
gallons = float(input("How many gallons did you use on this drive?"))

print(f"You drove: {miles} miles")
print(f"You used: {gallons} gallons")

mpg = miles / gallons

print(f"Your average miles per gallon on this trip was {mpg}.")



