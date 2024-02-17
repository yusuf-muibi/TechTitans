#Number scrabble is played with the list of numbers between 1 and 9. 
#Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game. 
#However, if all the numbers are used and no player gets exactly 15, the game is a draw.
#PSUEDOCODE
#1. Define a list [1-9]
#2. prompt user to input a number in list
#3. use the remove method to remove picked number
#4. 
list =[]
for i in range(1, 10):
    list.append(i)
print(list)


def scrabble():
    total = 15
    sum = 0
    if len(list) >= 3:
        for i in list:
            sum += i
            if sum == total:
                print("Win")

while True:                
    user1 = int(input("pick a number from 1-9: "))
    usr1_list = []
    list.remove(user1)
    usr1_list.append(user1)
    scrabble(usr1_list)
    