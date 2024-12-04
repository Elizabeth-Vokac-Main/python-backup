

import os
os.system('cls')

#control break example
sales_data = [['north', 10], ['south', 20], ['east', 30],
              ['north', 12], ['south', 22], ['east', 32],
              ['north', 15], ['south', 25], ['east', 35]]

#sort the data
sorted_sales_data = sorted(sales_data)

#initialize variables
current_region = None
total_sales = 0

#control break detection
for each_element in sorted_sales_data:
    if each_element[0] != current_region:
        if current_region is not None:
            print(f"Total sales for, {current_region}: {total_sales}")
            print("_________________________________________________")
        current_region = each_element[0]
        total_sales = 0
    total_sales += each_element[1]

print(f"Total Sales for {current_region}: {total_sales}")
