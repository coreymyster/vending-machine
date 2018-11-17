# Corey Sokol

def userInput():
    num = ''
    userSeq = []
    firstNum = int(input("Enter the first number: "))
    userSeq.append(firstNum)
    while True:
        num = int(input("Next: "))
        if num < -1:
            print("Please enter positive integers only, or enter -1 to quit.")
        elif num == -1:
            break
        else:
            userSeq.append(num)
    return userSeq

def main():    
    print("This program tests if the sequence of positive numbers you input are unique")
    print("Enter -1 to quit")
        
    values = userInput()
    duplicates = []

    for value in values:
        if values.count(value) > 1:
            duplicates.append(value)
    
    if len(duplicates) > 1:
        print("The sequence {} is NOT unique!".format(values))
    else:
        print("The sequence {} is unique!".format(values))
    
main()