
#calaculating of fizz,buzz,and fizzbuzz :- 
input=int(input("Enter a number: "))
if(input%15==0):
    print("fizzbuzz")
elif(input%5==0):
    print("buzz")
elif(input%3==0):
    print("fizz")  
else:
    print("invalid input")
# ---------------------------------------------------------------------------------------------------------------
#loops problems
#1.	Print all numbers from 1 to 100 using a  for  loop. 

for i in range(1,101):
    print(i)
#-------------------------------------------------------------------------------------------------------------------    
#2.	Write a program to print the sum of the first  n  natural  numbers. (n*n+1/ 2)     
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i  
print(f"The sum of the first {n} natural numbers is: {sum}") 
#-------------------------------------------------------------------------------------------------------------------    
#3.	Print all even numbers between 1 and 50 using a  while  loop.
num=0
while num<51:
    num+=1
    if num%2==0:
        print(num)
#-------------------------------------------------------------------------------------------------------------------    
#4.	Write a program to display the multiplication table of a given  number. First 20     
for i in range(1,21):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("------------")    
#-------------------------------------------------------------------------------------------------------------------    
#5.	Reverse a number using a while  loop
num=345
reverse=0
sum=0
i=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    sum+=rem
    num//=10
print(reverse)
print(sum)


#-------------------------------------------------------------------------------------------------------------------    
#6 Write a program to count the number of digits in a given  number using a  while  loop. 
num=input("enter a number: ")
while num:
    print(str(len(num)))
    break 
#---------------------------------------------------------------------------------------------------------------------
#divisble by 3 of given numbers,sum of given numbers,reverse of given numbers,and count
num1 = 54312693
sum=0
rev=0
count=0
while num1 > 0:
    rem = num1 % 10
    sum+=rem
    if rem%3==0:
        print(rem)
    rev=rev*10+rem
    num1 = num1 // 10
    count+=1
print(rev)
print(sum)
print("count",count)
#medium lopps
# 4.Print all numbers from 1 to 100 that are divisible by 3 and 5  using a  for  loop. 
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)

 