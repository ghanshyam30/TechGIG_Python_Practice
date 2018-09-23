''' Read input from STDIN. Print your output to STDOUT 
    You just need to take two strings as input from stdin and concatenate them and print the concatenated string to the stdout.

'''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    string1 = input()
    string2 = input()
    string3 = string1 + string2
    string3 = string3.split()
    print(string3[0]+string3[1])
main()


