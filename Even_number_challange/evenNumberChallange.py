# Function to check if there are exavlty three exclamation points between two even number
def checkExclamation(string):
        
    firstEven = False   
    exclamation = 0  # to count the exclamation points
    
    for ch in string:
        if ch == '!':
            if firstEven:   # if the first even number has been already seen, increase the count of exclamation points
                exclamation += 1
            else:
                exclamation = 0  
                
        elif ch >= '0' and ch <= '9':  # if the character is a digit
            if int(ch) % 2 == 0:  # if the number is even
                if firstEven:    # if the first even numebr has been already seen, this would be the second even number
                    if exclamation == 3:
                        return True
                    else:
                        exclamation = 0
                else:
                    firstEven = True 
            else:
                firstEven = False   # When an odd number is seen, reset the count of excalamtion point
                exclamation = 0

    return False
      
input_string = input()
print(checkExclamation(input_string))