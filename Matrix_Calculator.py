################################################
##                                            ##
##      Matrixtaschenrechner                  ##
##                                            ##
################################################

# Authors: Moritz Wagner / Jonas Heselschwerdt
# Brief: Matrix Calculator for 3x3 Matrices


# Note: In this current state the order of the subprograms does not make sense, they must be rearranged later
# (and put into functions)

################################################
##  Output File Preparation                   ##
################################################


template = "Template.txt"
output_file = "Output_File.txt"  # defines the Template and the Outputfile for the UI

"""
try:

    with open(template, "r", encoding="utf-8") as template_UI:  # opens Template.txt for reading purposes
        new_UI = template_UI.read()                             # reads Template.txt and stores it in new_UI

    with open(output_file, "w", encoding="utf-8") as user_Interface:     # opens Output_File.txt for writing purposes
        user_Interface.write(new_UI)                                     # writes the content of new_UI into Output_File

except:                                            
    print(f"Fehler: '{template}' wurde nicht gefunden.")       # Prints error message if file does not exist

"""
#################################################
##  User input extractor                       ##
#################################################
def location_matrix():
    global lines_matrix_left, lines_matrix_right
    lines_matrix_left = [6, 10, 14]
    lines_matrix_right = [9, 13, 17]
def matrix_reading():
    global matrix_A, matrix_B, matrix_C, matrixes
    matrix_A = []  # the array matrix_A contains the matrix A the user typed in in a easy to work with format
    matrix_B = []  # the array matrix_B contains the matrix B the user typed in in a easy to work with format
    matrix_C = []  # the array matrix_C contains the matrix C the user typed in in a easy to work with format
    matrixes = ["A","B","C"]
    for matrix_counter in range(3):  # loops 3 times because there are 3 matrices
        print("Matrix: ", matrixes[matrix_counter])
        with open(output_file, "r", encoding="utf-8") as user_Interface:
            lines = user_Interface.readlines() # opens the User interface for reading purposes

        matrix_lines = lines[lines_matrix_left[matrix_counter]:lines_matrix_right[matrix_counter]] # limits lines, which contains all 33 lines of the user interface to lines 7 to 9

        
        for line in matrix_lines:  # loops 3 times because there are 3 elements in the list matrix_lines
            line = line.strip().replace("(", "").replace(")", "").replace("A","").replace("=","") # Remove all Style Elements and spaces from the User Interface
            
            row = []       # Variable used to store one line each loop
        
            for value in line.split("|"):        # uses "|" as a divider for the elements in each line
                value = value.strip().replace(",", ".")  # adapts the numbers to international standards and removes spaces
                try:
                    row.append(float(value))  # converts all Matrix Elements into floats
                except:
                    row.append(0.000)  # if the number the user typed in does not make sense it will be replaced by 0

            if row and matrix_counter == 0:
                matrix_A.append(row)  # the row gets added to the matrix_A array
            if row and matrix_counter == 1:
                matrix_B.append(row)  # the row gets added to the matrix_B array
            if row and matrix_counter == 2:
                matrix_C.append(row)  # the row gets added to the matrix_C array

        if matrix_counter == 0:
            for row in matrix_A:  # prints the matrix out for testing purposes
                print(row)
        if matrix_counter == 1:
            for row in matrix_B:  # prints the matrix out for testing purposes
               print(row)
        if matrix_counter == 2:
            for row in matrix_C:  # prints the matrix out for testing purposes
                print(row)
        print("")

location_matrix()	

matrix_reading()

print("Matrix A: ", matrix_A)
print("Matrix B: ", matrix_B)
print("Matrix C: ", matrix_C)