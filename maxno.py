numbers=input("enter the list of numbers")
numbers_list=numbers.split()
for i in range (len(numbers_list)):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
max=numbers_list[0]
for i in range(1,len(numbers_list)):
    if numbers_list[i]>max:
        max=numbers_list[i]
print(f"the maximum number is the above list is {max}")
