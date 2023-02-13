"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

employeee_data = open("employee_data.csv", "r")
reader = csv.reader(employeee_data)

# create an empty dictionary

Employee_Dict = {}

# use a loop to iterate through the csv file

for row in employeee_data:
    print(row)

    # check if the employee fits the search criteria


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout

for row in employeee_data:
    if row[4] == "CSR":
        Employee_Dict["Full Name"] = employeee_data[1] + [2]
        Employee_Dict["Current Salary"] = employeee_data[5]
        Employee_Dict["New Salary"] = employeee_data[5] * 1.1

# print(employeee_data)

for row in employeee_data:
    if row[4] == "CSR":
        print(
            f"Manager Name:"[Employee_Dict]["Full Name"],
            "Current Salary:"[Employee_Dict]["Current Salary"],
        )
        print()
        print("=========================================")
        print()
        print(
            f"Manager Name:"[Employee_Dict]["Full Name"],
            "New Salary:"[Employee_Dict]["New Salary"],
        )
