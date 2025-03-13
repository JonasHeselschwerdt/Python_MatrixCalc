####################################################################
##                                                                ##
##      3x3 Matrixcalculator                                      ##
##                                                                ##
####################################################################

# Authors: Moritz Wagner / Jonas Heselschwerdt
# Brief: Matrix Calculator for 3x3 Matrices


####################################################################
##      Important Notes about this version                        ##
####################################################################

# This is the Alpha Version of the programm
# Unless there are any bugs in this version, it can be considered final
# some variable names might still change later for better readability
# some comments are still missing at getUserInput()


####################################################################
##      Variables                                                 ##
####################################################################

# here are all of the variables that the program needs:

global matrix_A   
global matrix_B
global matrix_C
global matrix_Ans
global matrix_Sol

global det_A, det_B, det_C, det_Ans, det_Sol

det_A, det_B, det_C, det_Ans, det_Sol = 0, 0 ,0 ,0, 0

matrix_A = [[0,0,0],[0,0,0],[0,0,0]]
matrix_B = [[0,0,0],[0,0,0],[0,0,0]]
matrix_C = [[0,0,0],[0,0,0],[0,0,0]]
matrix_Ans = [[0,0,0],[0,0,0],[0,0,0]]
matrix_Sol = [[0,0,0],[0,0,0],[0,0,0]]   # The Matrices are stored as global Variables so they can be accessed directly inside a Fucntion

matrix_Operand_1 = [[0,0,0],[0,0,0],[0,0,0]]
matrix_Operand_2 = [[0,0,0],[0,0,0],[0,0,0]]  # those variables are used to temporarily save the Operands

global calculated
global matrix_saved_in

calculated = ""
matrix_saved_in = "" # strings used to save the performed calculation and the matrix where the solution goes 
                     # they are used in refreshUI() to show the User what exactly the program did

help_menue = "Template_HelpMenue.txt"
template = "Template.txt"
output_file = "Output_File.txt"  # defines the .txt documents that we need for reference and as UI
                                 # they need to be in the same folder as the main python program


####################################################################
##      UI Refreshing                                             ##
####################################################################

# here is a function that will print all the matrices, as well as other information out in Output_File.txt
# it does that by completely overwriting Output_File and uses Template.txt as a reference

def refreshUI():

    try:
        with open(template, "r", encoding="utf-8") as template_UI:  # opens Template.txt for reading purposes
            template_content = template_UI.read()                             
    except:                                            
        print(f"Error: '{template}' does not exist")       # Prints error message if file does not exist

    for i in range(5):                                                      # this for loop is used to autoscale the numbers within the matrices
        letters = ["a","b","c","z","s"]                                     # it does that by checking how many digits the number has and if its
        matrices = [matrix_A, matrix_B, matrix_C, matrix_Ans, matrix_Sol]   # positive or negative
        for j in range (3):
            for k in range (3):
                matrix_index = f"{letters[i]}{j+1}{k+1}"
                if abs(matrices[i][j][k]) >= 1000:
                    digits = 4
                elif abs(matrices[i][j][k]) >= 100:
                    digits = 3
                elif abs(matrices[i][j][k]) >= 10:
                    digits = 2
                else:
                    digits = 1
                if matrices[i][j][k] > 0:
                    if digits != 4:
                        template_content = template_content.replace(matrix_index, str(f" {matrices[i][j][k]:.{4-digits}f}"))
                    else:
                        template_content = template_content.replace(matrix_index, str(f" {matrices[i][j][k]:.{4-digits}f} "))

                elif matrices[i][j][k] == -0.0:
                    if digits != 4:
                        template_content = template_content.replace(matrix_index, str(f" {abs(matrices[i][j][k]):.{4-digits}f}"))
                    else:
                        template_content = template_content.replace(matrix_index, str(f" {abs(matrices[i][j][k]):.{4-digits}f} "))                    

                else:
                    if digits != 4:     
                        template_content = template_content.replace(matrix_index, str(f"{matrices[i][j][k]:.{4-digits}f}"))
                    else: 
                        template_content = template_content.replace(matrix_index, str(f"{matrices[i][j][k]:.{4-digits}f} "))

    # the above for loops systematically loop through all of the placeholders in template.txt and replace the 
    # placeholders with the values calculated (placeholders like a11 -> a33, b11 -> b33 etc.)
    # we check how many decimal places the values have and if they are negative, this
    # information is used to autoscale the matrices nicely
    # this works for numbers from -9999 up to 9999
    
    template_content = template_content.replace("ACTION",calculated)
    template_content = template_content.replace("Svd",matrix_saved_in)  # the performed calculation and matrix_saved_in
                                                                        # are displayed for the user in the UI
    template_content = template_content.replace("DETA",str(f"{det_A:8f}"))
    template_content = template_content.replace("DETB",str(f"{det_B:.8f}"))
    template_content = template_content.replace("DETC",str(f"{det_C:.8f}"))      # the determinants are displayed in the UI
    template_content = template_content.replace("DETZ",str(f"{det_Ans:.8f}"))
    template_content = template_content.replace("DETSOL",str(f"{det_Sol:.8f}"))

    try:
        with open (output_file,"w",encoding= "utf-8") as refreshed_UI:
            refreshed_UI.write(template_content)
    except: print(f"Error: ' {output_file} ' does not exist")  # here we overwrite what is in Output_File.txt with the
                                                               # modified Template                  


