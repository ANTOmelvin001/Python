# variable = a box where we put things.
# datatypes = the things where we put inside the box.

name = "Anto Melvin" #we give in string -str type.
age = 21 # it in number - int type.
height = 153.00 # it in decimal - float type.
male = "TRUE" # it in TRUE or FALES - bool.

print(name,age,height,male)
print(type(name))
print(type(age))
print(type(height))
print(type(male))

#input and output
print("Welcome to learn python")

color = input("what is your favorite color : ")
print("Nice color")

fav_num = int(input("what is your Favorite Number : "))

print(fav_num)
coding = input("Do you like coding? (yes/no): ").strip().lower()
if coding == "yes":
    print(True)
else:
    print(False)



#logical thinking 
# here we are going to get DOB and convert into age.

Birth_year = int(input("Enter your DOF : "))
print("Your age is" ,2025 - Birth_year)


# operators
a =int(input("Enter a number :"))
b = int(input("Enter a number :"))

print(a+b , a-b ,a*b,a/b,a%b,a*b)


Mark = int(input("Enter a your mark out of 100 :"))
if (Mark>=50):
    print("pass")
else:
    print("Fail")

User = int(input("enter a number :"))
if(User%2 ==0 and User>=10):
    print("True")
else:
    print("False")

#condition statements.
year = int(input("enter a year:"))
if(year%4==0 and year%100 !=0) or (year%400==0):
    print("Leap Year")
else:
    print("not a leap year")


#loop
for i in range(1,21):
    if(i%2==0):
        print(i) #it prints only even number from 1 to 20

#while loop
count =10
while count > 0:
    print("countdown :",count)
    count = count - 1 #it print 10 down to 1

"""loop la locial thinking
Ask the user for a number n
Print the multiplication table of n (from n x 1 to n x 10)
"""
a=8
count =0
while count < 10:
  count = count + 1
  total=a*count
  print(a,"*",count,"=",total)  # it print 8 tables.
  