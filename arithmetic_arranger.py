

def arithmetic_arranger(myList, show_answer = False):
    firstOpList = []
    operandList = []
    secOpList   = []
    answerList  = []
    lengthList  = []
    #Check how many problems are in the list
    numProblems = len(myList)
    if numProblems > 4:
        return"Error: Too many problems."
        
    for string in myList:
        question = string.split()
        #Check if the number of digits is over 4
        if len(question[0]) > 4 or len(question[2]) > 4:
            return('Error: Numbers can not be more than four digits.')
            
        #Check to see if the strings of numbers contain digits only
        if not (question[0].isdigit()):
          return('Error: Numbers must only contain digits.')
        if not (question[2].isdigit()):
          return('Error: Numbers must only contain digits.')            
        #Check if the operand is acceptable
        if question[1] == '*':
            return('Error: Operator must be "+" or "-".')
        elif question[1] == '/':
            return('Error: Operator must be "+" or "-".')
            
        
        lineMax = max(len(question[0]),len(question[2]))
        if lineMax == 4:
            numOfLine =6
        elif lineMax == 3:
            numOfLine = 5
        else:
            numOfLine = 4
        lengthList.append(numOfLine)

        firstOpList.append(question[0])
        operandList.append(question[1])
        secOpList.append(question[2])
        if question[1] == '+':
            answer = int(question[0]) + int(question[2])
        elif question[1] == '-':
            answer = int(question[0]) + int(question[2])
        answerList.append(str(answer))

    #Print out the list as a line and format
    for first in firstOpList:
        print(first.rjust(6) + ' '*4, end = '')
    print()

    #Print out the second number along the lines
    for index,value in enumerate(secOpList):
        print(operandList[index] + value.rjust(5) + ' '*4, end= '')
    #Print the bottom line of the equations
    print()    

    for index,value in enumerate(lengthList):
        print(('-'*lengthList[index]).rjust(6) + ' '*4, end='')

    #if True included, include the answer
    if show_answer == True:
        print()
        for answers_stored in answerList:
            print(answers_stored.rjust(6) + ' '*4,end='')
    else:
        return

#Testing cases##

#Must show the answer
#arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"],True)

#No problems
#arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])

#Error:too many problems
#arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])

