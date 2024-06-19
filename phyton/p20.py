lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = (input())
    # adding the element
    lst.append(ele)  
    
count = 0
 
# Finding the sum
for i in lst:
    count +=i
 
print("sum = ", count)