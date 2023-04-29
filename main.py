# we'll use a command line version for now
from typing import List

import listobjects
from datetime import datetime

class ToDoListControllerCLI:
    def __init__(self):
        self._todolists: List[listobjects.ToDoList] = []
        self._selected_list: [listobjects.ToDoList, None] = None

    def create_todo_list(self, name: str, owner: str):
        new_todolist = listobjects.ToDoList(name, owner)
        self._todolists.append(new_todolist)

    def create_list_user(self):
        name = input("Name of the new to-do list: ")
        owner = input("Owner of the new to-do list: ")
        self.create_todo_list(name, owner)
    def print_lists(self):
        for todolist in self._todolists:
            print(todolist)

    def print_list_titles(self):
        for i in range(len(self._todolists)):
            cur_todolist = self._todolists[i]
            print(f"{i}: Name: {cur_todolist.get_title()}, Owner: {cur_todolist.get_owner()}")


    def merge_lists(self, list1: listobjects.ToDoList, list2:listobjects.ToDoList):
        "function that allows you to merge two different lists and their items in sorted order"
        pass

    def make_list_within_range(self, time_range):
        # out of time, but would just use the python filter() function
        pass

    def filter_by_parameter(self, parameter_type, value):
        # out of time but would just use the python filter() function with a custom parameter
        pass

    def create_list_item(self):
        if self._selected_list is None:
            print("You must select a list first")
            return

        self._selected_list.create_list_item(self.get_user_task_info)

    def select_list(self):
        print("Select a list using the list number: ")
        self.print_list_titles()
        user_input = self.input_number((0, len(self._todolists)-1))

        self._selected_list = self._todolists[user_input]

    def input_number(self, allowed_range: (int,int)):
        while True:
            try:
                user = int(input("> "))
                if allowed_range is None:
                    return user
                if user >= allowed_range[0] and user <=allowed_range[1]:
                    return user
                else:
                    raise Exception
            except:
                print("You must enter a valid number")
    def get_list_item(self):
        print("Choose an element from the list below")
        print(self._selected_list)
        user_input = self.input_number((0, self._selected_list.get_length()-1))
        return self._selected_list.get_item(user_input)


    def change_list_property(self):
        item = self.get_list_item()
        self._selected_list.change_list_item(item, self.get_user_task_info)

    def mark_finished(self):
        item = self.get_list_item()
        item.finished()

    def start(self):
        options = {
            "1": ("Show all lists", self.print_lists),
            "2": ("Create a list", self.create_list_user),
            "3": ("Select a list", self.select_list),
            "4": ("Add a list item", self.create_list_item),
            "5": ("Change List Property", self.change_list_property),
            "6": ("Mark an item as finished", self.mark_finished),
            "7": ("Merge two different lists", self.merge_lists),
            "8": ("Make lists within time range", self.make_list_within_range)
        }
        while True:
            print("Hi! Welcome to the to-do list, please enter an option:")
            if self._selected_list is None:
                print("No list selected")
            else:
                print("Currently selected list is " + self._selected_list.get_title())

            for key in options:
                print(key, " ", options[key][0])
            choice = self.input_number((1, len(options)))
            choice_function = options[str(choice)][1]
            choice_function()

    def get_user_task_info(self):
        task_name = input("Please enter a task name:\n")
        due_date = input("Please enter a due date in the format MM-DD-YYYY (or press empty to leave it blank):\n")
        if (due_date == ""):
            due_date = None
        else:
            due_date = datetime.strptime(due_date, "%M-%d-%Y")


        assignee = input("Please enter an assignee (or press empty to leave it blank):\n")
        if assignee == "":
            assignee = None
        priority = input("Is this a priority? (Y/N)\n")
        if priority == "Y":
            priority=True
        elif priority == "N":
            priority = False
        else:
            priority = None

        return task_name, due_date, assignee, priority

if __name__ == "__main__":
    controller = ToDoListControllerCLI()
    # try:
    #     controller.start()
    # except Exception as e:
    #     print("Sorry, an error occured.")
    #     print(e)
    controller.start()