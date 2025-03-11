####################################################################
##                                                                ##
##      Matrixtaschenrechner                                      ##
##                                                                ##
####################################################################

# Authors: Moritz Wagner / Jonas Heselschwerdt
# Brief: Matrix Calculator for 3x3 Matrices

##############################################################
## Important Notes about this version                       ##
##############################################################

# This is the first version of the final product. It has all the basic functions we 
# envisioned. As we still have plenty of time left for the project we will soon be adding a function to
# calculate the determinants of each matrix, as well as the Eigenvalues. We also still need to add functionalities
# that make the program foolproof in case the user types in something that doesnt make sense.
# We also need to add a help menue that informs the user about how to correctly use the program.
# The main program should also be put into a loop so the program doesnt have to be restarted every time
# someone wants to calculate something

###############################################
##  Variables                                ##
###############################################

# here are all of the variables that the program needs:

global matrix_A   
global matrix_B
global matrix_C
global matrix_Ans
global matrix_Sol

det_A, det_B, det_C, det_Ans, det_Sol = 0, 0 ,0 ,0, 0

matrix_A = []
matrix_B = []
matrix_C = []
matrix_Ans = []
matrix_Sol = []   # The Matrices are stored as global Variables so they can be accessed directly inside a Fucntion

matrix_Operand_1 = []
matrix_Operand_2 = []   # those variables are used to temporarily save the Operands

global calculated
global matrix_saved_in

calculated = ""
matrix_saved_in = "" # strings used to save the performed calculation and the matrix where the solution goes 
                     # they are used in refreshUI() to show the User what exactly the program did

template = "Template.txt"
output_file = "Output_File.txt"  # defines the Template and the Outputfile for the UI
                                 # they need to be in the same folder as the main python program


################################################
##  UI Refreshing                             ##
################################################

# here is a function that will print all the matrices, as well as other information out in Output_File.txt
# it does that by completely overwriting Output_File and uses Template.txt as a reference

def refreshUI():
    try:
        with open(template, "r", encoding="utf-8") as template_UI:  # opens Template.txt for reading purposes
            template_content = template_UI.read()                             
    except:                                            
        print(f"Error: '{template}' does not exist")       # Prints error message if file does not exist

    for z in range (3):
        for s in range (3):
            matrix_index = f"a{z+1}{s+1}"

            # Autoscaling:

            if abs(matrix_A[z][s]) >= 1000:
                digits = 4
            elif abs(matrix_A[z][s]) >= 100:
                digits = 3
            elif abs(matrix_A[z][s]) >= 10:
                digits = 2
            else:
                digits = 1
         
            if matrix_A[z][s] >= 0:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_A[z][s]:.{4-digits}f}"))
                else:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_A[z][s]:.{4-digits}f} "))                    
            else:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f"{matrix_A[z][s]:.{4-digits}f}"))
                else: 
                    template_content = template_content.replace(matrix_index, str(f"{matrix_A[z][s]:.{4-digits}f} "))                   

    for z in range (3):
        for s in range (3):
            matrix_index = f"b{z+1}{s+1}"

            # Autoscaling:
            
            if abs(matrix_B[z][s]) >= 1000:
                digits = 4
            elif abs(matrix_B[z][s]) >= 100:
                digits = 3
            elif abs(matrix_B[z][s]) >= 10:
                digits = 2
            else:
                digits = 1
         
            if matrix_B[z][s] >= 0:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_B[z][s]:.{4-digits}f}"))
                else:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_B[z][s]:.{4-digits}f} "))                    
            else:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f"{matrix_B[z][s]:.{4-digits}f}"))
                else: 
                    template_content = template_content.replace(matrix_index, str(f"{matrix_B[z][s]:.{4-digits}f} ")) 

    for z in range (3):
        for s in range (3):
            matrix_index = f"c{z+1}{s+1}"

            # Autoscaling:
            
            if abs(matrix_C[z][s]) >= 1000:
                digits = 4
            elif abs(matrix_C[z][s]) >= 100:
                digits = 3
            elif abs(matrix_C[z][s]) >= 10:
                digits = 2
            else:
                digits = 1
         
            if matrix_C[z][s] >= 0:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_C[z][s]:.{4-digits}f}"))
                else:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_C[z][s]:.{4-digits}f} "))                    
            else:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f"{matrix_C[z][s]:.{4-digits}f}"))
                else: 
                    template_content = template_content.replace(matrix_index, str(f"{matrix_C[z][s]:.{4-digits}f} ")) 

    for z in range (3):
        for s in range (3):
            matrix_index = f"z{z+1}{s+1}"

            # Autoscaling:
            
            if abs(matrix_Ans[z][s]) >= 1000:
                digits = 4
            elif abs(matrix_Ans[z][s]) >= 100:
                digits = 3
            elif abs(matrix_Ans[z][s]) >= 10:
                digits = 2
            else:
                digits = 1
         
            if matrix_Ans[z][s] >= 0:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_Ans[z][s]:.{4-digits}f}"))
                else:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_Ans[z][s]:.{4-digits}f} "))                    
            else:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f"{matrix_Ans[z][s]:.{4-digits}f}"))
                else: 
                    template_content = template_content.replace(matrix_index, str(f"{matrix_Ans[z][s]:.{4-digits}f} ")) 

    for z in range (3):
        for s in range (3):
            matrix_index = f"s{z+1}{s+1}"

            # Autoscaling:
            
            if abs(matrix_Sol[z][s]) >= 1000:
                digits = 4
            elif abs(matrix_Sol[z][s]) >= 100:
                digits = 3
            elif abs(matrix_Sol[z][s]) >= 10:
                digits = 2
            else:
                digits = 1
         
            if matrix_Sol[z][s] >= 0:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_Sol[z][s]:.{4-digits}f}"))
                else:
                    template_content = template_content.replace(matrix_index, str(f" {matrix_Sol[z][s]:.{4-digits}f} "))                    
            else:
                if digits != 4:
                    template_content = template_content.replace(matrix_index, str(f"{matrix_Sol[z][s]:.{4-digits}f}"))
                else: 
                    template_content = template_content.replace(matrix_index, str(f"{matrix_Sol[z][s]:.{4-digits}f} ")) 

    # the above for loops systematically loop through all of the placeholders in template.txt and replace the 
    # placeholders with the values calculated (placeholders like a11 -> a33, b11 -> b33 etc.)
    # we check how many decimal places the values have and if they are negative, this
    # information is used to autoscale the matrices nicely
    # this works for numbers up to 9999
    
    template_content = template_content.replace("ACTION",calculated)
    template_content = template_content.replace("Svd",matrix_saved_in)  # the performed calculation and matrix_saved_in
                                                                        # are displayed for the user in the UI

    try:
        with open (output_file,"w",encoding= "utf-8") as refreshed_UI:
            refreshed_UI.write(template_content)
    except: print(f"Error: ' {output_file} ' does not exist")  # here we overwrite what is in Output_File.txt with the
                                                               # modified Template