####################################################################
##  Calculation                                                   ##
####################################################################

# here the actual calculations happens, calculate() checks the operator and correctly instructs
# either addition(), subtraction(), multiplication(), invert() or transpose() to start
# those functions will then perform the correct calculation algorithm and overwrite matrix_Sol with the solution

def calculate(operand_1,operand_2,operator):   # chooses which function is needed for the operation and execute it

    if operator == "*":
        multiplication(operand_1, operand_2)
    if operator == "+":
        addition(operand_1,operand_2) 
    if operator == "-":
        subtraction(operand_1,operand_2)
    if operator == "i":
        invert(operand_1)
    if operator == "t":
        transpose(operand_1,matrix_Sol)
    
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


def determinant():   # calculates the determinants of all matrices

    det_matrices = [matrix_A, matrix_B, matrix_C, matrix_Ans, matrix_Sol]
    det = [det_A, det_B, det_C, det_Ans, det_Sol]
    for i in range(5):
        det[i] = det_matrices[i][0][0] * det_matrices[i][1][1] * det_matrices[i][2][2] + det_matrices[i][0][1] * det_matrices[i][1][2] * det_matrices[i][2][0] + det_matrices[i][0][2] * det_matrices[i][1][0] * det_matrices[i][2][1] - det_matrices[i][0][2] * det_matrices[i][1][1] * det_matrices[i][2][0] - det_matrices[i][0][1] * det_matrices[i][1][0] * det_matrices[i][2][2] - det_matrices[i][0][0] * det_matrices[i][1][2] * det_matrices[i][2][1]
    return det   # returns a list that contains the determinant of each matrix

def invert(operand_1):    # calculates the inverse of a matrix

    if operand_1 == matrix_A:
        determinant_operand = determinant()[0]
    elif operand_1 == matrix_B:
        determinant_operand = determinant()[1] 
    elif operand_1 == matrix_C:
        determinant_operand = determinant()[2]
    elif operand_1 == matrix_Ans:
        determinant_operand = determinant()[3]     
    if determinant_operand != 0:
        matrix_Sol[0][0] = ((operand_1[1][1] * operand_1[2][2]) - (operand_1[1][2] * operand_1[2][1])) / determinant_operand
        matrix_Sol[0][1] = ((operand_1[0][2] * operand_1[2][1]) - (operand_1[0][1] * operand_1[2][2])) / determinant_operand
        matrix_Sol[0][2] = ((operand_1[0][1] * operand_1[1][2]) - (operand_1[0][2] * operand_1[1][1])) / determinant_operand
        matrix_Sol[1][0] = ((operand_1[1][2] * operand_1[2][0]) - (operand_1[1][0] * operand_1[2][2])) / determinant_operand
        matrix_Sol[1][1] = ((operand_1[0][0] * operand_1[2][2]) - (operand_1[0][2] * operand_1[2][0])) / determinant_operand
        matrix_Sol[1][2] = ((operand_1[0][2] * operand_1[1][0]) - (operand_1[0][0] * operand_1[1][2])) / determinant_operand
        matrix_Sol[2][0] = ((operand_1[1][0] * operand_1[2][1]) - (operand_1[1][1] * operand_1[2][0])) / determinant_operand
        matrix_Sol[2][1] = ((operand_1[0][1] * operand_1[2][0]) - (operand_1[0][0] * operand_1[2][1])) / determinant_operand
        matrix_Sol[2][2] = ((operand_1[0][0] * operand_1[1][1]) - (operand_1[0][1] * operand_1[1][0])) / determinant_operand
    else:
        print("Error: Matrix is not invertible")
        print("The calculation was canceled!")
    # the inverse is stored in matrix_Sol

