# 1. Tuple Unpacking: Create a list of tuples, each containing a name and an age. Then, 
# use tuple unpacking to iterate through the list and print each name and age.
name = ["Amit","Badal","Rahul","Rita","Salini","Priya"]
age = [ 30,20,24,32,28,18]
list=[]
for i in range(0,len(name)):
    list.append((name[i],age[i]))
for l in range(0,len(list)):
    print(list[l][0]+" is "+str(list[l][1])+" year old")    


# 2. Dictionary Manipulation: Create a dictionary with keys as names and values as ages. 
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
dic = {
        "amit":30,
        "badal":20,
        "rahul":24
      }
def add_name_age(name,age):
    dic[name]=age

def update_name_age(name,age):
    dic[name]=age

def delete_name_age(name):
    # del dic[name]
    dic.pop(name)

add_name_age("rahul",24) 
update_name_age("rahul",34) 
delete_name_age("rahul")
print(dic) 

# 3. Two Sum Problem: Given an array of integers and a target integer,
# find the two integers in the array that sum to the target.
num = [2, 7, 11, 15]
target = 9
ans=[]
sum=0

for i in range(0,len(num)):
    for j in range(i,len(num)):
        sum=num[i]+num[j]
        if(sum==target):
            ans.append(i)
            ans.append(j)
            break
print(ans)


# 4.Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.
str = "madam"

def reverse(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    return rev
x = reverse(str)

if(str==x):
    print("Palindrome")
else:
    print("Not Palindrome") 



# 5.Selection Sort: Implement the selection sort algorithm in Python.
list = [64, 25, 12, 22, 11]  #[11, 12, 22, 25, 64]
N = len(list)
def selection_sort(arr):
     for i in range(0,N-1):
        min=i
        for j in range(i+1,N):
            if(arr[min]>arr[j]):
                min=j 
       
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
     print(arr)
selection_sort(list)


# 6.Implement Stack using Queue: Use Python's queue data structure to implement a stack.
# push(1), push(2), pop(), push(3), pop(), pop()


# 7.FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three,
#  print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three 
# and five, print "FizzBuzz".

def fizzBuzz():
    ar = []
    for i in range(1,101):
        if(i%3==0 and i%5==0):
            ar.append("FizzBuzz")
        elif(i%3==0):
            ar.append("Fizz")
        elif(i%5==0):
            ar.append("Buzz")
        else:
            ar.append(i) 
    print(ar)               
fizzBuzz()    



# 8.File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
# - *Input*: A text file named "input.txt" with the content "Hello world"
#  *Output*: A text file named "output.txt" with the content "Number of words: 2"
def read_file(file1,file2):
    
     with open(file1,"r") as file:
          reading = file.read()
          words = reading.split()
          count = len(words)
      
     with open(file2, 'w') as file:
          file.write("Number of words: 2")
          
file1 = "input.txt"
file2 = "output.txt"

read_file(file1,file2)
  

# 9. Exception Handling: Write a Python function that takes two numbers as inputs 
# and returns their division, handling any potential exceptions (like division by zero).

def exception_handling():
   num1 = input("enter 1st number ")
   num2 = input("enter 2st number ")
   num1 = int(num1)
   num2 = int(num2)
   if(num1==0 and num2==0):
       print("Cannot divide by zero")
   elif(num2==0):
       print("Cannot divide by zero")
   else:
       x=int(num1)/int(num2)
       print("The divisor is "+str(x))        
exception_handling()       