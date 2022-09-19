from re import A
import mysql.connector
yukidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuki$0623@",
    database="rds_hotel"
)
print(yukidb)
mycursor=yukidb.cursor()
print("welcome RDS hotel")
coustmer=input("veg or nonveg:")
if coustmer=="veg":
 mycursor.execute("SELECT items FROM rds_hotel.veg")
 for items in mycursor:
     print(items)
 enter=input("what do you want:")
 if enter=="dosa" or  enter=="idly" or enter=="poori" or enter=="vadai" or enter=="pongal":
    print(f"{enter} available")
    how_many=int(input(f"How many {enter} you want:"))
    mycursor.execute=("SELECT amount FROM rds_hotel.veg where items='%s'"%(enter))
    user=input("you want cooldrinks:")
    if  user=="yes":
        cool=input("which drinks you want:")
        if cool=="pepsi" or cool=="sprite":
                print(f"{cool} avialable")
                bottles=int(input(f"How many {cool} bottles you want:")) 
                mycursor.execute=("SELECT amount FROM rds_hotel.veg where items='%s'"%(enter)) and ("SELECT amount FROM rds_hotel.drinks where items='%s'"%(cool)) or ("SELECT amount FROM rds_hotel.drinks where items='%s'"%(cool))
                result=mycursor.fetchall()
                for x in result:
                    total=enter*how_many+cool*bottles
                    print(total)
        else:
                   print("{cool}  not available...")
    elif user=="no":
         mycursor.execute=("SELECT amount FROM rds_hotel.veg where items='%s'"%(enter))
         result=mycursor.fetchall()
         for x in result:
          total=enter*how_many
          print(total)
          
elif coustmer=="nonveg":
     mycursor.execute("SELECT items FROM rds_hotel.nonveg")
     for items in mycursor:
      print(items)
     enter=input("what do you want:")
     if enter=="chickenbriyani" or  enter=="muttonbriyani"  or enter=="chickenrice" or enter=="thandoori":
      print(f"{enter} available")
     how_many=int(input(f"How many {enter} you want:"))
     mycursor.execute=("SELECT amount FROM rds_hotel.nonveg where items='%s'"%(enter))
     user=input("you want cooldrinks:")
     if  user=="yes":
        cool=input("which drinks you want:")
        if cool=="pepsi" or cool=="sprite":
                print(f"{cool} avialable")
                bottles=int(input(f"How many {cool} bottles you want:")) 
                mycursor.execute=("SELECT amount FROM rds_hotel.nonveg where items='%s'"%(enter)) and ("SELECT amount FROM rds_hotel.drinks where items='%s'"%(cool)) or ("SELECT amount FROM rds_hotel.drinks where items='%s'"%(cool))
                result=mycursor.fetchall()
                for x in result:
                    total=enter*how_many+cool*bottles
                    print(total)
        else:
                   print("{cool}  not available...")
     elif user=="no":
         mycursor.execute=("SELECT amount FROM rds_hotel.nonveg where items='%s'"%(enter))
         result=mycursor.fetchall()
         for x in result:
          total=enter*how_many
          print(total)
           

           

else:
                   print("{cool}  not available...")