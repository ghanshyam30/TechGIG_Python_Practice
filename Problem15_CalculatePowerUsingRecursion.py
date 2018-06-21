''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def calculate_power(base, exponent):
    if exponent:
        return  base * calculate_power(base, exponent-1)
    return 1
    
def main():

 # Write code here 
    inputs = raw_input()
    
    base = int(inputs.split(" ")[0])
    exponent = int(inputs.split(" ")[1])
    result = calculate_power(base,exponent)
    print result

main()