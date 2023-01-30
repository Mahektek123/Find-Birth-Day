from datetime import date 
import datetime

a=int(input("Enter your birth year:"))
b=int(input("Enter your birth month:"))
c=int(input("Enter your birth date:"))
td=date.today()
x=datetime.date(a,b,c)
tage=td-x
age=tage/365
age=str(age)
nage=age.replace(age[3:],"")
nage=int(nage)
nage2=nage+1
print("Your completed age is",nage,"and running age is",nage2)
y=input("-:Enter x for exit:-")
