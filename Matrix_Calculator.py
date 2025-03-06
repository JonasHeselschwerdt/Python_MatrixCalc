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

template = "Template.txt"
output_file = "Output_File.txt"  # defines the Template and the Outputfile for the UI

try:

    with open(template, "r", encoding="utf-8") as template_UI:  # opens Template.txt for reading purposes
        new_UI = template_UI.read()                             # reads Template.txt and stores it in new_UI

    with open(output_file, "w", encoding="utf-8") as User_Interface:     # opens Output_File.txt for writing purposes
        User_Interface.write(new_UI)                                     # writes the content of new_UI into Output_File

except:                                            
    print(f"Fehler: '{template}' wurde nicht gefunden.")       # Prints error message if file does not exist
