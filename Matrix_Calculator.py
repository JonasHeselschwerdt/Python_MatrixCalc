################################################
##                                            ##
##      Matrixtaschenrechner                  ##
##                                            ##
################################################

# Authors: Moritz Wagner / Jonas Heselschwerdt
# Brief: Matrix Calculator for 3x3 Matrices

################################################
##  Output File Preparation                   ##
################################################

# Note: In this current state the order of the subprograms does not make sense, they must be rearranged later
# (and put into functions)

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

with open(output_file, "r", encoding="utf-8") as user_Interface:
    lines = user_Interface.readlines() # opens the User interface for reading purposes

matrix_lines = lines[6:9] # limits lines, which contains all 33 lines of the user interface to lines 7 to 9

matrix_A = []  # the array matrix_A contains the matrix A the user typed in in a easy to work with format

for line in matrix_lines:  # loops 3 times because there are 3 elements in the list matrix_lines
    line = line.strip().replace("(", "").replace(")", "").replace("A","").replace("=","") # Remove all Style Elements and spaces from the User Interface
    
    row = []       # Variable used to store one line each loop
   
    for value in line.split("|"):        # uses "|" as a divider for the elements in each line
        value = value.strip().replace(",", ".")  # adapts the numbers to international standards and removes spaces
        try:
            row.append(float(value))  # converts all Matrix Elements into floats
        except:
            row.append(0.000)  # if the number the user typed in does not make sense it will be replaced by 0

    if row:
        matrix_A.append(row)  # the row gets added to the matrix_A array

for row in matrix_A:  # prints the matrix out for testing purposes
    print(row)