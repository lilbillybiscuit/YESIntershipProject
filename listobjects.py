class ToDoList:
    def __init__(self, title="", owner = None):
        self._title = title
        self._owner = owner
        self._items = []
    def get_title(self):
        return self._title

    def get_owner(self):
        return self._owner

    def get_length(self):
        return len(self._items)

    def get_item(self, index):
        return self._items[index]

    def get_list(self):
        return self._items

    def create_list_item(self, data_input_function):
        task_name, due_date, assignee, priority = data_input_function()
        if priority is None:
            priority = False
        item = ToDoListItem(task_name, due_date, assignee, priority)
        self._items.append(item)
        self.sort_list()

    def change_list_item(self, cur_item, data_input_function):
        task_name, due_date, assignee, priority = data_input_function()
        if task_name is not None:
            cur_item.change_task(task_name)
        if due_date is not None:
            cur_item.change_due_date(due_date)
        if assignee is not None:
            cur_item.change_assignee(assignee)
        if priority is not None:
            cur_item.set_priority(priority)
        self.sort_list()

    def sort_key(self, item):
        return item.get_due_date()

    def __str__(self):
        ret = ""
        ret += "="*10 + str(self._title) + "="*10 + "\n"
        ret += "Owned by " +  str(self._owner) + "\n"
        for i in range(len(self._items)):
            ret+= str(i) + " " + str(self._items[i])
        return ret
    def sort_list(self):
        _items_priority = filter(lambda item: item.priority, self._items)
        _items_not_priority = filter(lambda item: not item.priority, self._items)

        _items_priority = sorted(_items_priority, key = self.sort_key)
        _items_not_priority = sorted(_items_not_priority, key=self.sort_key)

        self._items = _items_priority + _items_not_priority

class ToDoListItem:
    def __init__(self, task_name = "", due_date=None, assignee = None, priority=False):
        self._task_name = task_name
        self._due_date = due_date
        self._assignee = assignee
        self._priority = priority
        self._finished = False

    def get_due_date(self):
        return self._due_date

    def set_due_date(self, due_date):
        self._due_date = due_date

    def get_task_name(self):
        return self._task_name

    def set_task_name(self, task_name):
        self._task_name = task_name

    def get_assignee(self):
        return self._assignee

    def set_assignee(self, assignee):
        self._assignee = assignee
    def get_priority(self):
        return self._priority

    def set_priority(self, priority):
        self._priority = priority

    def change_task(self, new_task):
        self.set_task_name(new_task)

    def change_due_date(self, due_date):
        self.set_due_date(due_date)

    def change_assignee(self, assignee):
        self.set_assignee(assignee)

    def finished(self, status=True):
        self._finished = status

    def __str__(self):
        ret = ""
        if self._finished:
            ret+="(FINISHED) "
        else:
            ret+="(INPROGRE) "
        ret+=f"Due: {self._due_date}, Name: {self._task_name}, Assignee: {self._assignee}, Priority: {self._priority}"
        return ret
