#---------------------Sorting list using any algo ------------
list1=[5,9,2,7,3,1,8,4]
flag = 0
while flag==0:
   flag = 1
   for item in range(0,len(list1)-1):
	if list1[item] > list1[item+1]:
		temp = list1[item]
		list1[item]=list1[item+1]
		list1[item+1]=temp
		flag = 0
	else:
		item += 1
	
print list1

