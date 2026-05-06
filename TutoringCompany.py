#Scenario: You’re a junior developer at a tutoring company
#Your manager says:“We need a simple system that saves student names into a file, then lets us view all the students later.”
#That is where file handling comes in.

#===========================================================================================================================

# Student Register System
# This program lets us save student names into a text file
# and read the saved students later.

# Ask the user to enter a student's name
student_name = input("Enter student name: ")

# Open the file in append mode
# "a" means add new content without deleting old content
file = open("TutoringStudents.txt", "a")

# Write the student's name into the file
# \n moves the next student onto a new line
file.write(student_name + "\n")

# Always close the file after writing
file.close()

print("Student saved successfully!")


# Now we read the file to show all saved students
file = open("students.txt", "r")

print("\nCurrent student list:")

# Go through the file line by line
for line in file:
    print("- " + line.strip())

# Close the file after reading
file.close()