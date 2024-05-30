def invert_student_courses(student_courses):
    # Print the original dictionary
    print("Original Dictionary:", student_courses)
    
    # Initialize an empty dictionary for the inverted result
    course_students = {}
    
    # Iterate through the student-courses dictionary
    for student, courses in student_courses.items():
        # Iterate through each course in the student's course list
        for course in courses:
            # If the course is not already a key in the inverted dictionary, add it with an empty list
            if course not in course_students:
                course_students[course] = []
            # Append the student to the list of students for this course
            course_students[course].append(student)
    
    # Print the inverted dictionary
    print("Inverted Dictionary:", course_students)
    return course_students

# Sample input
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Call the function with the sample input and store the output
inverted_courses = invert_student_courses(student_courses)
