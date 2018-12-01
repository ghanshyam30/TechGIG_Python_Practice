#---------------------Sorting list using any algo ------------
list1=[5,9,2,7,3,1,8,4]
flag = 0	#Flag was set later in the program when repetion was needed and to decide when to get out of repetition.
while flag==0:	#While was added later in the code to repete the operation in the for loop
   flag = 1	#This is the key as it reduced the possible count variable's calcualtion time and updation aswell   #CORE of code
   for item in range(0,len(list1)-1):
	if list1[item] > list1[item+1]:
		temp = list1[item]
		list1[item]=list1[item+1]
		list1[item+1]=temp
		flag = 0		#Relation with core of the code
	else:
		item += 1
	
print list1

