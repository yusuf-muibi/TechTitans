#Write a Python function called find_primes that takes a positive integer n 
#as its parameter and returns a list containing all prime numbers less than or equal to n. 
#A prime number is a natural number greater than 1
# that is not a product of two smaller natural numbers.

#Finding prime numbers

#PSEUDOCODE
#A user defined functn taking in a parameter n.
#we are going to return all numbers starting from a particular number to n.
#Contains a list called prime.
#return prime


def calculate_primes(cal_prime):
    if cal_prime <= 1:
        return False
    for i in range(2, int(cal_prime**0.5) +1): #assuming cal_prime = 2, 
        if cal_prime % i == 0:
            return False
    return True
    
def find_primes(n):
    primes = []
    for num in range (2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes


n = 20
overall = find_primes(n)
print(overall)







# def find_primes(n, m):
#     print(n*m)

# #to call a function, you just pass in the value into the function name
# find_primes(20, 30)
#write a function that takes in the sum of three parameters and calls it
# def sum(a, b, c):
#     result = a+b+c 
#     #return result #the return statement is always done inside the function(we use it to return the result of a fxn)
#    #return statement should be the last thing you do after everything in a function becanse anything after is invalid
#     print(result)
#     return result 
# # sum(20, 50, 30)
# add = sum(20, 50, 30)
# print(add)


# name = ['damy','bello',28, 34,5.5]
# mylist = [2.4,'tobi', 'yusuf',23]
# num = [2,9,4,1,6]

# print(len(name))
# print(sorted(num))
# num.append(45)
# print(num)
# num.extend([2,3])
# print(num)
# num.insert(1, 56)
# print(num)
# #to remove from a list
# num[:]
# print(num)

# nums = num[::-1]
# print(nums)





