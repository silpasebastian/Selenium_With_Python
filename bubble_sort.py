# Bubble sort in python
# Sorts numbers in ascending order
str_input = input("Please enter numbers separated by spaces")

#split string and store it as a list of integers
numbers =[int(x) for x in str_input.split()]

count=len(numbers)

for j in range(count-1):
    for i in range(count-j-1):
        if(numbers[i]>numbers[i+1]):
            #swap numbers
            temp=numbers[i]
            numbers[i]=numbers[i+1]
            numbers[i+1]=temp
            #or you can use numbers[i],numbers[i+1] = numbers[i+1],numbers[i] to avoid temp
print(numbers)
