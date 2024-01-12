#Q1
unit = int(input("enter your current unit : "))
if unit<=100:
    print("no charges")

if 100<=unit<=200:
    amount=unit-100*5
    print("bill amount=",amount)

elif unit>=200:
    amount=100*0+100*5+(unit-200)*10
    print("bill amount=",amount)

else:
    print("unit is invalid")


#Q2
num=9947338034
num%10
print("last digit is : ",num%10)

#Q3
num=int(input("enter a number"))
last_digit=num%10
if last_digit%3==0:
    print("last digit is divisible by 3")
else:
    print("not divisible by 3")



#Q4
num = int(input("enter a number : "))
if num%5==0:
    print("hello!")
else:
    print("Bye")

#Q5
mark = int(input("enter your mark : "))
if mark >90:
    print("your grade is A")

elif 80>mark<=90:
    print("your grade is B")

elif 60>mark<=80:
    print("your grade is C")

else:
    print("your grade is D")

#Q6
price=int(input("enter price for bike"))
if price>100000:
    tax=price*15/100
    print("tax is",tax)

elif price>50000 and price<=100000:
    tax=price*10/100
    print("tax is",tax)

elif price<=50000:
    tax=price*5/100
    print("tax is",tax)
else:
    print("invalid")


#Q7
day=int(input("enter a number between 1-7: "))
if day==1:
    print("day is Sunday")
elif day==2:
    print("Day Monday")
elif day==3:
    print("day is Tuesday")
elif day==4:
    print("day is Wednesday")
elif day==5:
    print("day is Thursday")
elif day==6:
    print ("day is Friday")
elif day==7:
    print("day is Saturday")
else:
    print("invalid number")

#Q8
month=int(input("enter a number between 1-12: "))
if month==1:
    print("January has 31 days")
elif month==2:
    print("February has 28 days")
elif month==3:
    print("March has 31 days")
elif month==4:
    print("April has 30 days ")
elif month==5:
    print("May has 31 days")
elif month==6:
    print ("June has 30 days")
elif month==7:
    print("July has 31 days")
elif month==8:
    print("August has 31 days")
elif month==9:
    print("September has 30 days")
elif month==10:
    print("October has 31 days ")
elif month==11:
    print("November has 30 days")
elif month==12:
    print ("December has 31 days")
else:
    print("invalid number")

#Q9
cities=["delhi","agra","jaipur"]
print(cities)
city=input("enter a city name")
if city =="delhi":
    print("monument of ",city, "is RedFort")
elif city=="agra":
    print("monument of",city,"is taj mahal")
elif city =="jaipur":
    print("monument of",city,"is jal mahal")
else:
    print("enter the given city")

#Q10
a=9
if (a>5 and a<=10):
    print("hello")
else:
    print("bye")