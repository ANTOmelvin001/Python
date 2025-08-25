# LEARNING LIST
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


#LEARNING TUPLE
cities=("Erode","coimbator","trichy","chennai")
print(cities[0],cities[2],cities[-1])
print(len(cities))
#2
num=[1,2,3]
tuple_sum=0
for i in num:
    tuple_sum=tuple_sum+i
print(tuple_sum)
print(max(num))
#3
cities=("Erode","coimbator","trichy","chennai")
if "chennai" in cities:
    print("TURE")
else:
    print("FALES")

#PRATICE CODE👌
"""Q1. Swap Two Numbers using Tuple

Write a program to swap two numbers without using a third variable."""
tuple_a=3
tuple_b=4
tuple_a,tuple_b=tuple_b,tuple_a
print(tuple_a,tuple_b)

'''Q2. Count Occurrences in Tuple
Write a program to count how many times a number appears in a tuple.'''
Occurrences=[1,2,3,4,5,1,3,0,2]
target=int(input("enter target:"))

count=0
for i in Occurrences:
    if i==target:
        count +=1
print(count)
# another way
count=Occurrences.count(target)
print("the occurrence is :",count)

'''Find Min and Max in Tuple
Write a program to find the minimum and maximum number in a tuple without using min() or max().'''
# Tuple of numbers
numbers = (5, 2, 9, 1, 7, 3)

# Assume the first number is both min and max
minimum = numbers[0]
maximum = numbers[0]

# Loop through the tuple
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(f"Minimum number is: {minimum}")
print(f"Maximum number is: {maximum}")

