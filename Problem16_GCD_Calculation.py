''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    input_numbers = raw_input()
    no1 = int(input_numbers.split(" ")[0])
    no2 = int(input_numbers.split(" ")[1])
    
    if no1 < no2:
        minNo = no1
        maxNo = no2
    else:
        minNo = no2
        maxNo = no1
    for i in range(1,minNo+1):
        if (maxNo % i) == 0 :
            if (minNo % i) ==  0:
                result = i
    print result
main()