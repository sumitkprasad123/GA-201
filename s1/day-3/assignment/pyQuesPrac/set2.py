'''1. Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''
for i in range(1,6):
    bag=""
    for j in range(1,i+1):
        bag+=str(j)+" "
    print(bag)    

'''2: Display numbers from a list using loop**

Write a program to display only those numbers from a that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop  '''  
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(0,len(numbers)):
    if(numbers[i]>500):
        break  
    elif(numbers[i]>150):       #using for loop
        continue             
    elif(numbers[i]%5==0):
        print(numbers[i])            

#3: Append new string in the middle of a given string
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
s1 = "Ault"
s2 = "Kelly"
s3=""
for i in range(0,len(s1)):
    if(i==len(s1)/2):
       s3+=s2
    s3+=s1[i]
print(s3)   

# 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
s1,s2="",""
for i in range(0,len(str1)):
    if(str1[i].islower()):
         s1+=str1[i]
    else:
         s2+=str1[i]
print(s1+s2)  

# 5: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
sum1=""
list31=[]
for i in range(0,len(list1)):
    sum1=list1[i]+list2[i]
    list31.append(sum1)
print(list31)    

# 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list32=[]
sum2=""
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
       sum2=list1[i]+list2[j]
       list32.append(sum2)
print(list32)     

# 7: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(0,len(list1)):
     print(list1[i],list2[len(list2)-1-i])
    

# 8: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}   
dic={}
for i in range(0,len(employees)):
     dic[employees[i]]=defaults
print(dic) 

# 9: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dic={}
for key in sample_dict:
    for i in range(0,len(keys)):
        if(key==keys[i]):
           dic[key]=sample_dict[key]
print(dic)

# 10: Modify the tuple
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
x = list(tuple1)
x[1][0]=222
tuple1 = (x)
print(tuple1)