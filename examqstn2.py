#3rd largest number in a list
my_list=[1,3,5,6,9]
i=0
largest=second=third=my_list[i]
while i<len(my_list):
    if my_list[i]>largest:
        third=second
        second=largest
        largest=my_list[i]
    elif my_list[i]>second:
        third=second
        second=my_list[i]
    elif my_list[i]>third:
        third=my_list[i]

    i+=1
print("third largest number is : ",third)