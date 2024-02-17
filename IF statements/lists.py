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

# def find_primes(n, m):
#     print(n*m)

# #to call a function, you just pass in the value into the function name
# find_primes(20, 30)
#write a function that takes in the sum of three parameters and calls it
def sum(a, b, c):
    result = a+b+c 
    #return result #the return statement is always done inside the function(we use it to return the result of a fxn)
   #return statement should be the last thing you do after everything in a function becanse anything after is invalid
    print(result)
    return result 
# sum(20, 50, 30)
add = sum(20, 50, 30)
print(add)
