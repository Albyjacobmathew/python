
#1 python code after removing the syntax error
'''string = "python exception"
for s in string:
    if (s!=o):
        print'''

##2
'''num = int(input("enter a number : "))
if num<=0:
    raise Exception("negative numbers doesn't have factorials")
elif num==0:
    print("factorial of zero is one")

try:
    factorial=1
    i=1
    while i<=num:
        factorial *= i
        i +=1
    print("the factorial of",num,"is:",factorial)
except:
    print("error")'''

#3Value Error
'''try:
    num = int(input("enter a number : "))
    print(num)
except ValueError:
    print("error : Invalid input, input a valid integer")'''

#4
'''def list_program(list1,index):
    try:
        print("the element is :", list1[index])
    except IndexError as e:
        raise Exception("index is out of range",e)
    
limit=int(input("Enter th limit"))
list1=[]
for i in range[limit]:
    number=list(input("enter numbers : "))
    list1.append(number)
print("list elements are : ",list1)
index=int(iput("enter the index of element you want : "))
list_program(list1,index)'''

#5 keyboard Error
try:
    num=int(input("Enter a number : "))
except KeyboardInterrupt as e:
    raise Exception(e)