####################################################################
##  Calculation                                                   ##
####################################################################

# here the actual calculations happens, calculate() checks the operator and correctly instructs
# either addition(), subtraction() or multiplication() to start
# those functions will then perform the correct calculation algorithm and overwrite matrix_Sol with the solution


def calculate(operand_1,operand_2,operator):   # chooses which function is needed for the operation and execute it

    if operator == "*":
        multiplication(operand_1, operand_2)

    if operator == "+":
        addition(operand_1,operand_2)
 
    if operator == "-":
        subtraction(operand_1,operand_2)


def multiplication(operand_1, operand_2): # multiplication of two matrices

    for i in range(3):
        for j in range(3):
            matrix_sum = 0
            for k in range(3):
                matrix_sum += operand_1[i][k] * operand_2[k][j]
            matrix_Sol[i][j] = matrix_sum   # the Solution is always stored in Matrix_Sol
    
def addition(operand_1,operand_2):    # addition of two matrices
    for i in range(3):
        for j in range(3):
            matrix_Sol[i][j] = operand_1[i][j] + operand_2[i][j]  # the Solution is always stored in Matrix_Sol

def subtraction(operand_1,operand_2): # subtraction of two matrices
    for i in range(3):
        for j in range(3):
            matrix_Sol[i][j] = operand_1[i][j] - operand_2[i][j]  # the Solution is always stored in Matrix_Sol


def determinant():
    det_matrices = [matrix_A, matrix_B, matrix_C, matrix_Ans, matrix_Sol]
    det = [det_A, det_B, det_C, det_Ans, det_Sol]
    for i in range(5):
        det[i] = det_matrices[i][0][0] * det_matrices[i][1][1] * det_matrices[i][2][2] + det_matrices[i][0][1] * det_matrices[i][1][2] * det_matrices[i][2][0] + det_matrices[i][0][2] * det_matrices[i][1][0] * det_matrices[i][2][1] - det_matrices[i][0][2] * det_matrices[i][1][1] * det_matrices[i][2][0] - det_matrices[i][0][1] * det_matrices[i][1][0] * det_matrices[i][2][2] - det_matrices[i][0][0] * det_matrices[i][1][2] * det_matrices[i][2][1]



####################################################################
##  Matrix input extractor                                        ##
####################################################################

# here we extract all the matrices that the user typed in
# and return it as a 3x3 array

