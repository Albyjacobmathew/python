'''fileprint=open("filehandling.txt","r")
if fileprint:
    print("Opened successfully")'''

'''file=open("filehandling.txt","a")
file.write("................bye")
file.close'''


#ZIP FUNCTION
#example1 basic usage
list1=[1,2,3]
list2=['a','b','c']
list3=['x','y','z']

zipped_list = zip(list1, list2, list3)
print(zipped_list)
result = list(zipped_list)
print(result)


#Unzipping the zip
unzipped_lists = zip(*result)
print(unzipped_lists)
unzipped_result=[]
#convert the result to seperate list
for item in unzipped_lists:
    unzipped_result.extend(list(item))  #unzipped_result = [list(item) for item in unzipped_lists]

print(unzipped_result)


###
list_1=["name","age","address"]
list_2=["alby",25,"kottayam"]
s = zip(list_1,list_2)
res = dict(s)
print(res)