# f = open("guru99.txt", "w+")  # Open a file named 'guru99.txt' in write-plus mode.
# for i in range(10):           # Loop through the range from 0 to 9 (10 iterations).
#     f.write("This is line %d\r\n" % (i+1))  # Write a line with the current line number.
# f.close()                     # Close the file.

# g = open("sz88.txt", "w+")
# for i in range(10):
#  g.write("this is line %s\r\n"%(i+1))
# g.close()






# a="Hello"
# b=5
# c=True
# d=2.88
# e=[1,2,3,4,5]
# f=(1,2,3,4)
# print(a[1])
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))






# a=int(input("enter the number"))
# if a<0:
#     print("the number is negative")
# elif a==0:
#     print ("the number is zero")
# else:
#     print("the number is positive")
    
    
    
    
    
# a=444
# b=90
# c=12
# if a>b and a>c:
#     print ("a is great")
# elif b>a and b>c:
#     print ("b is great")
# else:
#     print ("c is great")








# a="hello"
# b="123"
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

    
           
 
 
 
 
           
           
# a=2
# b=15
# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#           print(num)








# s="racecat"

# def pal(s):
#    return s==s[::-1]

# r=pal(s)

# if r:
#     print("Yes")
# else :
#     print("No")




    

    
    
    
# a="Hello"
# print(a[::-1])







# s1="this program is "
# s2="concatenated"
# s3=s1+s2
# print(s3)
# s4="abc"
# print(s4)
# res = [s4[i: j] 
#        for i in range(len(s4)) 
#           for j in range(i + 1, len(s4) + 1)]
# print("All substrings of string are : " + str(res))



 

# def print_me( str): 
#   print(str) 
#   return; 

# print_me("I'm first call to user defined function!") 
# print_me("Again second call to the same function")
# print_me("now the 3rd")





# print("Argument Example") 

# def m_fun(fname):
#     print(fname,"Khan")

# m_fun("sarfaraaz")



 
# #This function has a variable with   
# #name same as s.   
# def f(): 
#     # local scope   
#     s = "Me too." 
#     print(s)   
 
# # Global scope   
# s = "I love Python"  
# f()  
# print(s) 
 
 
 
# def my_func(): 
#     # local scope  
#     x = 10 
#     print("Value inside function:", x)   
 
# # Global scope  
# x = 20 
# my_func() 
# print("Value outside function:",x) 








# def factorial(x): 
#     """This is a recursive function 
#     to find the factorial of an integer""" 
 
#     if x == 1: 
#         return 1 
#     else: 
#         return (x * factorial(x-1)) 
 
 
# num = int(input("enter number : "))
# print("The factorial of", num, "is", factorial(num)) 
        
 
 
 
 
 
 
 
 
    


# list = [1,2,3,4,5,6,7]
# print("inserting at specific")
# list.insert(0,3)
# print(list)

# print(len(list))

# list.remove(4)
# print(list)

# list.append(9)
# print(list)

# list.pop()
# print (list)

# list.clear()
# print(list)




# dict={"Brand":"Ford",
#       "model":"mustang",
#       "year":1964
#       }

# print(dict)

# print("Accessing")
# x=dict["model"]
# print(x)

# print("GET METHOD")
# y=dict.get("model")
# print(y)

# print("changing value")
# dict["year"]=2025
# print(dict)


# print("print dictionary elements")
# print(len(dict))










# tup=(1,2,3,4,5)
# print(type(tup))

# print("adding in tuple")
# y=list(tup)
# print(y)
# y.append(9)
# print(y)

# print("Checking an item in tuple")
# if 2 in tup:
#     print("Yes 2 is in tuple")
# else:
#     print("No")
    
# print("accessing tuple items")
# print(tup[0])


# print("loop in tuple")
# for i in tup:
#     print(i)

# print("len of this tuple")
# print(len(tup))









# arr=[5,13,9,77,25,3]
# print("sorting in ascending")
# ascending=sorted(arr)
# print(ascending)

# print("sorted in descending")
# descending=sorted(arr,reverse=True)
# print(descending)








# x=lambda a:a+10
# print(x(5))

# y=lambda a:a*2
# print(y(10))

# x=lambda a,b:a+b
# print(x(14,15))






# list1=[1,5,4,6,8,11,3,12,66,99,78]
# nlist=list(filter(lambda x:(x%2==0),list1))
# print(nlist)










# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y

# print("Select the operations")
# print("1 Add")
# print("2 Sub")
# print("3 Mul")
# print("4 Div")

# while True:
#     choice=input("ENTER CHOICE(1/2/3/4) : ")
    
#     if choice in ('1', '2', '3', '4'):
#         n1=float(input("Enter Num 1 : "))
#         n2=float(input("Enter Num 2 : "))
  