def getMatrix(matrixname):  # is used to extract the matrices the user typed into the UI

    with open(output_file, "r", encoding="utf-8") as user_Interface:
        lines = user_Interface.readlines()    # opens the User interface for reading purposes

    matrix = []

    if matrixname == "A":
        matrix_lines = lines[6:9]
    elif matrixname == "B":
        matrix_lines = lines[10:13]
    elif matrixname == "C":
        matrix_lines = lines[14:17]
    elif matrixname == "Ans":
        matrix_lines = lines[18:21]  
    elif matrixname == "Sol":
        matrix_lines = lines[26:29]   # the locations of the Matrices in Output_File is being defined
        
    else:
        print("Error: No such matrix exists")
        return matrix  # return all zeros if the Matrix does not exist

    for line in matrix_lines:  
        line = line.strip().replace("(", "").replace(")", "").replace(matrixname,"").replace("=","") 
        # Remove all Style Elements and spaces from the User Interface, only the numbers, seperated by "|" remain

        row = []       # Variable used to store one row each loop
   
        for value in line.split("|"):        # uses "|" as a divider for the elements in each line
            value = value.strip().replace(",", ".")  # adapts the numbers to international standards (decimal point)
                                                     #  and removes spaces
            try:
                row.append(float(value))  # converts all Matrix Elements into floats
            except:
                row.append(0.000)  # if the number the user typed in does not make sense it will be replaced by 0

        matrix.append(row)  # the row gets added to the matrix array which getMatrix returns

    return matrix

############################################
##    User Input Extractor                ##
############################################

# here we ask the user what calculation he wants to perform, and return all the needed information as a list

def getUserInput():
    userInput = [0,0,0,0]
    
    status = [False,False,False,False]
    while not all(status):
        if status[0] == False:
            userInput[0] = input("Which Operator do you want to use? Type '?' to open the help menue! You can choose between +, - and *: ")
            if userInput[0] not in ["+","-","*"]:
                print("Error: No Operator like this exists")
            else:
                status[0] = True
        if status[1] == False:
            userInput[1] = input("What is the first Operand? You can choose between A, B, C: ")
            if userInput[1] not in ["A","B","C"]:
                print("Error: No Operand like this exists")
            else:
                status[1] = True
        if status[2] == False:
            userInput[2] = input("What is the second Operand? You can choose between A, B, C: ")
            if userInput[2] not in ["A","B","C"]:
                print("Error: No Operand like this exists")
            else:
                status[2] = True
        if status[3] == False:
            userInput[3] = input("Where do you want to save the solution? You can choose between A, B, C, Ans: ")
            if userInput[3] not in ["A","B","C","Ans",""]:
                print("Error: No Operand like this exists")
                print("If you type nothing Ans will be used to save the Solution")
            else:
                status[3] = True
    return userInput


    # this function asks the user about what calculation to perform and returns it a list containing all the
    # needed information

#############################################
##    Main Programm                        ##
#############################################

# This is the main program of the calculator, which makes use of all the defined functions and variables

userInput = getUserInput()  #find out what the user wants to do
operator = userInput[0]     
op_1 = userInput[1]
op_2 = userInput[2]
saved_in = userInput[3]    # store the instructions in seperate variables

matrix_A = getMatrix("A")
matrix_B = getMatrix("B")
matrix_C = getMatrix("C")
matrix_Ans = getMatrix("Ans")
matrix_Sol = getMatrix("Sol")    # acquire the matrices the user typed in


if op_1 == "A":
    matrix_Operand_1 = matrix_A
elif op_1 == "B":
    matrix_Operand_1 = matrix_B
elif op_1 == "C":
    matrix_Operand_1 = matrix_C
elif op_1 == "Ans":
    matrix_Operand_1 = matrix_Ans
else:
    matrix_Operand_1 = matrix_A

if op_2 == "A":
    matrix_Operand_2 = matrix_A
elif op_2 == "B":
    matrix_Operand_2 = matrix_B
elif op_2 == "C":
    matrix_Operand_2 = matrix_C
elif op_2 == "Ans":
    matrix_Operand_2 = matrix_Ans
else:
    matrix_Operand_2 = matrix_B    # assigned the two operands correctly

calculate(matrix_Operand_1,matrix_Operand_2,operator)  # perform the calculation by giving the calculate function 
                                                       # the two operands ant the operator
                                                      
if saved_in == "A":
    matrix_A = matrix_Sol
elif saved_in == "B":
    matrix_B = matrix_Sol
elif saved_in == "C":
    matrix_C = matrix_Sol
else:
    matrix_Ans = matrix_Sol     # copy the solution (always stored in matrix_Solution) into the matrix the user defined
                                # if the user didnt specify the matrix where the solution goes, matrix_Ans will 
                                # be used by default

determinant()

calculated = op_1 + " " + operator + " " + op_2
matrix_saved_in = saved_in    # update the variables to show the user the calculation performed and 
                              # where the solution has been saved

refreshUI()   # as the last step of the program everything will be displayed  for the user in Output_File.txt
