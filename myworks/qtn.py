# #Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# #Runner up score is the second highest number in the list
# #psudocode
# #It receives input and uses the while loop as a seperator
# #We are working with a list
# #We will be using a sorted function 
# #We will output the second number of the list

# list = []

# while True:
#     total_score = input("input total score for each team: ")
#     if total_score.lower() == "done":
#         break
#     print(total_score) 
#     list.append(int(total_score))
# list.sort()

# runner_up = list[-2]
# print(f"Our runner_up is {runner_up}")

# #or we use the map function
# list = [1, 2, 3, 4, 5]
# max_num = max(list)
# list.remove(max_num)
# print(max(list))

#or
list_num = []
n = input("input the scores seperated by a comma: ").split(" ")
for i in n:
    int(i)
list_num.append(i)
max_num = max(list_num)
list_num.remove(max_num)
print(max(list_num))


