import numpy as np
height = 35
width = 35

# Making a list of all the number to use
# Planning to turn this into a list of symbols  -> * = Prime, - = Not Prime 
listToManipulate = [" " for i in range(1, height*width +1)]
print(len(listToManipulate))
# Provide a blank list and all prime numbered indices will be changed to a * 
def convertToPrimeArrangement (a_list):
    primeNumbersSeen = []
    for i in range(len(a_list)):
        isPrime = True
        if (i+1 > 1):
            for p_num in primeNumbersSeen:
                if (i+1) % p_num == 0:
                    isPrime = False
                
            if (isPrime):
                primeNumbersSeen.append(i+1)
                a_list[i] = "*"
    
    return a_list

# print(listToManipulate)
# print(convertToPrimeArrangement(listToManipulate))

# Now we want to read these numbers into a spiral
finalSpiral = np.full((int(height),int(width)), '_', dtype='U1')
spiralfyMe = convertToPrimeArrangement(listToManipulate)

# Start at the end of list of characters
columnPointer = width -1 
rowPointer = height-1
indexOfList = len(spiralfyMe)-1

# We are going to start working from bottom right corner to the left
movingLeft = True #this means decrease columnPointer 
movingUp = False #this means decrease rowPointer 
movingRight = False #this means increase columnPointer
movingDown = False #this meanse increase rowPointer

def isSquareAvailable(row, col):
    if(row >= width or col >= height or row < 0 or col<0):
        return False
    elif (finalSpiral[row][col] == '_'):
        return True
    return False

while (indexOfList >= 0):
    if (indexOfList == 0):
        finalSpiral[rowPointer][columnPointer] = spiralfyMe[indexOfList]
        indexOfList = indexOfList - 1
    else:
        if(movingLeft):
            #check the left box is available
            finalSpiral[rowPointer][columnPointer] = spiralfyMe[indexOfList]
            if (isSquareAvailable(rowPointer, columnPointer-1)):
                columnPointer = columnPointer -1
                indexOfList = indexOfList - 1
            else :
                movingLeft = False
                movingUp = True
        elif(movingUp):
            #check the left box is available
            finalSpiral[rowPointer][columnPointer] = spiralfyMe[indexOfList]
            if (isSquareAvailable(rowPointer-1, columnPointer)):
                rowPointer = rowPointer -1
                indexOfList = indexOfList - 1
            else :
                movingUp = False
                movingRight = True
        elif(movingRight):
            #check the left box is available
            finalSpiral[rowPointer][columnPointer] = spiralfyMe[indexOfList]
            if (isSquareAvailable(rowPointer, columnPointer + 1)):
                columnPointer = columnPointer +1
                indexOfList = indexOfList - 1
            else :
                movingRight = False
                movingDown = True
        elif(movingDown):
            #check the left box is available
            finalSpiral[rowPointer][columnPointer] = spiralfyMe[indexOfList]
            if (isSquareAvailable(rowPointer+1, columnPointer)):
                rowPointer = rowPointer +1
                indexOfList = indexOfList - 1
            else :
                movingDown = False
                movingLeft = True


# print(spiralfyMe)
print(finalSpiral)

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B33D')

frame = Frame(ws, bg='#F2B33D')

for row in range(len(finalSpiral)):
    for col in range(len(finalSpiral[row])):
        Button(frame, text=finalSpiral[row][col]).grid(row=row, column=col, ipadx = 5)

frame.pack(expand=True) 

ws.mainloop()