def transpose(matrix_Operand_1,matrix_Sol):  # transposes the matrix

    for i in range(3):
        for j in range(3):
            matrix_Sol[i][j] = matrix_Operand_1[j][i]  # stores the solution in matrix_Sol

####################################################################
##      Matrix input extractor                                    ##
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

####################################################################
##      User Input Extractor                                      ##
####################################################################

# here we ask the user what calculation he wants to perform, and return all the needed information as a list

def getUserInput():

    userInput = [0,0,0,0]

    global matrix_A
    global matrix_B   # needs to be specified again because otherwise the matrices are interpreted as local
    global matrix_C
    global matrix_Ans
    global matrix_Sol

    status = [False,False,False,False]
    while not all(status):
        if status[1] == False:
            print("Type '?' to open the help menue!")
            userInput[1] = input("What is the first Operand? You can choose between A, B, C: ")
            if userInput[1] == "?":

                matrix_A = getMatrix("A")
                matrix_B = getMatrix("B")
                matrix_C = getMatrix("C")
                matrix_Ans = getMatrix("Ans")
                matrix_Sol = getMatrix("Sol")  

                try:
                    with open(help_menue, "r", encoding="utf-8") as help_menue_UI:  # opens Template.txt for reading purposes
                        help_UI = help_menue_UI.read()                            
                except:                                            
                    print(f"Error: '{help_menue}' does not exist")
                
                try:
                    with open (output_file,"w",encoding= "utf-8") as help_menue_UI:
                        help_menue_UI.write(help_UI)
                except: print(f"Error: ' {output_file} ' does not exist")
                   
                input("Press enter to proceed: ")

                refreshUI()
                # if the user has opened the help menue before (inside getUserInput())
                # refresh the UI to reset it to its original state before the help menue was opened

                status = [False,False,False,False]
                userInput[1] = input("What is the first Operand? You can choose between A, B, C: ")

            if userInput[1] not in ["A","B","C"]:
                print("Error: No Operand like this exists")
            else:
                status[1] = True
        if status[0] == False:
            userInput[0] = input("Which Operator do you want to use? You can choose between +, -, *, i and t: ")
            if userInput[0] not in ["+","-","*","i","t"]:
                print("Error: No Operator like this exists")
            elif userInput[0] in ["i","t"]:
                    status[0] = True
                    status[2] = True
            else:
                status[0] = True
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

    # this function asks the user about what calculation to perform and returns a list containing all the
    # needed information

####################################################################
##      Main Programm                                             ##
####################################################################

# This is the main program of the calculator, which makes use of all the defined functions and variables

while True:

    userInput = getUserInput()  # find out what the user wants to do
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
                                                           # the two operands and the operator
                                                        
    if saved_in == "A":
        matrix_A = matrix_Sol
    elif saved_in == "B":
        matrix_B = matrix_Sol
    elif saved_in == "C":
        matrix_C = matrix_Sol
    else:
        matrix_Ans = matrix_Sol
        saved_in = "Ans"            # copy the solution (always stored in matrix_Solution) into the matrix the user defined
                                    # if the user didnt specify the matrix where the solution goes, matrix_Ans will 
                                    # be used by default

    det_A = determinant()[0]
    det_B = determinant()[1]
    det_C = determinant()[2]
    det_Ans = determinant()[3]
    det_Sol = determinant()[4]

    if operator not in ["i", "t"]:
        calculated = op_1 + " " + operator + " " + op_2
        matrix_saved_in = saved_in    # update the variables to show the user the calculation performed and 
                                      # where the solution has been saved
    elif operator == "i":
        calculated = "inverse(" + op_1 + ")"
        matrix_saved_in = saved_in
    elif operator == "t":
        calculated = "transpose(" + op_1 + ")"
        matrix_saved_in = saved_in

    refreshUI()   # as the last step of the program everything will be displayed  for the user in Output_File.txt
    print("Operation completed!")
