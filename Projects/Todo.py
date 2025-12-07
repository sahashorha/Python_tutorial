# List
todo_list = [];
# Add task function  
def add_task():
      task = input("Enter a task: ")
      todo_list.append({"Task" :task , "Status" : "pending"});
      print("New Task Added Successfully.....\n")
# View task fucntion
def view_task():
      print("Your Todo List....")
      if len(todo_list) == 0:
            print("No pending tasks...");
      else:
            for index,task in enumerate(todo_list,1):
                  print(f"{index}: {task['Task']} - {task['Status']}")
# remove task function
def remove_task():
      if(len(todo_list) == 0):                                   
            print("List is Empty")
      else: 
            try:
                  searchIndex = int(input("Enter the task number that you want to remove!: ")) -1;
                  if 0<= searchIndex and searchIndex < len(todo_list):
                        remove_task = todo_list.pop(searchIndex);
                        print(f"Task Removed: {remove_task['Task']}")
                  else:
                        print("Invalid Task Number")
            except:
                  print("Please Enter a valid Task Number: ")
#  mark done function
def mark_done():
      try:
            if len(todo_list) == 0:
                  print("List is Empty...")
            else:
                  searchIndex = int(input("Enter the task number that you want to mark done: ")) -1;
                  if 0 <= searchIndex and searchIndex < len(todo_list):
                        todo_list[searchIndex]['Status'] = 'done'
                        print(f"Task {todo_list[searchIndex]['Task']} has been marked as Done")
                  else:
                        print("Invalid Task Number: ")
      except ValueError:
            print("Please Enter a Valid Task Number")
# menu function
def menu():
      while(True):
            print("*** Menu Item ****")
            print("1. Add a New Task")
            print("2. View All Tasks")
            print("3. Remove a Tasks")
            print("4. Mark a Task Completed")
            print("5. Exit")

            choice = input("Enter Your Choice: ");
            if (choice == '1'):
                  add_task();
            elif(choice == '2'):
                  view_task();
            elif(choice == '3'):
                  remove_task();
            elif (choice == '4'):
                  mark_done();
            else:
                  print("Invalid Choice ! Please Try Again")
menu();

