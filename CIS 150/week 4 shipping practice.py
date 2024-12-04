'''week 4 practice problem
shipping cost calculator
'''

#input parameters
weight = float(input("Enter the package weight in pounds "))
zone = int(input("Enter your zone number: 1, 2 or 3. "))



if weight < 5:
    cost = 5 + zone
elif weight >= 5 and weight <= 10:
        cost= 6 + 2*zone    
else:
        cost = 5 + 5*zone

print("Shipping your package will cost $", + cost)
      




      
