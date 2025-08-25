'''Q1. Maximum Number in List

Write a program that takes a list of numbers and prints the largest number without using max().
Example:
Input: [3, 7, 2, 9, 5]  
Output: 9'''

a=[3,7,2,9,5]
larger=a[0]
for i in a:
    if i>larger:
        larger=i
print("the larger number is : ",larger)


'''
🔹 Q2. Sum of Even Numbers

Write a program that prints the sum of all even numbers in a list.
Example:
Input: [1, 2, 3, 4, 5, 6]  
Output: 12'''
b=[1,2,3,4,5,6]
sum=0
for i in b:
    if i%2==0:
        sum=sum+i
print("sum of even",sum)


'''Q3. Reverse a List (without using reverse function)

Write a program that prints the list in reverse order.
Example:
Input: [10, 20, 30, 40]  
Output: [40, 30, 20, 10]'''
c=[10,20,30,40]
reverse_list=[]
for i in c:
    reverse_list.insert(0,i)
print(reverse_list)


'''🔹 Q4. Remove Duplicates

Write a program that removes duplicates from a list
Example:
Input: [1, 2, 2, 3, 4, 4, 5]  
Output: [1, 2, 3, 4, 5]
'''
e=[1,2,2,3,4,4]
unique_list=list(set(e))
print(unique_list)

'''Q5. Find Second Largest Number
Write a program to find the second largest number in a list.
Example:
Input: [10, 20, 4, 45, 99]  
Output: 45'''

d=[10, 20, 4, 45, 99] 
biggest=d[0]

for i in d:
    if i>biggest:
        biggest=i
second_biggest=d[0]       
for i in d:
    if i > second_biggest and i != biggest:
        second_biggest=i
print(second_biggest)