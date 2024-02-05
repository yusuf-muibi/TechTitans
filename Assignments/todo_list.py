print("Welcome to My To-Do List!")

todo_list = []


def mark_task(todo_list, done_sucessfully):
    if not todo_list:
        print("Empty To-do list. No tasks to mark.")
    else:
        print("Your To-Do List: ")
        for index, item in enumerate(todo_list, start=1):
            status = "Done" if item["done"] else "Undone"
            print(f"{index}. {item['task']} - {status}")

        task_index = int(input("Enter the task letter to mark: "))
        if 1 <= task_index <= len(todo_list):
            todo_list[task_index - 1]["done"] = done_sucessfully
            status = "Done" if done_sucessfully else "Undone"
            print(f"Task '{todo_list[task_index - 1]['task']}' marked as {status}!")
        else:
            print("Invalid pick. enter a valid letter.")


while True:

    print("Menu: ")
    print("A. Add Task")
    print("V. View To-Do List")
    print("MD. Mark Task as Done")
    print("MUD. Mark Task as Undone")
    print("Q. Quit")

    todo_pick = input("Enter your choice (A, V, MD, MUD, Q): ")

    if todo_pick == "A":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully!")
    elif todo_pick == "V":
        if not todo_list:
            print("Empty to-do list. Add some tasks!")
        else:
            print("Your To-Do List: ")
            for index, item in enumerate(todo_list, start=1):
                status = "Done" if item["done"] else "Undone"
                print(f"{index}. {item['task']} - {status}")

    elif todo_pick == "MD":
        mark_task(todo_list, True)
    elif todo_pick == "MUD":
        mark_task(todo_list, False)
    elif todo_pick == "Q":
        print("Quit Successfully!")
        break
    else:
        print("Invalid input. Please enter a letter between (A, V, MD, MUD, Q).")
