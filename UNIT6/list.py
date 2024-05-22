#List of employees
employees = ['John', 'Jane', 'Jack', 'Janice', 'James', 'Judy', 'Nobel', 'Nancy', 'Nathan', 'Nina']
#printing the lenght of the list to ensure that it is exactly 10
print(len(employees))
#Slicing the list to make two sublists
subList1 = employees[:5]
subList2 = employees[5:]
print(subList1)
#Appending/adding a new employee to the first sublist
subList2.append('Kriti Brown')
print(subList2)
#Removing the second employee from the first sublist
del subList1[1]
print(subList1)
#Merging the two sublists to form a new list called mergedList
mergedList = subList1 + subList2
print(mergedList)
#List of salaries
salaryList = [2300, 2000, 5000, 4000, 9000, 5500, 4500, 10000, 8800, 7400]
updatedSalary = [salary * 1.04 for salary in salaryList]
#Printing the initial and updated salary list to compare the difference
print(f"Initial Salary:{salaryList}")
print(f"Updated Salary:{updatedSalary}")

sortedSalary = sorted(updatedSalary)
print(f"Sorted Salary:{sortedSalary}")

#top3 salaries
top3 = sortedSalary[-3:]