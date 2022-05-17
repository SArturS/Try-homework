# 1) Ask the user for scientist’s name and birthday to add to the dictionary,
#  and update the JSON file you have on disk with the scientist’s name.
#  If you run the program multiple times and keep adding new names,
#  your JSON file should keep getting bigger and bigger.





# 2)By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# my_lst = [12,24,35,24,88,120,155]
# result = [i for i in my_lst if i != 24]
# print(result)



# 3)Write a program in Python that asks the user to input ten integers of their choice and return them a dictionary
#  whose keys are the integers entered and whose values ​​are the lists of divisors of the numbers entered.
#  Example if the user enters the numbers: 2, 7,14, 9, 1, 4, the program returns the dictionary:
# d = {2: [1,2], 7: [1,7], 14: [1,2,7,14],1: [1], 4: [1,2,4]}.(try to use 'try except' if inputed value is not proper type)


# def listDivisors(n):
#     listDiv =[]
#     for i in range(1,n+1):
#         if n % i == 0:
#             listDiv.append(i)
#     return listDiv  
# my_dict = {}
# for i in range(1,11):
#     n = int(input("Enter integer: "))    
#     my_dict[n] = listDivisors(n)
# print(my_dict)



# 4) Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
    
# my_lst = [1,2,3,4]
# my_str = "emp"
# new_lst = []
# for i in my_lst:
# 	new_lst.append(my_str + str(i))
# print(new_lst)













