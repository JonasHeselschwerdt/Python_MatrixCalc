####################################################################
##                                                                ##
##      Matrixtaschenrechner                                      ##
##                                                                ##
####################################################################

# Authors: Moritz Wagner / Jonas Heselschwerdt
# Brief: Matrix Calculator for 3x3 Matrices

###############################################
##  Variables                                ##
###############################################
####################################################################
##  explanation                                                   ##
####################################################################

# "not in" checks, if the input is in the list, 
# seen in the function operation_...() 


####################################################################
##  Output File Preparation                                       ##
####################################################################

global matrix_A
global matrix_B
global matrix_C
global matrix_Ans
global matrix_Sol

matrix_A = []
matrix_B = []
matrix_C = []
matrix_Ans = []
matrix_Sol = []



template = "Template.txt"
output_file = "Output_File.txt"  # defines the Template and the Outputfile for the UI

################################################
##  UI Refreshing                             ##
################################################

def refreshUI():
    try:
        with open(template, "r", encoding="utf-8") as template_UI:  # opens Template.txt for reading purposes
            template_content = template_UI.read()                             
    except:                                            
        print(f"Error: '{template}' does not exist")       # Prints error message if file does not exist

    for z in range (3):
        for s in range (3):
            matrix_index = f"a{z+1}{s+1}"
            template_content = template_content.replace(matrix_index, str(f"{matrix_A[z][s]:.3f}"))
    for z in range (3):
        for s in range (3):
            matrix_index = f"b{z+1}{s+1}"
            template_content = template_content.replace(matrix_index, str(f"{matrix_B[z][s]:.3f}"))
    for z in range (3):
        for s in range (3):
            matrix_index = f"c{z+1}{s+1}"
            template_content = template_content.replace(matrix_index, str(f"{matrix_C[z][s]:.3f}"))
    for z in range (3):
        for s in range (3):
            matrix_index = f"z{z+1}{s+1}"
            template_content = template_content.replace(matrix_index, str(f"{matrix_Ans[z][s]:.3f}"))
    for z in range (3):
        for s in range (3):
            matrix_index = f"s{z+1}{s+1}"
            template_content = template_content.replace(matrix_index, str(f"{matrix_Sol[z][s]:.3f}"))
    try:
        with open (output_file,"w",encoding= "utf-8") as refreshed_UI:
            refreshed_UI.write(template_content)
    except: print(f"Error: ' {output_file} ' does not exist")


def introduction():     #introduce the program to the user
    print("Welcome, this programm will allow you to do some calculations with 3x3 matrices.")
    print("It will allow you to to addition, subtraction and multiplication with two matrices.")
    print("Firstly, you can fill in the matrices in the Output_file.txt. You need only to fill the needed matrices.")
    print("If you have done this, choose the operation in console of the proramm.")

introduction()

####################################################################
##  User input extractor                                          ##
####################################################################

def getMatrix(matrixname):  # is used to extract the matrices the user typed into the UI

    with open(output_file, "r", encoding="utf-8") as user_Interface:
        lines = user_Interface.readlines()# opens the User interface for reading purposes

    matrix = []

    if matrixname == "A":
        matrix_lines = lines[6:9]
    elif matrixname == "B":
        matrix_lines = lines[10:13]
    elif matrixname == "C":
        matrix_lines = lines[14:17]
    elif matrixname == "Ans":
        matrix_lines = lines[18:21]  # those are the line numbers of each matrix
    else:
        print("Error: No such matrix exists")
        return matrix  # return all zeros if the Matrix does not exist

    for line in matrix_lines:  # loops 3 times because there are 3 elements in the list matrix_lines
        line = line.strip().replace("(", "").replace(")", "").replace(matrixname,"").replace("=","") # Remove all Style Elements and spaces from the User Interface
    
        row = []       # Variable used to store one line each loop
   
        for value in line.split("|"):        # uses "|" as a divider for the elements in each line
            value = value.strip().replace(",", ".")  # adapts the numbers to international standards and removes spaces
            try:
                row.append(float(value))  # converts all Matrix Elements into floats
            except:
                row.append(0.000)  # if the number the user typed in does not make sense it will be replaced by 0

        matrix.append(row)  # the row gets added to the matrix_A array

    return matrix



####################################################################
##  User choose operation and the used matrices                   ##
####################################################################


def operation_operation():  # user chooses the operation
    print("Which operation you want to do?")
    status = False
    while status == False:      # checks if the the input is the expected 
        get_calculation[1] = input("You can choose between +, - and *: ")
        if get_calculation[1] not in ["+","-","*"]:
            print("Error: No operation like this exists")
            status = False
        else:
            status = True
            print("Your choosen operation is: " + get_calculation[1])

def operation_matrix1(): # user choose the first matrix
        status = False
        print("Which matrix do you choose for your operation?")
        while status == False:
            get_calculation[0] = input("You can choose between A, B and C: ")
            if get_calculation[0] not in ["A","B","C"]:     # checks if the the input is the expected
                print("Error: No matrix like this exists")
                status = False
            else: 
                status = True
                print("Your first matrix is: " + get_calculation[0])


def operation_matrix2(): #user choose the second matrix
        status = False
        print("Which is your second matrix, which you choose for your operation?")
        while status == False:
            get_calculation[2] = input("You can choose between A, B and C: ")       # checks if the the input is the expected
            if get_calculation[2] not in ["A","B","C"]:
                print("Error: No matrix like this exists")
                status = False
            else: 
                status = True
                print("Your second matrix is: " + get_calculation[2])

def operation():        # the user choose the operation and the matrices
    global get_calculation
    print("Matrix Calculator")
    get_calculation = [0,0,0]
    operation_operation()
    operation_matrix1()
    operation_matrix2()

operation()

####################################################################
##  calculation                                                   ##
####################################################################


def calculation(get_calculation):   # choose which function is needed for the operation and execute it
    matrix_1 = getMatrix(get_calculation[0])
    matrix_2 = getMatrix(get_calculation[2])
    operation = get_calculation[1]
    matrix_Ans = getMatrix("Ans")
    if operation == "*":
        multiplication(matrix_1, matrix_2)
        print("multiplication")         # optional
        print(matrix_Ans)
    if operation == "+":
        addition(matrix_1,matrix_2)
        print("adddition")              # optional
        print(matrix_Ans)
    if operation == "-":
        subtraction(matrix_1,matrix_2)
        print("subtraction")            # optional
        print(matrix_Ans)

def multiplication(matrix_1, matrix_2): # multiplication of two matrices
           # creates the matrix structure of 3x3, by reading Ans matrix
    for i in range(3):
        for j in range(3):
            matrix_sum = 0
            for k in range(3):
                matrix_sum += matrix_1[i][k] * matrix_2[k][j]
            matrix_Ans[i][j] = matrix_sum   # storing of part results in matrix_ans
    
def addition(matrix_1,matrix_2):    # addition of two matrices
    for i in range(3):
        for j in range(3):
            matrix_Ans[i][j] = matrix_1[i][j] + matrix_2[i][j]
def subtraction(matrix_1,matrix_2): # subtraction of two matrices
    for i in range(3):
        for j in range(3):
            matrix_Ans[i][j] = matrix_1[i][j] - matrix_2[i][j]

calculation(get_calculation)
