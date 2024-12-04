#Fibonacci sequence

#returns the nth term of the Fibonacci Sequence

index = int(input('Choose an integer from 0 and up ' ))

fib_list = [0, 1]

if index >= 0:
    for index in range(0, index):
        fib_list[index] = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(fib_list[index])
        index += 1
    print(fib_list[index])
else:
    print('-1')



   
   
n = int(input('Enter a positive integer greater than or equal to 2. '))
# create a list of length n and use that with index
index_list = []

for index in range(1, n + 1):
    number = int(index)
    index_list.append(number)

print(index_list)


'''
while n >= 2:

    i = 0
    n += 1
#    n = [n]
#create a list for the indeces


