# 1. print "Hello world"
print("Hello world")

# 2.Data Type Play: Create variables of each data type 
# (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
a = 5  #integer
b = 2.5 #float
c = "Hello python" #string
d = True  #boolean
e = [1,2,"python",2.5] #list
f = (1,"Sumit",2.3) #tuple
g = {
      "name":"sumit",
      "city":"Garhwa",        #dictionary
      "is_married":False,
      "NameOfSchool":"D.A.V",
      "learnProgramme":"javascript"
    }
h = { 1,3,4,6}  #set
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))

# 3. List Operations: Write a Python program to create a list of numbers from 1 to 10,
# and then add a number, remove a number, and sort the list.
num = [3,4,5,2,6,9,7,8,10,1]
num.append(20)
num.pop()
num = set(num)
num = list(num)
print(num)

# 4.Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
count=0
sum=0
num1 = [10,20,30,40]
for i in range(0,len(num1)):
   count+=1
   sum+=num1[i]
print(sum/count)

# 5.String Reversal: Write a Python function that takes a string and returns the string in reverse order.

def reverse(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    return rev
x = reverse("masai") 
print(x)      

# 6.Count Vowels: Write a Python program that counts the number of vowels in a given string.
str = "sumit"
count = 0
for i in range(0,len(str)):
    if(str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        count+=1
print(count)  

# 7.Prime Number: Write a Python function that checks whether a given number is a prime number
def prime(num):
    count=0
    for i in range(2,num+1):
        if(num%i==0):
            count+=1
    if(count==1):
        print("Prime number")        
    else:
        print("Not Prime")
prime(10)

# 8.Factorial Calculation: Write a Python function that calculates the factorial of a number.
def factorial(num):
    prod=1
    for i in range(1,num+1):
       prod=prod*i
    print(prod)
factorial(5)

# 9.Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.
Sum=0
def Fibonacci(num):
    if(num==0 or num==1):
        return num
    return  Fibonacci(num-1)+Fibonacci(num-2)
x=Fibonacci(7)
print(x)

# 10.List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.

list_comprehension = [i**2 for i in range(1,11)]
print(list_comprehension)
