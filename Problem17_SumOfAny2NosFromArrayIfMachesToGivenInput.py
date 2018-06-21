def main():
 # Write code here 
    size_of_list = int(raw_input())
    #Actual List
    string_list = raw_input()
    sum_tobe_found = int(raw_input())
    trueFlag = False
    integer_list = []
    for i in range(0,size_of_list):
        integer_list.append(int(string_list.split(" ")[i]))

    for i in integer_list:
        for j in integer_list:
            if i+j == sum_tobe_found :
                trueFlag = True
                break
        if trueFlag:
            print "True"
            break
        
    if not trueFlag:
        print "False"
    
main()