#     if choice == '1':
#       print(n1, "+", n2, "=" , add(n1,n2))
#     elif choice == '2':
#       print(n1, "+", n2, "=" , sub(n1,n2))
#     elif choice == '3':
#       print(n1, "+", n2, "=" , mul(n1,n2))
#     elif choice == '4':
#       print(n1, "+", n2, "=" , div(n1,n2))
#     else:
#           print("Invalid choice")
#     break

      

    
    
 
# class Person: 
#   def __init__(self, name, age): 
#     self.name = name 
#     self.age = age 
 
# p1 = Person("John", 36) 
 
# print(p1.name) 
# print(p1.age) 




# #Create a new file  
# f = open("itworkshop.txt", "w") 
# f = open("abc.txt", "w") 
# #Write to an Existing File 
# #Open the file "demofile2.txt" and append content to the file: 
# f = open("itworkshop.txt", "a") 
# f.write("Now the file has more content!") 
# f.close() 
 
# #open and read the file after the appending: 
# f = open("itworkshop.txt", "r") 
# print(f.read()) 
 
# # Close file 
# f = open("itworkshop.txt", "r") 
# print(f.readline()) 
# f.close() 
# #Check if file exists, then delete it: 
# import os 
# if os.path.exists("abcd.txt"): 
#    os.remove("abc.txt") 
# else: 
#      print("The file does not exist") 
# #Delete file 
# import os 
# os.remove("abc.txt") 






# class A(object): 
#     def __new__(cls): 
        
#          print("Creating instance") 
#          return super(A, cls).__new__(cls) 
   
#     def __init__(self): 
#         print("Init is called") 
   
# A()



#  #Inheritance Concept using the Quadrilateral  
# class quadriLateral: 
#   def __init__(self, a, b, c, d): 
#     self.side1=a 
#     self.side2=b 
#     self.side3=c 
#     self.side4=d 
 
# def perimeter(self): 
#         p=self.side1 + self.side2 + self.side3 + self.side4 
#         print("perimeter=",p) 
 
# q1=quadriLateral(7,5,6,4) 
# q1.perimeter() 
 
# class rectangle(quadriLateral): 
#     def __init__(self, a, b): 
#      super().__init__(a, b, a, b) 
# r1=rectangle(10, 20) 
# r1.perimeter()



# Base class
# class quadriLateral: 
#     def __init__(self, a, b, c, d): 
#         self.side1 = a 
#         self.side2 = b 
#         self.side3 = c 
#         self.side4 = d 
 
#     def perimeter(self): 
#         p = self.side1 + self.side2 + self.side3 + self.side4 
#         print("Perimeter =", p) 

# # Derived class
# class rectangle(quadriLateral): 
#     def __init__(self, a, b): 
#         # Call the constructor of the base class with sides of a rectangle
#         super().__init__(a, b, a, b) 

# # Instantiate and test
# q1 = quadriLateral(7, 5, 6, 4) 
# q1.perimeter()  # Expected output: Perimeter = 22

# r1 = rectangle(10, 20) 
# r1.perimeter()  # Expected output: Perimeter = 60



 
# #The following program demonstrates method overriding in action: 
# class A: 
#     def explore(self): 
#         print("explore() method from class A") 
 
# class B(A): 
#     def explore(self): 
#         print("explore() method from class B") 
 
# b_obj =B() 
# a_obj =A() 
# b_obj.explore() 
# a_obj.explore()


# import re 
 
# pattern = '^a...s$' 
# test_string = 'abyss' 
# result = re.match(pattern, test_string) 
 
# if result: 
#    print("Search successful.") 
# else: 
#    print("Search unsuccessful.") 




# # Initialize array
# arr = [5, 2, 8, 7, 1]
# temp = 0

# # Display elements of the original array
# print("Elements of original array:")
# for i in range(len(arr)):
#     print(arr[i], end=" ")

# # Sort the array in ascending order
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] < arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# # Display elements of sorted array
# print("\nElements of sorted array in ascending order:")
# for i in range(len(arr)):
#     print(arr[i], end=" ")






# from tkinter import*
# root=Tk()
# root.title("Python programming lab")
# root.geometry('350x200')
# menu=Menu(root)
# item=Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File',menu=item)
# root.config(menu=menu)
# lbl=Label(root,text='Are u a student')
# lbl.grid()


# import numpy as np
# arr1=np.array([10,11,12,13,14,15])
# arr2=np.array([20,21,22,23,24,25])
# newarr=np.add(arr1,arr2)
# print(newarr)


# from scipy import constants
# print(dir(constants))
# print(constants.pi)
# print(constants.minute)
# print(constants.hour)
# print(constants.day)
# print(constants.week)
# print(constants.year)
# print(constants.Julian_year)



# import os
# os.getcwd()
# os.chdir('C:\Users\mdsar\OneDrive\Desktop\SM3\Plab')
# print(os.getcwd())
# os.mkdir('New folder')


import random
num=random.randrange(1,10)
print(num)
ran_s=random.choice('Random module')
print(ran_s)
ran1=random.choice([1,2,3,4,5,6])
print(ran1)

list=[23,44,56,2,9,67]
random.shuffle(list)
print(list)