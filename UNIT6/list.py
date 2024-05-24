def listfun():
    #List of employees
    employees = ['John', 'Jane', 'Jack', 'Janice', 'James', 'Judy', 'Nobel', 'Nancy', 'Nathan', 'Nina']
    #printing the lenght of the list to ensure that it is exactly 10
    print(str(len(employees))+ "\n")
    #Slicing the list to make two sublists
    subList1 = employees[:5]
    subList2 = employees[5:]
    print(subList1)
    #Appending/adding a new employee to the first sublist
    subList2.append('Kriti Brown')
    print(f"\nUpdated sublist2{subList2}")
    #Removing the second employee from the first sublist, you can use pop, remove or del keyword
    del subList1[1] #we use the index of the employee when using the del keyword

    #****uncomment the line below to see the effect of using the pop and remove keyword
    #subList1.pop(1) #we use the index of the employee when using the pop keyword
    #subList1.remove('Jane') #we use the exact name of the employee when using the remove keyword

    print(f'\nSublist1 after removing the seconf element:{subList1}')

    #Merging the two sublists to form a new list called mergedList
    mergedList = subList1 + subList2
    print(f'\nMerged List: {mergedList}')


    #List of salaries
    salaryList = [2300, 2000, 5000, 4000, 9000, 5500, 4500, 10000, 8800, 7400]
    updatedSalary = [salary * 1.04 for salary in salaryList]
    #Printing the initial and updated salary list to compare the difference
    print(f"\nInitial Salary:{salaryList}")
    print(f"\nUpdated Salary:{updatedSalary}")
    #Sorting the updated salary list
    sortedSalary = sorted(updatedSalary)
    print(f"\nSorted Salary:{sortedSalary}")
    #Printing the top 3 salaries
    top3 = sortedSalary[-3:]
    print(f"\nTop 3 Salaries:{top3}")
listfun()
