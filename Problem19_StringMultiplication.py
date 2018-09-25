''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
    #You just need to take a string and a integer as an input from stdin and repeat the string upto the count given as in integer. 
def main():
    string_input = input()
    repetition = input()
    repetition = int(repetition)
    print(string_input*repetition)
 # Write code here 

main()
