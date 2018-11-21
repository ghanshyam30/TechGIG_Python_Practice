import datetime
count_temp =  raw_input("elements of the array:")
dummy_count=0
count = int(count_temp)
array_formed = []
print "Enter Elements of array:[separated by enter]"
for i in range(count):
	ele = raw_input()
	converted_ele= int(ele)
	array_formed.append(converted_ele)

print "list formed:",array_formed

def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list
rotate_count=raw_input("places to rotate:")
converted_rotate_count = int(rotate_count)
rotated_list = rightRotate(array_formed,converted_rotate_count)
print "Rotated List:",rotated_list

first = 0
last = count-1
mid = count/2
found_temp = raw_input("element to be found:")
found = int(found_temp)
input_list = rotated_list
iteration=0
def check_element(first,mid,last,found,input_list,iteration):
	iteration += 1	
	print "Iteration=",iteration
	if input_list[first] == found :
		print "found at location:",first+1
		return
	elif input_list[last] == found :
		print "found at location:",last+1
		return
	elif input_list[mid] == found :
		print "found at location:",mid+1
		return
	elif (input_list[first]<found and input_list[mid] >found) or (input_list[last]< found and input_list[mid]<found):
		check_element(first,mid/2,mid,found,input_list,iteration)
	elif (input_list[last] > found and input_list[mid] < found) or (input_list[last]> found and input_list[mid]>found):
		new_mid = last - mid
		new_mid = mid+ (new_mid/2)
		check_element(mid,new_mid,last,found,input_list,iteration)
print "StartTime:",datetime.datetime.now().time()
check_element(first,mid,last,found,input_list,iteration)
print "EndTime:",datetime.datetime.now().time()
for i in rotated_list:
	dummy_count += 1
	if i == found:
		print "found at:",dummy_count
		break
print "NewEndTime:",datetime.datetime.now().time()
