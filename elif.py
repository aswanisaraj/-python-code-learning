#Practicw 01

   total = 600
   discount = 0

 if total >500:
	discount = 10
	total = total - total * discount/100
	elsediscount = 0
		print(total)
		

#Practice 02

 print(" Enter your age:")
 Age = int(input())
 if Age>18:
    print("You can Drive")
 elif Age==18:
     print("We will check")
 else:
     print("You cannot drive")
     
     
     
#Practice 03  

d1=(input("Select your operator Add(+),Sub(-),Mul(*),Div(/)"))
d2=d1.capitalize()
x=int(input("Exter your 1st number "))
y=int(input("Exter your 2nd number "))
if x==45 and y==3 and d2=="Mul":
    print("555")
elif x==56 and y==9 and d2=="Add":
    print("77")
elif x==56 and y==4 and d2=="Div":
    print ("4")
elif d2=="Add":
    z=x+y
    print(z)
elif d2=="Sub":
    z=x-y
    print(z)
elif d2=="Mul":
    z=x*y
    print(z)
elif d2=="Div":
    z=x/y
    print(z) """
