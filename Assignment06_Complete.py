# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Slai,11.20.2021,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add header and code Here!
        """ Adds a row of data as a dict to a list of dictionaries

        :param task: (string) name of task:
        :param priority: (string) priority:
        :return list_of_rows: (list) of dictionary rows
        """
        row_dic = {"Task": task, "Priority": priority}
        list_of_rows = table_lst.append(row_dic)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task , list_of_rows):
        # TODO: Add header and code Here!
        """ Removes a row of data as a dict to a list of dictionaries

        :param task: (string) name of task:
        :return list_of_rows: (list) of dictionary rows
        """
        for i in range(len(table_lst)):
            if table_lst[i]['Task'] == task:
                del table_lst[i]
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add header and code Here!
        """ Writes list of dictionaries to a file

        :param file_name: (string) name of output file:
        :param list_of_rows: (string) data or list of dictionaries:
        :return list_of_rows: (list) of dictionary rows
        """
        for row in list_of_rows:
            objFile = open(file_name, 'a', encoding='utf-8')
            objFile.write('{task_value},{priority_value}\n'.format(task_value=row['Task'], priority_value=row['Priority']))
        objFile.close()
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        pass  # TODO: Add header and code Here!
        """ Collects user input for task and priority

        :param task: (string) name of task:
        :param priority: (string) priority:
        :return task: (string) name of task for later use
        :return priority: (string) value of priority for later use
        """
        choice = input("\tPlease enter a task:").lower()
        task = choice
        choice = input("\tPlease enter that task's priority:").lower()
        priority = choice
        return task, priority

    @staticmethod
    def input_task_to_remove():
        pass  # TODO: Add header and code Here!
        choice = input("\tPlease enter a task:").lower()
        task = choice
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name_str, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        task , priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task,priority,list_of_rows = table_lst)
        continue  # to show the menu
        IO.output_menu_tasks()

    elif choice_str == '2':  # Remove an existing Task
        # TODO: Add Code Here
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task,list_of_rows = table_lst)
        continue  # to show the menu
        IO.output_menu_tasks()

    elif choice_str == '3':  # Save Data to File
        # TODO: Add Code Here
        Processor.write_data_to_file("ToDoFile.txt", list_of_rows = table_lst)
        continue  # to show the menu
        IO.output_menu_tasks()

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
