''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    upperChars = []
    lowerChars = []
    upperCounter = lowerCounter = 0
    stringInput = raw_input()
    for char in stringInput:
        if char.isupper():
            upperChars.append(char)
            upperCounter = upperCounter + 1
        if char.islower():
            lowerChars.append(char)
            lowerCounter = lowerCounter + 1
    print upperCounter
    print lowerCounter
    
main()